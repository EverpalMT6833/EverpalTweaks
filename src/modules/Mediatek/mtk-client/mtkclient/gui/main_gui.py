# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(902, 730)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(746, 730))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"	background-color: rgb(101, 114, 138);\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #898988;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #c4c5c3;\n"
"	color: #000000;\n"
"    border: 1px solid #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #979796;\n"
"    border: 1px solid #000;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #c4c5c3;\n"
"    border: 1px solid;\n"
"    color: #000000;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #363942;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
" "
                        "   margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #363942;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #898988;\n"
"}\n"
"\n"
"\n"
"")
        self.actionRead_partition_s = QAction(MainWindow)
        self.actionRead_partition_s.setObjectName(u"actionRead_partition_s")
        self.actionRead_full_flash = QAction(MainWindow)
        self.actionRead_full_flash.setObjectName(u"actionRead_full_flash")
        self.actionRead_offset = QAction(MainWindow)
        self.actionRead_offset.setObjectName(u"actionRead_offset")
        self.actionWrite_partition_s = QAction(MainWindow)
        self.actionWrite_partition_s.setObjectName(u"actionWrite_partition_s")
        self.actionWrite_full_flash = QAction(MainWindow)
        self.actionWrite_full_flash.setObjectName(u"actionWrite_full_flash")
        self.actionWrite_at_offset = QAction(MainWindow)
        self.actionWrite_at_offset.setObjectName(u"actionWrite_at_offset")
        self.actionErase_partitions_s = QAction(MainWindow)
        self.actionErase_partitions_s.setObjectName(u"actionErase_partitions_s")
        self.actionErase_at_offset = QAction(MainWindow)
        self.actionErase_at_offset.setObjectName(u"actionErase_at_offset")
        self.actionRead_RPMB = QAction(MainWindow)
        self.actionRead_RPMB.setObjectName(u"actionRead_RPMB")
        self.actionWrite_RPMB = QAction(MainWindow)
        self.actionWrite_RPMB.setObjectName(u"actionWrite_RPMB")
        self.actionRead_preloader = QAction(MainWindow)
        self.actionRead_preloader.setObjectName(u"actionRead_preloader")
        self.actionGenerate_RPMB_keys = QAction(MainWindow)
        self.actionGenerate_RPMB_keys.setObjectName(u"actionGenerate_RPMB_keys")
        self.actionRead_boot2 = QAction(MainWindow)
        self.actionRead_boot2.setObjectName(u"actionRead_boot2")
        self.actionWrite_preloader = QAction(MainWindow)
        self.actionWrite_preloader.setObjectName(u"actionWrite_preloader")
        self.actionWrite_boot2 = QAction(MainWindow)
        self.actionWrite_boot2.setObjectName(u"actionWrite_boot2")
        self.actionUnlock_device = QAction(MainWindow)
        self.actionUnlock_device.setObjectName(u"actionUnlock_device")
        self.actionLock_device = QAction(MainWindow)
        self.actionLock_device.setObjectName(u"actionLock_device")
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	\n"
"	background-color: rgb(101, 114, 138);\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	bord"
                        "er-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logoPic = QLabel(self.centralwidget)
        self.logoPic.setObjectName(u"logoPic")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logoPic.sizePolicy().hasHeightForWidth())
        self.logoPic.setSizePolicy(sizePolicy1)
        self.logoPic.setMinimumSize(QSize(128, 128))
        self.logoPic.setMaximumSize(QSize(128, 128))
        self.logoPic.setPixmap(QPixmap(u"images/logo_256.png"))
        self.logoPic.setScaledContents(True)
        self.logoPic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.logoPic)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_8.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        self.title.setMinimumSize(QSize(0, 24))
        self.title.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.title.setLineWidth(0)
        self.title.setTextFormat(Qt.AutoText)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.title.setWordWrap(False)
        self.title.setIndent(0)

        self.verticalLayout.addWidget(self.title)

        self.title_2 = QLabel(self.centralwidget)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy1)
        self.title_2.setMinimumSize(QSize(0, 24))
        self.title_2.setMaximumSize(QSize(16777215, 20))
        self.title_2.setFont(font)
        self.title_2.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.title_2.setLineWidth(0)
        self.title_2.setTextFormat(Qt.AutoText)
        self.title_2.setScaledContents(False)
        self.title_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.title_2.setWordWrap(False)
        self.title_2.setIndent(0)

        self.verticalLayout.addWidget(self.title_2)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.copyrightInfo = QLabel(self.centralwidget)
        self.copyrightInfo.setObjectName(u"copyrightInfo")
        sizePolicy1.setHeightForWidth(self.copyrightInfo.sizePolicy().hasHeightForWidth())
        self.copyrightInfo.setSizePolicy(sizePolicy1)
        self.copyrightInfo.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.copyrightInfo)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)


        self.horizontalLayout.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.verticalSpacer_20 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_20)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(40, 13, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.phoneDebugInfoTextbox = QLabel(self.centralwidget)
        self.phoneDebugInfoTextbox.setObjectName(u"phoneDebugInfoTextbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.phoneDebugInfoTextbox.sizePolicy().hasHeightForWidth())
        self.phoneDebugInfoTextbox.setSizePolicy(sizePolicy2)
        self.phoneDebugInfoTextbox.setMinimumSize(QSize(150, 50))
        self.phoneDebugInfoTextbox.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: rgb(213, 213, 213);\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"")
        self.phoneDebugInfoTextbox.setTextFormat(Qt.PlainText)
        self.phoneDebugInfoTextbox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.phoneDebugInfoTextbox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(160, 180))
        self.pic = QLabel(self.widget_3)
        self.pic.setObjectName(u"pic")
        self.pic.setGeometry(QRect(20, 0, 135, 180))
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pic.sizePolicy().hasHeightForWidth())
        self.pic.setSizePolicy(sizePolicy3)
        self.pic.setMinimumSize(QSize(135, 180))
        self.pic.setMaximumSize(QSize(87, 128))
        self.pic.setPixmap(QPixmap(u"images/phone_notfound.png"))
        self.pic.setScaledContents(True)
        self.pic.setAlignment(Qt.AlignCenter)
        self.pic.setWordWrap(False)
        self.spinner_pic = QLabel(self.widget_3)
        self.spinner_pic.setObjectName(u"spinner_pic")
        self.spinner_pic.setGeometry(QRect(50, 90, 71, 71))
        sizePolicy1.setHeightForWidth(self.spinner_pic.sizePolicy().hasHeightForWidth())
        self.spinner_pic.setSizePolicy(sizePolicy1)
        self.spinner_pic.setPixmap(QPixmap(u"images/phone_loading.png"))
        self.spinner_pic.setScaledContents(True)
        self.spinner_pic.setAlignment(Qt.AlignCenter)
        self.phoneInfoTextbox = QLabel(self.widget_3)
        self.phoneInfoTextbox.setObjectName(u"phoneInfoTextbox")
        self.phoneInfoTextbox.setGeometry(QRect(40, 20, 91, 141))
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.phoneInfoTextbox.sizePolicy().hasHeightForWidth())
        self.phoneInfoTextbox.setSizePolicy(sizePolicy4)
        self.phoneInfoTextbox.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"")
        self.phoneInfoTextbox.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.phoneInfoTextbox.setWordWrap(True)
        self.pic.raise_()
        self.phoneInfoTextbox.raise_()
        self.spinner_pic.raise_()

        self.horizontalLayout_6.addWidget(self.widget_3)


        self.verticalLayout_19.addLayout(self.horizontalLayout_6)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_2)

        self.connectInfo = QWidget(self.centralwidget)
        self.connectInfo.setObjectName(u"connectInfo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.connectInfo.sizePolicy().hasHeightForWidth())
        self.connectInfo.setSizePolicy(sizePolicy5)
        self.connectInfo.setMinimumSize(QSize(0, 0))
        self.connectInfo.setMaximumSize(QSize(16777215, 0))
        self.verticalLayout_6 = QVBoxLayout(self.connectInfo)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_7 = QSpacerItem(9, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.initStepsImage = QLabel(self.connectInfo)
        self.initStepsImage.setObjectName(u"initStepsImage")
        self.initStepsImage.setMinimumSize(QSize(685, 330))
        self.initStepsImage.setMaximumSize(QSize(685, 330))
        self.initStepsImage.setFrameShape(QFrame.NoFrame)
        self.initStepsImage.setPixmap(QPixmap(u"images/initsteps.png"))
        self.initStepsImage.setScaledContents(True)
        self.initStepsImage.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.initStepsImage.setWordWrap(False)
        self.initStepsImage.setMargin(0)

        self.horizontalLayout_4.addWidget(self.initStepsImage)

        self.horizontalSpacer = QSpacerItem(5, 18, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.connectInfo)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setMinimumSize(QSize(195, 0))
        self.label_2.setMaximumSize(QSize(195, 16777215))
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.connectInfo)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        self.label_3.setMinimumSize(QSize(195, 10))
        self.label_3.setMaximumSize(QSize(195, 16777215))
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.connectInfo)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        self.label_4.setMinimumSize(QSize(195, 0))
        self.label_4.setMaximumSize(QSize(195, 16777215))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_showdebug = QSpacerItem(50, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_showdebug)

        self.showdebugbtn = QPushButton(self.connectInfo)
        self.showdebugbtn.setObjectName(u"showdebugbtn")

        self.horizontalLayout_5.addWidget(self.showdebugbtn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_19.addWidget(self.connectInfo)

        self.Main = QVBoxLayout()
        self.Main.setSpacing(0)
        self.Main.setObjectName(u"Main")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(650, 400))
        font1 = QFont()
        font1.setPointSize(9)
        self.tabWidget.setFont(font1)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"/*-----QTabWidget-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	width: 100px;\n"
