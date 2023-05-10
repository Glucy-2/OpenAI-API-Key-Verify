#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import sys
import time
import chardet
import datetime
import requests
from requests.utils import get_environ_proxies
import logging
from logging import debug, info, warning, error, critical
from PySide6.QtCore import QThread, QObject, Signal, Slot
from PySide6.QtWidgets import *
from gui import main_form_ui


class Config:
    endpoint = "https://api.openai.com"
    use_sys_proxy = True
    proxy_pool = {}  # "http://example.com:8080": 0
    max_conn_per_proxy = 1
    thread_count_from_proxies = True
    thread_count = 1
    delay = 3
    keys_to_query = []
    query_usage_days = 100


class KeyExtract(QObject):
    finished = Signal(list)

    def __init__(self, file_list):
        super().__init__()
        self.file_list = file_list

    def run(self):
        all_keys = []
        for file in self.file_list:
            with open(file, "rb") as f:
                encoding = chardet.detect(f.read())["encoding"]
                debug(f"检测到 {file} 的编码：{encoding}")
            with open(file, "r", encoding=encoding) as f:
                info(f"读取文件 {file}")
                keys = re.findall(r"sk-[a-zA-Z0-9]{48}", f.read())
                # debug(f"Found keys in {file}: {keys}")
                all_keys.extend(keys)
        all_keys = list(set(all_keys))
        invaild_keys = []
        for key in all_keys:
            invaild_keys.append(key) if re.match(
                r"^sk-([a-zA-Z0-9])\1*$", key, re.IGNORECASE
            ) else None
        # debug(f"Invaild keys: {invaild_keys}")
        for invaild_key in invaild_keys:
            all_keys.remove(invaild_key)
        self.finished.emit(all_keys)


class KeyQuery(QObject):
    finished = Signal(tuple)

    def __init__(self, key):
        super().__init__()
        self.key = key
        self.headers = {"Authorization": f"Bearer {self.key}"}

    def run(self, proxy_addr):
        self.proxy = {"http": proxy_addr, "https": proxy_addr} if proxy_addr else None
        s = requests.Session()
        s.trust_env = False
        s.proxies = self.proxy
        try:
            # 查询可用模型
            models_r = s.get(f"{Config.endpoint}/v1/models", headers=self.headers)
            match models_r.status_code:
                # https://platform.openai.com/docs/guides/error-codes/api-errors
                case 200:
                    models_j = models_r.json()
                    if "data" not in models_j:
                        self.finished.emit((
                            proxy_addr,
                            self.key,
                            "成功",
                            f'{models_r.status_code}: {models_r.json()["error"]["message"]}',
                            "无效",
                        ))
                        return
                    # 分类模型
                    gpt4_models = []
                    gpt3_5_models = []
                    gpt3_models = []
                    # https://platform.openai.com/docs/models
                    for model in models_j["data"]:
                        if "gpt-4" in model["id"]:
                            gpt4_models.append(model["id"])
                        if "gpt-3.5" in model["id"]:
                            gpt3_5_models.append(model["id"])
                        if model["id"] in [
                            "text-davinci-003",
                            "text-davinci-002",
                            "code-davinci-002",
                        ]:
                            gpt3_5_models.append(model["id"])
                        if model["id"] in [
                            "text-curie-001",
                            "text-babbage-001",
                            "text-ada-001",
                            "davinci",
                            "curie",
                            "babbage",
                            "ada",
                        ]:
                            gpt3_models.append(model["id"])

                    # 查询到期时间、限额、当前计划
                    sub_r = s.get(
                        f"{Config.endpoint}/dashboard/billing/subscription",
                        headers=self.headers,
                    )
                    sub_j = sub_r.json()
                    access_until = time.strftime(
                        "%xT%X", time.localtime(sub_j["access_until"])
                    )
                    limit_usd = sub_j["hard_limit_usd"]
                    current_plan = f'{sub_j["plan"]["title"]}: {sub_j["plan"]["id"]}'

                    # 查询使用额度
                    now = datetime.datetime.now()
                    usage_r = s.get(
                        f"{Config.endpoint}/dashboard/billing/usage",
                        params={
                            "start_date": (
                                now - datetime.timedelta(days=Config.query_usage_days)
                            ).strftime("%Y-%m-%d"),
                            "end_date": now.strftime("%Y-%m-%d"),
                        },
                        headers={"Authorization": f"Bearer {self.key}"},
                        proxies=self.proxy,
                    )
                    usage_usd = usage_r.json()["total_usage"] / 100

                    self.finished.emit((
                        proxy_addr,
                        self.key,
                        "成功", # 查询状态
                        "", # 错误信息
                        "有效", # 密钥查询结果
                        access_until, # 到期时间
                        limit_usd, # 限额（USD）
                        usage_usd, # 100天内使用额度（USD）
                        current_plan, # 当前计划
                        gpt4_models, # GPT4
                        gpt3_5_models, # GPT3.5
                        gpt3_models, # GPT3
                    ))
                case 401 | 429:
                    self.finished.emit((
                        proxy_addr,
                        self.key,
                        "成功",
                        f'{models_r.status_code}: {models_r.json()["error"]["message"]}',
                        "无效",
                    ))
                case 500:
                    self.finished.emit((
                        proxy_addr,
                        self.key,
                        "失败",
                        f'{models_r.status_code}: {models_r.json()["error"]["message"]}',
                        "未知",
                    ))
                case _:
                    self.finished.emit((
                        proxy_addr, self.key, "成功", f"{models_r.status_code}: {models_r.reason}", "未知"
                    ))
        except Exception as e:
            self.finished.emit((proxy_addr, self.key, "失败", str(e)))
        finally:
            s.close()


