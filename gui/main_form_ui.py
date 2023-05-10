# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 671)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.queryGroupBox = QGroupBox(self.centralwidget)
        self.queryGroupBox.setObjectName("queryGroupBox")
        self._4 = QGridLayout(self.queryGroupBox)
        self._4.setObjectName("_4")
        self.stopBtn = QPushButton(self.queryGroupBox)
        self.stopBtn.setObjectName("stopBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)

        self._4.addWidget(self.stopBtn, 2, 0, 1, 2)

        self.startBtn = QPushButton(self.queryGroupBox)
        self.startBtn.setObjectName("startBtn")
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)

        self._4.addWidget(self.startBtn, 0, 0, 1, 2)

        self.doNotQuerySucceededChkBox = QCheckBox(self.queryGroupBox)
        self.doNotQuerySucceededChkBox.setObjectName("doNotQuerySucceededChkBox")
        self.doNotQuerySucceededChkBox.setChecked(True)

        self._4.addWidget(self.doNotQuerySucceededChkBox, 1, 0, 1, 1)

        self.queryProgressBar = QProgressBar(self.queryGroupBox)
        self.queryProgressBar.setObjectName("queryProgressBar")
        self.queryProgressBar.setMaximum(1)

        self._4.addWidget(self.queryProgressBar, 3, 0, 1, 1)

        self.gridLayout.addWidget(self.queryGroupBox, 1, 0, 1, 1)

        self.dataGroupBox = QGroupBox(self.centralwidget)
        self.dataGroupBox.setObjectName("dataGroupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.dataGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.dataGroupBox.setSizePolicy(sizePolicy1)
        self._3 = QGridLayout(self.dataGroupBox)
        self._3.setObjectName("_3")
        self.dataTable = QTableWidget(self.dataGroupBox)
        if self.dataTable.columnCount() < 11:
            self.dataTable.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.dataTable.setObjectName("dataTable")

        self._3.addWidget(self.dataTable, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.dataGroupBox, 3, 0, 1, 2)

        self.fileGroupBox = QGroupBox(self.centralwidget)
        self.fileGroupBox.setObjectName("fileGroupBox")
        self._2 = QGridLayout(self.fileGroupBox)
        self._2.setObjectName("_2")
        self.importFileBtn = QPushButton(self.fileGroupBox)
        self.importFileBtn.setObjectName("importFileBtn")
        sizePolicy.setHeightForWidth(
            self.importFileBtn.sizePolicy().hasHeightForWidth()
        )
        self.importFileBtn.setSizePolicy(sizePolicy)

        self._2.addWidget(self.importFileBtn, 0, 0, 1, 1)

        self.exportFileBtn = QPushButton(self.fileGroupBox)
        self.exportFileBtn.setObjectName("exportFileBtn")
        sizePolicy.setHeightForWidth(
            self.exportFileBtn.sizePolicy().hasHeightForWidth()
        )
        self.exportFileBtn.setSizePolicy(sizePolicy)

        self._2.addWidget(self.exportFileBtn, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.fileGroupBox, 0, 0, 1, 1)

        self.settingsGroupBox = QGroupBox(self.centralwidget)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.settingsGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.settingsGroupBox.setSizePolicy(sizePolicy2)
        self._5 = QGridLayout(self.settingsGroupBox)
        self._5.setObjectName("_5")
        self.delaySpinBox = QDoubleSpinBox(self.settingsGroupBox)
        self.delaySpinBox.setObjectName("delaySpinBox")

        self._5.addWidget(self.delaySpinBox, 7, 2, 1, 2)

        self.discardConfigBtn = QPushButton(self.settingsGroupBox)
        self.discardConfigBtn.setObjectName("discardConfigBtn")

        self._5.addWidget(self.discardConfigBtn, 9, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self._5.addItem(self.verticalSpacer, 5, 0, 1, 4)

        self.label_4 = QLabel(self.settingsGroupBox)
        self.label_4.setObjectName("label_4")

        self._5.addWidget(self.label_4, 7, 0, 1, 2)

        self.threadCountSpinBox = QSpinBox(self.settingsGroupBox)
        self.threadCountSpinBox.setObjectName("threadCountSpinBox")
        self.threadCountSpinBox.setMinimum(1)

        self._5.addWidget(self.threadCountSpinBox, 6, 3, 1, 1)

        self.threadCountFromProxiesCheckBox = QCheckBox(self.settingsGroupBox)
        self.threadCountFromProxiesCheckBox.setObjectName(
            "threadCountFromProxiesCheckBox"
        )
        self.threadCountFromProxiesCheckBox.setChecked(True)

        self._5.addWidget(self.threadCountFromProxiesCheckBox, 6, 1, 1, 2)

        self.setConfigBtn = QPushButton(self.settingsGroupBox)
        self.setConfigBtn.setObjectName("setConfigBtn")

        self._5.addWidget(self.setConfigBtn, 9, 0, 1, 1)

        self.proxiesTextEdit = QPlainTextEdit(self.settingsGroupBox)
        self.proxiesTextEdit.setObjectName("proxiesTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.proxiesTextEdit.sizePolicy().hasHeightForWidth()
        )
        self.proxiesTextEdit.setSizePolicy(sizePolicy3)

        self._5.addWidget(self.proxiesTextEdit, 3, 0, 1, 4)

        self.label_3 = QLabel(self.settingsGroupBox)
        self.label_3.setObjectName("label_3")

        self._5.addWidget(self.label_3, 6, 0, 1, 1)

        self.label = QLabel(self.settingsGroupBox)
        self.label.setObjectName("label")

        self._5.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.settingsGroupBox)
        self.label_2.setObjectName("label_2")

        self._5.addWidget(self.label_2, 2, 0, 1, 1)

        self.useSystemProxyChkBox = QCheckBox(self.settingsGroupBox)
        self.useSystemProxyChkBox.setObjectName("useSystemProxyChkBox")
        self.useSystemProxyChkBox.setChecked(True)

        self._5.addWidget(self.useSystemProxyChkBox, 2, 1, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self._5.addItem(self.verticalSpacer_2, 1, 0, 1, 4)

        self.verticalSpacer_3 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self._5.addItem(self.verticalSpacer_3, 8, 0, 1, 4)

        self.apiEndpointLineEdit = QLineEdit(self.settingsGroupBox)
        self.apiEndpointLineEdit.setObjectName("apiEndpointLineEdit")

        self._5.addWidget(self.apiEndpointLineEdit, 0, 1, 1, 3)

        self.label_5 = QLabel(self.settingsGroupBox)
        self.label_5.setObjectName("label_5")

        self._5.addWidget(self.label_5, 4, 0, 1, 2)

        self.maxConnPerProxy = QSpinBox(self.settingsGroupBox)
        self.maxConnPerProxy.setObjectName("maxConnPerProxy")
        self.maxConnPerProxy.setMinimum(1)
        self.maxConnPerProxy.setValue(1)

        self._5.addWidget(self.maxConnPerProxy, 4, 3, 1, 1)

        self.gridLayout.addWidget(self.settingsGroupBox, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "OpenAI-API-Key-Verify by Glucy2", None
            )
        )
        self.queryGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", "\u67e5\u8be2", None)
        )
        self.stopBtn.setText(
            QCoreApplication.translate("MainWindow", "\u505c\u6b62", None)
        )
        self.startBtn.setText(
            QCoreApplication.translate("MainWindow", "\u5f00\u59cb", None)
        )
        self.doNotQuerySucceededChkBox.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u5df2\u67e5\u8be2\u6210\u529f\u7684\u4e0d\u518d\u67e5\u8be2",
                None,
            )
        )
        self.queryProgressBar.setFormat(
            QCoreApplication.translate("MainWindow", "%v/%m", None)
        )
        self.dataGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", "\u6570\u636e", None)
        )
        ___qtablewidgetitem = self.dataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "\u5bc6\u94a5", None)
        )
        ___qtablewidgetitem1 = self.dataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "\u67e5\u8be2\u72b6\u6001", None)
        )
        ___qtablewidgetitem2 = self.dataTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "\u9519\u8bef\u4fe1\u606f", None)
        )
        ___qtablewidgetitem3 = self.dataTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate(
                "MainWindow", "\u5bc6\u94a5\u67e5\u8be2\u7ed3\u679c", None
            )
        )
        ___qtablewidgetitem4 = self.dataTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", "\u5230\u671f\u65f6\u95f4", None)
        )
        ___qtablewidgetitem5 = self.dataTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate(
                "MainWindow", "\u9650\u989d\uff08USD\uff09", None
            )
        )
        ___qtablewidgetitem6 = self.dataTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "100\u5929\u5185\u4f7f\u7528\u989d\u5ea6\uff08USD\uff09",
                None,
            )
        )
        ___qtablewidgetitem7 = self.dataTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", "\u5f53\u524d\u8ba1\u5212", None)
        )
        ___qtablewidgetitem8 = self.dataTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", "GPT4", None)
        )
        ___qtablewidgetitem9 = self.dataTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", "GPT3.5", None)
        )
        ___qtablewidgetitem10 = self.dataTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", "GPT3", None)
        )
        self.fileGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", "\u6587\u4ef6", None)
        )
        self.importFileBtn.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u5bfc\u5165\uff08\u6216\u62d6\u5165\uff09\u6587\u4ef6",
                None,
            )
        )
        self.exportFileBtn.setText(
            QCoreApplication.translate(
                "MainWindow", "\u5bfc\u51fa\uff08\u8fd8\u6ca1\u505a\uff09", None
            )
        )
        self.settingsGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", "\u8bbe\u7f6e", None)
        )
        self.discardConfigBtn.setText(
            QCoreApplication.translate("MainWindow", "\u4e22\u5f03", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u7ebf\u7a0b\u7b49\u5f85\u65f6\u95f4\uff08\u79d2\uff09\uff1a",
                None,
            )
        )
        self.threadCountFromProxiesCheckBox.setText(
            QCoreApplication.translate(
                "MainWindow", "\u4e0e\u4ee3\u7406\u6570\u76f8\u540c", None
            )
        )
        self.setConfigBtn.setText(
            QCoreApplication.translate("MainWindow", "\u5e94\u7528", None)
        )
        # if QT_CONFIG(tooltip)
        self.proxiesTextEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u683c\u5f0f\uff1a\u534f\u8bae://\u7528\u6237\u540d:\u5bc6\u7801@\u5730\u5740\uff0c\u4ee5\u7a7a\u683c\u3001\u6362\u884c\u6216\u5236\u8868\u7b26\u5206\u9694</p><p>\u5982\u679c\u4e3a\u7a7a\u5219\u4e0d\u4f7f\u7528\u4ee3\u7406</p><p>\u4f8b\uff1a</p><p>http://127.0.0.1:7890</p><p>https://username:password@example.com</p><p>socks5://localhost:8080</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "\u7ebf\u7a0b\u6570\uff1a", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "API\u7aef\u70b9\uff1a", None)
        )
        # if QT_CONFIG(tooltip)
        self.label_2.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u683c\u5f0f\uff1a\u534f\u8bae://\u7528\u6237\u540d:\u5bc6\u7801@\u5730\u5740\uff0c\u4ee5\u7a7a\u683c\u3001\u6362\u884c\u6216\u5236\u8868\u7b26\u5206\u9694</p><p>\u5982\u679c\u4e3a\u7a7a\u5219\u4e0d\u4f7f\u7528\u4ee3\u7406</p><p>\u4f8b\uff1a</p><p>http://127.0.0.1:7890</p><p>https://username:password@example.com</p><p>socks5://localhost:8080</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "\u4ee3\u7406\uff1a", None)
        )
        self.useSystemProxyChkBox.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u4f7f\u7528\u7cfb\u7edf/\u73af\u5883\u53d8\u91cf\u4ee3\u7406",
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u6bcf\u4e2a\u4ee3\u7406\u7684\u6700\u5927\u8fde\u63a5\u6570\uff1a",
                None,
            )
        )

    # retranslateUi