"	height: 12px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	border: 1px groove #333333;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #484c58;\n"
"	color: #ffffff;\n"
"	border: 1px groove #333333;\n"
"	border-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected \n"
"{\n"
"    background-color: #a3a7b2;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"    background-color: #484c58;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:!selected \n"
"{\n"
"    margin-top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:!selected \n"
""
                        "{\n"
"    margin-bottom: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom \n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:selected \n"
"{\n"
"    border-bottom-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:selected \n"
"{\n"
"    border-top-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one \n"
"{\n"
"    margin-right: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:!selected \n"
"{\n"
"    margin-right: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right \n"
"{\n"
"    min-height: 15ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:selected \n"
"{\n"
"    border-left-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:selected \n"
"{"
                        "\n"
"    border-right-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one \n"
"{\n"
"    margin-bottom: 0;\n"
"\n"
"}")
        self.readtab = QWidget()
        self.readtab.setObjectName(u"readtab")
        self.horizontalLayout_8 = QHBoxLayout(self.readtab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.readtitle = QLabel(self.readtab)
        self.readtitle.setObjectName(u"readtitle")
        sizePolicy5.setHeightForWidth(self.readtitle.sizePolicy().hasHeightForWidth())
        self.readtitle.setSizePolicy(sizePolicy5)
        self.readtitle.setMinimumSize(QSize(0, 20))
        self.readtitle.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"")
        self.readtitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.readtitle)

        self.readselectallcheckbox = QCheckBox(self.readtab)
        self.readselectallcheckbox.setObjectName(u"readselectallcheckbox")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.readselectallcheckbox.setFont(font2)
        self.readselectallcheckbox.setStyleSheet(u"/*-----QCheckBox-----*/\n"
"QCheckBox{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: rgb(72, 76, 88);\n"
"    border: 2px solid rgb(163, 167, 178);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: 1px solid #323232;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255, 201, 38);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 2px solid rgb(255, 201, 38);\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_11.addWidget(self.readselectallcheckbox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.readDumpGPTCheckbox = QCheckBox(self.readtab)
        self.readDumpGPTCheckbox.setObjectName(u"readDumpGPTCheckbox")
        self.readDumpGPTCheckbox.setFont(font2)
        self.readDumpGPTCheckbox.setStyleSheet(u"/*-----QCheckBox-----*/\n"
"QCheckBox{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: rgb(72, 76, 88);\n"
"    border: 2px solid rgb(163, 167, 178);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: 1px solid #323232;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255, 201, 38);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 2px solid rgb(255, 201, 38);\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.readDumpGPTCheckbox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.label_8 = QLabel(self.readtab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 1.5px;\n"
"	color:  rgb(235, 235, 235);\n"
"	font-weight: bold;\n"
"	\n"
"background-color: rgb(114, 130, 156)")

        self.verticalLayout_12.addWidget(self.label_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.readpartitionList = QScrollArea(self.readtab)
        self.readpartitionList.setObjectName(u"readpartitionList")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.readpartitionList.sizePolicy().hasHeightForWidth())
        self.readpartitionList.setSizePolicy(sizePolicy7)
        self.readpartitionList.setMinimumSize(QSize(0, 280))
        self.readpartitionList.setStyleSheet(u"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #63676d;\n"
"    height: 18px;\n"
"    margin: 0px 18px 0 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
""
                        "    image: url(://arrow-left.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #63676d;\n"
"    width: 18px;\n"
"    margin: 18px 0 18px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScro"
                        "llBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: rgb(61, 69, 84);\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: rgb(72, 76, 88);\n"
"    border: 2px solid rgb(163, 167, 178);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: 1px solid #323232;\n"
"	border-radius: 7px;\n"
"	b"
                        "ackground-color: rgb(255, 201, 38);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 2px solid rgb(255, 201, 38);\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"")
        self.readpartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.readpartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.readpartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.readpartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 700, 308))
        self.scrollAreaWidgetContents.setStyleSheet(u"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #000000;\n"
"	color: #00ff00;\n"
"	font-weight: bold;\n"
"    border: 1px solid #333333;\n"
"	padding: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    border: 1px solid #00ff00;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTextEdit\n"
"{\n"
"	background-color: #808080;\n"
"	color: #fff;\n"
"	border: 1px groove #333333;\n"
"\n"
"}\n"
"\n"
"\n"
"QTextEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"")
        self.readpartitionList.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.readpartitionList)

        self.verticalSpacer_18 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_18)

        self.readpartitionsbtn = QPushButton(self.readtab)
        self.readpartitionsbtn.setObjectName(u"readpartitionsbtn")
        self.readpartitionsbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")
        self.readpartitionsbtn.setIconSize(QSize(16, 16))

        self.verticalLayout_13.addWidget(self.readpartitionsbtn)


        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.tabWidget.addTab(self.readtab, "")
        self.writetab = QWidget()
        self.writetab.setObjectName(u"writetab")
        self.horizontalLayout_10 = QHBoxLayout(self.writetab)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.writetitle = QLabel(self.writetab)
        self.writetitle.setObjectName(u"writetitle")
        sizePolicy5.setHeightForWidth(self.writetitle.sizePolicy().hasHeightForWidth())
        self.writetitle.setSizePolicy(sizePolicy5)
        self.writetitle.setMinimumSize(QSize(0, 20))
        self.writetitle.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"")
        self.writetitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_15.addWidget(self.writetitle)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_9)

        self.label_9 = QLabel(self.writetab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"	color:  rgb(235, 235, 235);\n"
"	font-weight: bold;")

        self.verticalLayout_15.addWidget(self.label_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_15)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.writepartitionList = QScrollArea(self.writetab)
        self.writepartitionList.setObjectName(u"writepartitionList")
        sizePolicy7.setHeightForWidth(self.writepartitionList.sizePolicy().hasHeightForWidth())
        self.writepartitionList.setSizePolicy(sizePolicy7)
        self.writepartitionList.setMinimumSize(QSize(0, 280))
        self.writepartitionList.setStyleSheet(u"/*-----QCheckBox-----*/\n"
"QCheckBox{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: rgb(72, 76, 88);\n"
"    border: 2px solid rgb(163, 167, 178);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: 1px solid #323232;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255, 201, 38);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 2px solid rgb(255, 201, 38);\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: rgb(61, 69, 84);\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
""
                        "/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"	width: 80px;\n"
"	height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
""
                        "\n"
"\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #000000;\n"
"	color: rgb(255, 175, 56);\n"
"	font-weight: bold;\n"
"    border: 1px solid #333333;\n"
"	padding: 4px;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    border: 1.5px solid rgb(164, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #63676d;\n"
"    height: 18px;\n"
"    margin: 0px 18px 0 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;"
                        "\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #63676d;\n"
"    width: 18px;\n"
"    margin: 18px 0 18px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radi"
                        "us: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.writepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.writepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.writepartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.writepartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 695, 306))
        self.writepartitionList.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.writepartitionList)

        self.verticalSpacer_17 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_17)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.writeselectfromdir = QPushButton(self.writetab)
        self.writeselectfromdir.setObjectName(u"writeselectfromdir")
        self.writeselectfromdir.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.writeselectfromdir)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.writepartbtn = QPushButton(self.writetab)
        self.writepartbtn.setObjectName(u"writepartbtn")
        self.writepartbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.writepartbtn)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_14)

        self.tabWidget.addTab(self.writetab, "")
        self.erasetab = QWidget()
        self.erasetab.setObjectName(u"erasetab")
        self.horizontalLayout_11 = QHBoxLayout(self.erasetab)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.erasetitle = QLabel(self.erasetab)
        self.erasetitle.setObjectName(u"erasetitle")
        sizePolicy5.setHeightForWidth(self.erasetitle.sizePolicy().hasHeightForWidth())
        self.erasetitle.setSizePolicy(sizePolicy5)
        self.erasetitle.setMinimumSize(QSize(0, 20))
        self.erasetitle.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"")
        self.erasetitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.erasetitle)

        self.eraseselectallpartitionscheckbox = QCheckBox(self.erasetab)
        self.eraseselectallpartitionscheckbox.setObjectName(u"eraseselectallpartitionscheckbox")
        self.eraseselectallpartitionscheckbox.setFont(font2)
        self.eraseselectallpartitionscheckbox.setStyleSheet(u"/*-----QCheckBox-----*/\n"
"QCheckBox{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: rgb(72, 76, 88);\n"
"    border: 2px solid rgb(163, 167, 178);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: 1px solid #323232;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255, 201, 38);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 2px solid rgb(255, 201, 38);\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_17.addWidget(self.eraseselectallpartitionscheckbox)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_10)

        self.label = QLabel(self.erasetab)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"	color:  rgb(235, 235, 235);\n"
"	font-weight: bold;")

        self.verticalLayout_17.addWidget(self.label)


        self.horizontalLayout_11.addLayout(self.verticalLayout_17)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.erasepartitionList = QScrollArea(self.erasetab)
        self.erasepartitionList.setObjectName(u"erasepartitionList")
        sizePolicy4.setHeightForWidth(self.erasepartitionList.sizePolicy().hasHeightForWidth())
        self.erasepartitionList.setSizePolicy(sizePolicy4)
        self.erasepartitionList.setMinimumSize(QSize(0, 280))
        font3 = QFont()
        font3.setPointSize(10)
        self.erasepartitionList.setFont(font3)
        self.erasepartitionList.setStyleSheet(u"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #63676d;\n"
"    height: 18px;\n"
"    margin: 0px 18px 0 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
""
                        "    image: url(://arrow-left.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #63676d;\n"
"    width: 18px;\n"
"    margin: 18px 0 18px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScro"
                        "llBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: rgb(61, 69, 84);\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: rgb(72, 76, 88);\n"
"    border: 2px solid rgb(163, 167, 178);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: 1px solid #323232;\n"
"	border-radius: 7px;\n"
"	b"
                        "ackground-color: rgb(255, 201, 38);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 2px solid rgb(255, 201, 38);\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"")
        self.erasepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.erasepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.erasepartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.erasepartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 639, 308))
        self.erasepartitionList.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_16.addWidget(self.erasepartitionList)

        self.verticalSpacer_19 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_19)

        self.erasepartitionsbtn = QPushButton(self.erasetab)
        self.erasepartitionsbtn.setObjectName(u"erasepartitionsbtn")
        self.erasepartitionsbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.erasepartitionsbtn)


        self.horizontalLayout_11.addLayout(self.verticalLayout_16)

        self.tabWidget.addTab(self.erasetab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_18 = QVBoxLayout(self.tab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.readflashbtn = QPushButton(self.tab)
        self.readflashbtn.setObjectName(u"readflashbtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.readflashbtn.sizePolicy().hasHeightForWidth())
        self.readflashbtn.setSizePolicy(sizePolicy8)
        self.readflashbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.readflashbtn)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.readpreloaderbtn = QPushButton(self.tab)
        self.readpreloaderbtn.setObjectName(u"readpreloaderbtn")
        sizePolicy8.setHeightForWidth(self.readpreloaderbtn.sizePolicy().hasHeightForWidth())
        self.readpreloaderbtn.setSizePolicy(sizePolicy8)
        self.readpreloaderbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.readpreloaderbtn)

        self.verticalSpacer_3 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.readboot2btn = QPushButton(self.tab)
        self.readboot2btn.setObjectName(u"readboot2btn")
        sizePolicy8.setHeightForWidth(self.readboot2btn.sizePolicy().hasHeightForWidth())
        self.readboot2btn.setSizePolicy(sizePolicy8)
        self.readboot2btn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.readboot2btn)

        self.verticalSpacer_11 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_11)

        self.readrpmbbtn = QPushButton(self.tab)
        self.readrpmbbtn.setObjectName(u"readrpmbbtn")
        sizePolicy8.setHeightForWidth(self.readrpmbbtn.sizePolicy().hasHeightForWidth())
        self.readrpmbbtn.setSizePolicy(sizePolicy8)
        self.readrpmbbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.readrpmbbtn)


        self.horizontalLayout_13.addLayout(self.verticalLayout_5)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(15, 0))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.writeflashbtn = QPushButton(self.tab)
        self.writeflashbtn.setObjectName(u"writeflashbtn")
        sizePolicy8.setHeightForWidth(self.writeflashbtn.sizePolicy().hasHeightForWidth())
        self.writeflashbtn.setSizePolicy(sizePolicy8)
        self.writeflashbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.writeflashbtn)

        self.verticalSpacer_12 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_12)

        self.writepreloaderbtn = QPushButton(self.tab)
        self.writepreloaderbtn.setObjectName(u"writepreloaderbtn")
        sizePolicy8.setHeightForWidth(self.writepreloaderbtn.sizePolicy().hasHeightForWidth())
        self.writepreloaderbtn.setSizePolicy(sizePolicy8)
        self.writepreloaderbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.writepreloaderbtn)

        self.verticalSpacer_13 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_13)

        self.writeboot2btn = QPushButton(self.tab)
        self.writeboot2btn.setObjectName(u"writeboot2btn")
        sizePolicy8.setHeightForWidth(self.writeboot2btn.sizePolicy().hasHeightForWidth())
        self.writeboot2btn.setSizePolicy(sizePolicy8)
        self.writeboot2btn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.writeboot2btn)

        self.verticalSpacer_14 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)

        self.writerpmbbtn = QPushButton(self.tab)
        self.writerpmbbtn.setObjectName(u"writerpmbbtn")
        sizePolicy8.setHeightForWidth(self.writerpmbbtn.sizePolicy().hasHeightForWidth())
        self.writerpmbbtn.setSizePolicy(sizePolicy8)
        self.writerpmbbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.writerpmbbtn)


        self.horizontalLayout_13.addLayout(self.verticalLayout_3)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(15, 0))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.erasepreloaderbtn = QPushButton(self.tab)
        self.erasepreloaderbtn.setObjectName(u"erasepreloaderbtn")
        sizePolicy8.setHeightForWidth(self.erasepreloaderbtn.sizePolicy().hasHeightForWidth())
        self.erasepreloaderbtn.setSizePolicy(sizePolicy8)
        self.erasepreloaderbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.erasepreloaderbtn)

        self.verticalSpacer_15 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_15)

        self.eraseboot2btn = QPushButton(self.tab)
        self.eraseboot2btn.setObjectName(u"eraseboot2btn")
        sizePolicy8.setHeightForWidth(self.eraseboot2btn.sizePolicy().hasHeightForWidth())
        self.eraseboot2btn.setSizePolicy(sizePolicy8)
        self.eraseboot2btn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.eraseboot2btn)

        self.verticalSpacer_16 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_16)

        self.eraserpmbbtn = QPushButton(self.tab)
        self.eraserpmbbtn.setObjectName(u"eraserpmbbtn")
        sizePolicy8.setHeightForWidth(self.eraserpmbbtn.sizePolicy().hasHeightForWidth())
        self.eraserpmbbtn.setSizePolicy(sizePolicy8)
        self.eraserpmbbtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.eraserpmbbtn)


        self.horizontalLayout_13.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_15 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.verticalLayout_18.addLayout(self.horizontalLayout_13)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_16 = QSpacerItem(6, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 1px;")

        self.horizontalLayout_15.addWidget(self.label_5)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.lockbutton = QPushButton(self.tab)
        self.lockbutton.setObjectName(u"lockbutton")
        sizePolicy8.setHeightForWidth(self.lockbutton.sizePolicy().hasHeightForWidth())
        self.lockbutton.setSizePolicy(sizePolicy8)
        self.lockbutton.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 8px;\n"
"	font-size:14px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.lockbutton)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.unlockbutton = QPushButton(self.tab)
        self.unlockbutton.setObjectName(u"unlockbutton")
        sizePolicy8.setHeightForWidth(self.unlockbutton.sizePolicy().hasHeightForWidth())
        self.unlockbutton.setSizePolicy(sizePolicy8)
        self.unlockbutton.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 8px;\n"
"	font-size:14px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.unlockbutton)

        self.horizontalSpacer_12 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.verticalLayout_18.addLayout(self.verticalLayout_2)

        self.verticalSpacer_21 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_21)

        self.tabWidget.addTab(self.tab, "")
        self.keytab = QWidget()
        self.keytab.setObjectName(u"keytab")
        self.gridLayout_2 = QGridLayout(self.keytab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.keytable = QTableWidget(self.keytab)
        if (self.keytable.columnCount() < 2):
            self.keytable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.keytable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.keytable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.keytable.rowCount() < 7):
            self.keytable.setRowCount(7)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.keytable.setVerticalHeaderItem(6, __qtablewidgetitem8)
        self.keytable.setObjectName(u"keytable")
        self.keytable.setEnabled(True)
        self.keytable.setStyleSheet(u"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: rgb(61, 69, 84);\n"
"    border: 1px groove #333333;\n"
"    color: #f0f0f0;\n"
"	font-weight: bold;\n"
"    gridline-color: #333333;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #484c58;\n"
"    color: #f0f0f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #484c58;\n"
"    border: 2px groove rgb(255, 201, 38);\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #282830;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
""
                        "    background-color: #282830;\n"
"    color: #fff;\n"
"	font-weight: bold;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: rgb(255, 201, 38);\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 0px;\n"
"\n"
"}\n"
"\n"
"")
        self.keytable.setSortingEnabled(True)
        self.keytable.setWordWrap(False)
        self.keytable.horizontalHeader().setProperty("showSortIndicator", True)
        self.keytable.horizontalHeader().setStretchLastSection(True)
        self.keytable.verticalHeader().setVisible(False)
        self.keytable.verticalHeader().setCascadingSectionResizes(False)
        self.keytable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.keytable, 1, 0, 1, 1)

        self.keystatuslabel = QLabel(self.keytab)
        self.keystatuslabel.setObjectName(u"keystatuslabel")

        self.gridLayout_2.addWidget(self.keystatuslabel, 2, 0, 1, 1)

        self.generatekeybtn = QPushButton(self.keytab)
        self.generatekeybtn.setObjectName(u"generatekeybtn")
        self.generatekeybtn.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 6px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.generatekeybtn, 3, 0, 1, 1)

        self.tabWidget.addTab(self.keytab, "")
        self.debugtab = QWidget()
        self.debugtab.setObjectName(u"debugtab")
        self.gridLayout_3 = QGridLayout(self.debugtab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.debugtab)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.logBox = QPlainTextEdit(self.debugtab)
        self.logBox.setObjectName(u"logBox")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.logBox.sizePolicy().hasHeightForWidth())
        self.logBox.setSizePolicy(sizePolicy9)
        self.logBox.setMinimumSize(QSize(722, 0))
        self.logBox.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	background-color: rgb(61, 69, 84);\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #63676d;\n"