class QueryManage(QObject):
    stopped = Signal()
    key_query_status_changed = Signal(tuple)

    def __init__(self):
        super().__init__()

    def query_finished(self, args: tuple):
        debug(f"key查询完成：{args}")
        self.keys_querying.remove(args[1])
        self.thread_count -= 1
        Config.proxy_pool[args[0]] -= 1
        self.key_query_status_changed.emit(args[1:])

    def run(self):
        self.thread_count = 0
        self.query_thread = QThread()
        self.query_workers = []
        self.keys_querying = []
        for key in Config.keys_to_query:
            self.keys_querying.append(key)
            worker = KeyQuery(key)
            worker.moveToThread(self.query_thread)
            worker.finished.connect(self.query_finished)
            self.query_workers.append(worker)
        while self.keys_querying:
            if self.thread_count < Config.thread_count:
                for proxy_addr in Config.proxy_pool.keys():
                    if Config.proxy_pool[proxy_addr] < Config.max_conn_per_proxy:
                        self.thread_count += 1
                        Config.proxy_pool[proxy_addr] += 1
                        worker = self.query_workers.pop(0)
                        debug(f"查询密钥 {worker.key}，代理 {proxy_addr}")
                        worker.run(proxy_addr)
                        self.key_query_status_changed.emit((worker.key,))
        self.query_thread.quit()
        debug("所有key查询结束")
        self.stopped.emit()