"    height: 18px;\n"
"    margin: 0px 18px 0 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-"
                        "right.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #63676d;\n"
"    width: 18px;\n"
"    margin: 18px 0 18px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;"
                        "\n"
"    height: 18px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.logBox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.logBox.setReadOnly(True)
        self.logBox.setProperty("hidden", False)

        self.gridLayout.addWidget(self.logBox, 0, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.debugtab, "")

        self.Main.addWidget(self.tabWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.Main.addItem(self.verticalSpacer_4)

        self.partProgressText = QLabel(self.centralwidget)
        self.partProgressText.setObjectName(u"partProgressText")
        self.partProgressText.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"")

        self.Main.addWidget(self.partProgressText)

        self.partProgress = QProgressBar(self.centralwidget)
        self.partProgress.setObjectName(u"partProgress")
        self.partProgress.setStyleSheet(u"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"	color: rgb(255, 175, 2);\n"
"	font-weight: bold;\n"
"	border-radius: 6px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color:  qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"border: 0px;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"QProgressBar:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"	border: 1px solid #000;\n"
"	border-radius: 6px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"	background-color: #333;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	color: #656565;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.partProgress.setValue(0)

        self.Main.addWidget(self.partProgress)

        self.fullProgressText = QLabel(self.centralwidget)
        self.fullProgressText.setObjectName(u"fullProgressText")
        self.fullProgressText.setStyleSheet(u"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"")

        self.Main.addWidget(self.fullProgressText)

        self.fullProgress = QProgressBar(self.centralwidget)
        self.fullProgress.setObjectName(u"fullProgress")
        self.fullProgress.setStyleSheet(u"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"	color: rgb(255, 175, 2);\n"
"	font-weight: bold;\n"
"	border-radius: 6px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color:  qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"border: 0px;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"QProgressBar:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"	border: 1px solid #000;\n"
"	border-radius: 6px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"	background-color: #333;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	color: #656565;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.fullProgress.setValue(0)

        self.Main.addWidget(self.fullProgress)


        self.verticalLayout_19.addLayout(self.Main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.line_2.raise_()
        self.connectInfo.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 902, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_Quit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MTKClient v2.0", None))
        self.actionRead_partition_s.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionRead_full_flash.setText(QCoreApplication.translate("MainWindow", u"Read full flash", None))
        self.actionRead_offset.setText(QCoreApplication.translate("MainWindow", u"Read at offset", None))
        self.actionWrite_partition_s.setText(QCoreApplication.translate("MainWindow", u"Write partition(s)", None))
        self.actionWrite_full_flash.setText(QCoreApplication.translate("MainWindow", u"Write full flash", None))
        self.actionWrite_at_offset.setText(QCoreApplication.translate("MainWindow", u"Write at offset", None))
        self.actionErase_partitions_s.setText(QCoreApplication.translate("MainWindow", u"Erase partitions(s)", None))
        self.actionErase_at_offset.setText(QCoreApplication.translate("MainWindow", u"Erase at offset", None))
        self.actionRead_RPMB.setText(QCoreApplication.translate("MainWindow", u"Read RPMB", None))
        self.actionWrite_RPMB.setText(QCoreApplication.translate("MainWindow", u"Write RPMB", None))
        self.actionRead_preloader.setText(QCoreApplication.translate("MainWindow", u"Read preloader", None))
        self.actionGenerate_RPMB_keys.setText(QCoreApplication.translate("MainWindow", u"Generate RPMB keys", None))
        self.actionRead_boot2.setText(QCoreApplication.translate("MainWindow", u"Read boot2", None))
        self.actionWrite_preloader.setText(QCoreApplication.translate("MainWindow", u"Write preloader", None))
        self.actionWrite_boot2.setText(QCoreApplication.translate("MainWindow", u"Write boot2", None))
        self.actionUnlock_device.setText(QCoreApplication.translate("MainWindow", u"Unlock / Lock", None))
        self.actionLock_device.setText(QCoreApplication.translate("MainWindow", u"Lock device", None))
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.logoPic.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"MTKClient v2.0", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#d5d5d5;\">SPEED MODE</span></p></body></html>", None))
        self.copyrightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffaf02;\">Moded By: Balveer Jat</span><br/>Made by: Bjoern Kerler<br/>Gui by: Geert-Jan Kreileman</p></body></html>", None))
        self.phoneDebugInfoTextbox.setText("")
        self.pic.setText("")
        self.spinner_pic.setText("")
        self.phoneInfoTextbox.setText(QCoreApplication.translate("MainWindow", u"No phone detected.", None))
        self.initStepsImage.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Step 1:</span></p><p>Power off the phone</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Step 2:</span></p><p>Connect the USB cable, hold both volume buttons if needed</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>No connection? Try shorting the test point to ground</p></body></html>", None))
        self.showdebugbtn.setText(QCoreApplication.translate("MainWindow", u"Show Debug Log", None))
        self.readtitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Select partitions to read</span></p></body></html>", None))
        self.readselectallcheckbox.setText(QCoreApplication.translate("MainWindow", u"Select all partitions", None))
        self.readDumpGPTCheckbox.setText(QCoreApplication.translate("MainWindow", u"Dump GPT", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" \">It takes a lot of time to<br/>read oversized userdata</span></p></body></html>", None))
        self.readpartitionsbtn.setText(QCoreApplication.translate("MainWindow", u"Read partition(s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.readtab), QCoreApplication.translate("MainWindow", u"Read partition(s)", None))
        self.writetitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Select partitions to write</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1. Select Out folder to <br/>flash firmware.</p><p>2. after flashing firmware <br/>erase userdata.</p></body></html>", None))
        self.writeselectfromdir.setText(QCoreApplication.translate("MainWindow", u"Select from directory", None))
        self.writepartbtn.setText(QCoreApplication.translate("MainWindow", u"Write partition(s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.writetab), QCoreApplication.translate("MainWindow", u"Write partition(s)", None))
        self.erasetitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Select partitions to erase</span></p></body></html>", None))
        self.eraseselectallpartitionscheckbox.setText(QCoreApplication.translate("MainWindow", u"Select all partitions", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1. Backup before erasing a partition<br/>2. Don't erase a partition you<br/>dont know about</p></body></html>", None))
        self.erasepartitionsbtn.setText(QCoreApplication.translate("MainWindow", u"Erase partition(s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.erasetab), QCoreApplication.translate("MainWindow", u"Erase partition(s)", None))
        self.readflashbtn.setText(QCoreApplication.translate("MainWindow", u"Read flash", None))
        self.readpreloaderbtn.setText(QCoreApplication.translate("MainWindow", u"Read preloader", None))
        self.readboot2btn.setText(QCoreApplication.translate("MainWindow", u"Read boot2", None))
        self.readrpmbbtn.setText(QCoreApplication.translate("MainWindow", u"Read RPMB", None))
        self.writeflashbtn.setText(QCoreApplication.translate("MainWindow", u"Write flash", None))
        self.writepreloaderbtn.setText(QCoreApplication.translate("MainWindow", u"Write preloader", None))
        self.writeboot2btn.setText(QCoreApplication.translate("MainWindow", u"Write boot2", None))
        self.writerpmbbtn.setText(QCoreApplication.translate("MainWindow", u"Write RPMB", None))
        self.erasepreloaderbtn.setText(QCoreApplication.translate("MainWindow", u"Erase preloader", None))
        self.eraseboot2btn.setText(QCoreApplication.translate("MainWindow", u"Erase boot2", None))
        self.eraserpmbbtn.setText(QCoreApplication.translate("MainWindow", u"Erase RPMB", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; color:#ffffff; background-color:transparent;\">Before Unlocking and Locking the Bootloader :</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; color:#ffffff; background-color:transparent;\"> Erase </span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; font-weight:700; color:#ffffff; background-color:transparent;\">metadata</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; color:#ffffff; background-color:transparent;\"> and </span><span style=\" font-family:'-apple-system','BlinkMacSyste"
                        "mFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; font-weight:700; color:#ffffff; background-color:transparent;\">userdata</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; color:#ffffff; background-color:transparent;\"> (and </span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; font-weight:700; color:#ffffff; background-color:transparent;\">md_udc</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Helvetica','Arial','sans-serif','Apple Color Emoji','Segoe UI Emoji'; font-size:13px; color:#ffffff; background-color:transparent;\"> if existing):</span></p></body></html>", None))
        self.lockbutton.setText(QCoreApplication.translate("MainWindow", u"Lock bootloader", None))
        self.unlockbutton.setText(QCoreApplication.translate("MainWindow", u"Unlock bootloader", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Flash Tools", None))
        ___qtablewidgetitem = self.keytable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem1 = self.keytable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem2 = self.keytable.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem3 = self.keytable.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem4 = self.keytable.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem5 = self.keytable.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem6 = self.keytable.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem7 = self.keytable.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        ___qtablewidgetitem8 = self.keytable.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Neue Zeile", None));
        self.keystatuslabel.setText(QCoreApplication.translate("MainWindow", u"Ready.", None))
        self.generatekeybtn.setText(QCoreApplication.translate("MainWindow", u"Generate Keys", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.keytab), QCoreApplication.translate("MainWindow", u"Keys", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debugtab), QCoreApplication.translate("MainWindow", u"Debug Log", None))
        self.partProgressText.setText("")
        self.fullProgressText.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