class MainWindow(QMainWindow, main_form_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # 绑定信号与槽函数
        self.importFileBtn.clicked.connect(self.import_file)
        self.exportFileBtn.clicked.connect(self.export_file)
        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)
        self.setConfigBtn.clicked.connect(self.set_config)
        self.discardConfigBtn.clicked.connect(self.load_config)

        self.useSystemProxyChkBox.toggled.connect(self.proxy_source_toggled)
        self.threadCountFromProxiesCheckBox.toggled.connect(
            self.thread_count_source_toggled
        )

        # 表格设置
        self.dataTable.setEditTriggers(QTableWidget.NoEditTriggers)

        # 加载配置到图形界面
        self.load_config()

    def proxy_source_toggled(self):
        if self.useSystemProxyChkBox.isChecked():
            self.proxiesTextEdit.setReadOnly(False)
        else:
            self.proxiesTextEdit.setReadOnly(True)

    def thread_count_source_toggled(self):
        if self.threadCountFromProxiesCheckBox.isChecked():
            self.threadCountSpinBox.setEnabled(False)
        else:
            self.threadCountSpinBox.setEnabled(True)

    def load_config(self):
        info("加载配置")
        self.apiEndpointLineEdit.setText(Config.endpoint)
        if Config.use_sys_proxy:
            self.useSystemProxyChkBox.setChecked(True)
            Config.proxy_pool = {}
            for proxy in get_environ_proxies(Config.endpoint).values():
                Config.proxy_pool[proxy] = 0
            self.proxiesTextEdit.setReadOnly(False)
        else:
            self.useSystemProxyChkBox.setChecked(False)
            self.proxiesTextEdit.setReadOnly(True)
        proxy_text = ""
        for proxy in Config.proxy_pool.keys():
            proxy_text += f"{proxy}\n"
        self.proxiesTextEdit.setPlainText(proxy_text)
        self.maxConnPerProxy.setValue(Config.max_conn_per_proxy)
        if Config.thread_count_from_proxies:
            self.threadCountFromProxiesCheckBox.setChecked(True)
            Config.thread_count = len(Config.proxy_pool)
            self.threadCountSpinBox.setEnabled(False)
        else:
            self.threadCountFromProxiesCheckBox.setChecked(False)
            self.threadCountSpinBox.setEnabled(True)
        self.threadCountSpinBox.setValue(Config.thread_count)
        self.delaySpinBox.setValue(Config.delay)

    def set_config(self):
        Config.endpoint = self.apiEndpointLineEdit.text()
        if self.useSystemProxyChkBox.isChecked():
            Config.use_sys_proxy = True
            Config.proxy_pool = {}
            for proxy in get_environ_proxies(Config.endpoint).values():
                Config.proxy_pool[proxy] = 0
            proxy_text = ""
            for proxy in Config.proxy_pool.keys():
                proxy_text += f"{proxy}\n"
            self.proxiesTextEdit.setPlainText(proxy_text)
        else:
            Config.use_sys_proxy = False
            proxies = self.proxiesTextEdit.toPlainText().split()
            for proxy in proxies:
                Config.proxy_pool[proxy] = 0
        Config.max_conn_per_proxy = self.maxConnPerProxy.value()
        if self.threadCountFromProxiesCheckBox.isEnabled():
            Config.thread_count = len(Config.proxy_pool)
            Config.thread_count_from_proxies = False
        else:
            Config.thread_count = self.threadCountSpinBox.value()
            Config.thread_count_from_proxies = True
        Config.delay = self.delaySpinBox.value()
        QMessageBox.information(self, "应用成功", "配置已应用")

    def add_keys(self, new_keys):
        debug("添加密钥到表格")
        row = self.dataTable.rowCount()
        self.dataTable.setRowCount(row + len(new_keys))
        for key in new_keys:
            self.dataTable.setItem(row, 0, QTableWidgetItem(key))
            row += 1
        self.dataTable.resizeColumnsToContents()
        self.dataTable.resizeRowsToContents()
        QMessageBox.information(self, "导入成功", f"成功导入 {len(new_keys)} 个不重复的 key")

    def key_extract_finished(self, keys):
        self.key_extract_thread.quit()
        self.add_keys(keys)

    def key_query_finished(self):
        debug("接收到所有key查询结束信号")
        self.query_manage_thread.quit()
        self.queryProgressBar.setValue(-1)
        self.queryProgressBar.setMaximum(1)
        self.fileGroupBox.setEnabled(True)
        self.settingsGroupBox.setEnabled(True)
        self.doNotQuerySucceededChkBox.setEnabled(True)
        QMessageBox.information(self, "信息", "查询结束")

    def import_file(self):
        self.import_file_list = QFileDialog.getOpenFileNames(self, "选择任意包含key的一个或多个文件")[
            0
        ]
        if self.import_file_list:
            self.key_extract_worker = KeyExtract(self.import_file_list)
            self.key_extract_thread = QThread()
            self.key_extract_worker.moveToThread(self.key_extract_thread)
            self.key_extract_worker.finished.connect(self.key_extract_finished)
            self.key_extract_thread.start()
            self.key_extract_worker.run()

    def export_file(self):
        QMessageBox.warning(self, "未实现", "未实现")

    def change_query_status(self, data):
        debug(f"接收到key查询结果：{data}")
        for row in range(self.dataTable.rowCount()):
            if self.dataTable.item(row, 0).text() == data[0]:
                column = 1
                for dt in data[1:]:
                    self.dataTable.setItem(row, column, QTableWidgetItem(str(dt)))
                    column += 1
                break
        else:
            warning(f"{data[0]} 似乎不在表格中")

    def start(self):
        self.queryProgressBar.setValue(-1)
        self.queryProgressBar.setMaximum(0)
        self.fileGroupBox.setEnabled(False)
        self.settingsGroupBox.setEnabled(False)
        self.doNotQuerySucceededChkBox.setEnabled(False)
        only_query_succeeded = self.doNotQuerySucceededChkBox.isChecked()
        Config.keys_to_query = []
        for row in range(self.dataTable.rowCount()):
            if only_query_succeeded and self.dataTable.item(row, 1) and self.dataTable.item(row, 1).text() == "成功":
                continue
            else:
                Config.keys_to_query.append(self.dataTable.item(row, 0).text())
                self.dataTable.setItem(row, 1, QTableWidgetItem("等待"))
        self.queryProgressBar.setValue(0)
        self.queryProgressBar.setMaximum(len(Config.keys_to_query))
        if Config.keys_to_query == []:
            QMessageBox.warning(self, "警告", "没有需要查询的key")
            self.stop()
            return

        self.query_manage_worker = QueryManage()
        self.query_manage_thread = QThread()
        self.query_manage_worker.moveToThread(self.query_manage_thread)
        self.query_manage_worker.key_query_status_changed.connect(self.change_query_status)
        self.query_manage_worker.stopped.connect(self.key_query_finished)
        self.query_manage_thread.start()
        self.query_manage_worker.run()

    def stop(self):
        Config.keys_to_query = []
        self.queryProgressBar.setValue(-1)
        if self.query_manage_thread.isRunning():
            self.queryProgressBar.setMaximum(0)
        else:
            self.queryProgressBar.setMaximum(1)
        self.fileGroupBox.setEnabled(True)
        self.settingsGroupBox.setEnabled(True)
        self.doNotQuerySucceededChkBox.setEnabled(True)


def run():
    if sys.gettrace():
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    app = QApplication([])  # 创建 QApplication 对象
    try:
        w = MainWindow()
        # 展示窗口
        w.show()
        app.exec()
    except Exception as e:
        critical(f"打开窗口时发生错误，错误信息：{e}")
    finally:
        # 在应用程序关闭之前停止Qt对象的运行
        app.quit()


if __name__ == "__main__":
    run()
