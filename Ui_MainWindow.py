# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 600)
        MainWindow.setMinimumSize(QtCore.QSize(960, 600))
        MainWindow.setMaximumSize(QtCore.QSize(960, 600))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_Main = QtWidgets.QFrame(self.centralwidget)
        self.frame_Main.setStyleSheet("QFrame {\n"
"    background: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0.75, y1:0.25, x2:0.25, y2:0.75, \n"
"        stop:0 rgba(255, 244, 236, 255), \n"
"        stop:1 rgba(248, 231, 210, 255)\n"
"    );\n"
"    border:none;\n"
"    border-radius:20px;\n"
"}")
        self.frame_Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Main.setObjectName("frame_Main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_Main)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(12, -1, 12, -1)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_head_title = QtWidgets.QLabel(self.frame_Main)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_head_title.setFont(font)
        self.label_head_title.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: rgb(10, 10, 10);\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.label_head_title.setObjectName("label_head_title")
        self.horizontalLayout_10.addWidget(self.label_head_title)
        self.label_identify = QtWidgets.QLabel(self.frame_Main)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_identify.setFont(font)
        self.label_identify.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: rgb(10, 10, 10);\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.label_identify.setAlignment(QtCore.Qt.AlignCenter)
        self.label_identify.setObjectName("label_identify")
        self.horizontalLayout_10.addWidget(self.label_identify)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.pushButton_exchange = QtWidgets.QPushButton(self.frame_Main)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_exchange.setFont(font)
        self.pushButton_exchange.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exchange.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(123, 123, 123);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(32, 32, 32);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/img/ui/兑换激活码.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exchange.setIcon(icon)
        self.pushButton_exchange.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_exchange.setObjectName("pushButton_exchange")
        self.horizontalLayout_10.addWidget(self.pushButton_exchange)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_Main)
        self.pushButton_close.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButton_close.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_close.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(254, 81, 111, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(254, 81, 111, 75);\n"
"}")
        self.pushButton_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/img/ui/窗口控制-关闭.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon1)
        self.pushButton_close.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_10.addWidget(self.pushButton_close)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalFrame = QtWidgets.QFrame(self.frame_Main)
        self.verticalFrame.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:12px;\n"
"}")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(12, 6, 9, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_privilege = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_privilege.setFont(font)
        self.label_privilege.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: rgb(254, 81, 111);\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.label_privilege.setObjectName("label_privilege")
        self.horizontalLayout_3.addWidget(self.label_privilege)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_privilege = QtWidgets.QPushButton(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_privilege.setFont(font)
        self.pushButton_privilege.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_privilege.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(123, 123, 123);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(32, 32, 32);\n"
"}")
        self.pushButton_privilege.setObjectName("pushButton_privilege")
        self.horizontalLayout_3.addWidget(self.pushButton_privilege)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.frame_select_version = QtWidgets.QFrame(self.verticalFrame)
        self.frame_select_version.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px solid red;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"}")
        self.frame_select_version.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_select_version.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_select_version.setObjectName("frame_select_version")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_select_version)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_A = QtWidgets.QPushButton(self.frame_select_version)
        self.pushButton_A.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_A.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_A.setStyleSheet("QPushButton {\n"
"    margin-right: 3px;\n"
"    margin-bottom: 0px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgba(120, 120, 120, 60);\n"
"    border-radius: 8px;\n"
"    background: none;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(254, 81, 111, 120);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.2s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(254, 81, 111, 255);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.1s ease-in-out;\n"
"}")
        self.pushButton_A.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/img/Prices/A.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_A.setIcon(icon2)
        self.pushButton_A.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_A.setObjectName("pushButton_A")
        self.horizontalLayout_6.addWidget(self.pushButton_A)
        self.pushButton_B = QtWidgets.QPushButton(self.frame_select_version)
        self.pushButton_B.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_B.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_B.setStyleSheet("QPushButton {\n"
"    margin-right: 3px;\n"
"    margin-bottom: 0px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgba(120, 120, 120, 60);\n"
"    border-radius: 8px;\n"
"    background: none;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(254, 81, 111, 120);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.2s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(254, 81, 111, 255);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.1s ease-in-out;\n"
"}")
        self.pushButton_B.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/img/Prices/B.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_B.setIcon(icon3)
        self.pushButton_B.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_B.setObjectName("pushButton_B")
        self.horizontalLayout_6.addWidget(self.pushButton_B)
        self.pushButton_C = QtWidgets.QPushButton(self.frame_select_version)
        self.pushButton_C.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_C.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_C.setStyleSheet("QPushButton {\n"
"    margin-right: 3px;\n"
"    margin-bottom: 0px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgba(120, 120, 120, 60);\n"
"    border-radius: 8px;\n"
"    background: none;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(254, 81, 111, 120);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.2s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(254, 81, 111, 255);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.1s ease-in-out;\n"
"}")
        self.pushButton_C.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/img/Prices/C.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_C.setIcon(icon4)
        self.pushButton_C.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_C.setObjectName("pushButton_C")
        self.horizontalLayout_6.addWidget(self.pushButton_C)
        self.pushButton_D = QtWidgets.QPushButton(self.frame_select_version)
        self.pushButton_D.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_D.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_D.setStyleSheet("QPushButton {\n"
"    margin-right: 3px;\n"
"    margin-bottom: 0px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgba(120, 120, 120, 60);\n"
"    border-radius: 8px;\n"
"    background: none;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(254, 81, 111, 120);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.2s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(254, 81, 111, 255);\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0.5, y1:1, x2:0.5, y2:0,\n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:1 rgba(255, 153, 170, 88)\n"
"    );\n"
"    transition: background 0.1s ease-in-out;\n"
"}")
        self.pushButton_D.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/img/Prices/D.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_D.setIcon(icon5)
        self.pushButton_D.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_D.setObjectName("pushButton_D")
        self.horizontalLayout_6.addWidget(self.pushButton_D)
        self.verticalLayout_2.addWidget(self.frame_select_version)
        self.Frame_mid = QtWidgets.QFrame(self.verticalFrame)
        self.Frame_mid.setStyleSheet("background:rgb(254, 246, 241);\n"
"border: 1px solid rgba(213, 202, 188, 180);\n"
"border-radius:4px;")
        self.Frame_mid.setObjectName("Frame_mid")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Frame_mid)
        self.horizontalLayout_8.setContentsMargins(12, 2, 0, 2)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.Frame_mid)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;\n"
"color: rgb(135, 135, 135);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.label_prices = QtWidgets.QLabel(self.Frame_mid)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_prices.setFont(font)
        self.label_prices.setStyleSheet("color:rgb(255, 85, 0);\n"
"border:none;")
        self.label_prices.setObjectName("label_prices")
        self.horizontalLayout_8.addWidget(self.label_prices)
        self.label_Yuan = QtWidgets.QLabel(self.Frame_mid)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_Yuan.setFont(font)
        self.label_Yuan.setStyleSheet("border:none;\n"
"color: rgb(135, 135, 135);")
        self.label_Yuan.setObjectName("label_Yuan")
        self.horizontalLayout_8.addWidget(self.label_Yuan)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.Frame_mid)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalFrame1 = QtWidgets.QFrame(self.verticalFrame)
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_head = QtWidgets.QWidget(self.verticalFrame1)
        self.widget_head.setMinimumSize(QtCore.QSize(650, 100))
        self.widget_head.setMaximumSize(QtCore.QSize(650, 16777215))
        self.widget_head.setStyleSheet("QWidget {\n"
"border-radius: 0px;\n"
"image: url(\'resources/img/ui/head.png\');\n"
"background: transparent;\n"
"}")
        self.widget_head.setObjectName("widget_head")
        self.horizontalLayout_9.addWidget(self.widget_head)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.Code_redemption = QtWidgets.QFrame(self.verticalFrame1)
        self.Code_redemption.setObjectName("Code_redemption")
        self.Code_redemption_2 = QtWidgets.QHBoxLayout(self.Code_redemption)
        self.Code_redemption_2.setContentsMargins(56, -1, 56, -1)
        self.Code_redemption_2.setSpacing(12)
        self.Code_redemption_2.setObjectName("Code_redemption_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Code_redemption_2.addItem(spacerItem3)
        self.label_7 = QtWidgets.QLabel(self.Code_redemption)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.Code_redemption_2.addWidget(self.label_7)
        self.lineEdit_code = QtWidgets.QLineEdit(self.Code_redemption)
        self.lineEdit_code.setMinimumSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_code.setFont(font)
        self.lineEdit_code.setStyleSheet("color:rgb(0, 0, 0);\n"
"background:rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"border: 1px solid rgba(120, 120, 120, 150);")
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.Code_redemption_2.addWidget(self.lineEdit_code)
        self.pushButton_OK = QtWidgets.QPushButton(self.Code_redemption)
        self.pushButton_OK.setMinimumSize(QtCore.QSize(86, 34))
        self.pushButton_OK.setMaximumSize(QtCore.QSize(86, 34))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_OK.setFont(font)
        self.pushButton_OK.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_OK.setStyleSheet("QPushButton {\n"
"    background: rgb(215, 184, 121);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 4px;\n"
"    transition: background 0.3s, transform 0.2s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(235, 204, 141);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgb(195, 164, 101);\n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.Code_redemption_2.addWidget(self.pushButton_OK)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Code_redemption_2.addItem(spacerItem4)
        self.Code_redemption_2.setStretch(2, 1)
        self.verticalLayout_6.addWidget(self.Code_redemption)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_4.addWidget(self.verticalFrame1)
        self.widget_bottom = QtWidgets.QWidget(self.verticalFrame)
        self.widget_bottom.setMinimumSize(QtCore.QSize(683, 78))
        self.widget_bottom.setMaximumSize(QtCore.QSize(683, 16777215))
        self.widget_bottom.setStyleSheet("QWidget {\n"
"    border-radius: 12px;\n"
"image: url(\'resources/img/ui/bottom.png\');\n"
"background: transparent;\n"
"}")
        self.widget_bottom.setObjectName("widget_bottom")
        self.verticalLayout_4.addWidget(self.widget_bottom)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.Frame_Right = QtWidgets.QFrame(self.frame_Main)
        self.Frame_Right.setStyleSheet("QFrame {\n"
"    background: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0.75, y1:0.25, x2:0.25, y2:0.75, \n"
"        stop:0 rgba(255, 251, 250, 255), \n"
"        stop:1 rgba(255, 252, 247, 255)\n"
"    );\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}")
        self.Frame_Right.setObjectName("Frame_Right")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Frame_Right)
        self.verticalLayout_5.setContentsMargins(0, 88, 0, 12)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.Frame_Right)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 85, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_prices_2 = QtWidgets.QLabel(self.Frame_Right)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_prices_2.setFont(font)
        self.label_prices_2.setStyleSheet("color:rgb(255, 85, 0);")
        self.label_prices_2.setObjectName("label_prices_2")
        self.horizontalLayout_2.addWidget(self.label_prices_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.pushButton_Wechat = QtWidgets.QPushButton(self.Frame_Right)
        self.pushButton_Wechat.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_Wechat.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_Wechat.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgba(120, 120, 120, 60);\n"
"    border-radius:12px;\n"
"}")
        self.pushButton_Wechat.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/img/wp/wp99.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Wechat.setIcon(icon6)
        self.pushButton_Wechat.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_Wechat.setObjectName("pushButton_Wechat")
        self.horizontalLayout_4.addWidget(self.pushButton_Wechat)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.label_3 = QtWidgets.QLabel(self.Frame_Right)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: rgb(0, 186, 0);\n"
"    background: rgba(0, 0, 0, 0);\n"
"    qproperty-alignment: \'AlignHCenter | AlignVCenter\';\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_check = QtWidgets.QPushButton(self.Frame_Right)
        self.pushButton_check.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_check.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_check.setFont(font)
        self.pushButton_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_check.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 rgb(128, 94, 62), \n"
"                                      stop:1 rgb(128, 94, 162));\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 4px;\n"
"    transition: background 0.3s, transform 0.2s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 rgb(178, 144, 122),\n"
"                                      stop:1 rgb(178, 144, 212));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 rgb(98, 74, 42), \n"
"                                      stop:1 rgb(98, 74, 142)); \n"
"    transform: translateY(2px);\n"
"}")
        self.pushButton_check.setObjectName("pushButton_check")
        self.horizontalLayout_7.addWidget(self.pushButton_check)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.pushButton_feedback = QtWidgets.QPushButton(self.Frame_Right)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_feedback.setFont(font)
        self.pushButton_feedback.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_feedback.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(123, 123, 123);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: rgb(32, 32, 32);\n"
"}")
        self.pushButton_feedback.setObjectName("pushButton_feedback")
        self.verticalLayout_5.addWidget(self.pushButton_feedback)
        self.horizontalLayout.addWidget(self.Frame_Right)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout.addWidget(self.frame_Main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_head_title.setText(_translate("MainWindow", "WinQSB安装程序即将继续："))
        self.label_identify.setText(_translate("MainWindow", "123456"))
        self.pushButton_exchange.setText(_translate("MainWindow", "安装码领取"))
        self.label_privilege.setText(_translate("MainWindow", "原版WinQSB内核，支持Win10/Win11无需虚拟机"))
        self.pushButton_privilege.setText(_translate("MainWindow", "查看安装教程 >"))
        self.label_5.setText(_translate("MainWindow", "支付金额："))
        self.label_prices.setText(_translate("MainWindow", "99.00"))
        self.label_Yuan.setText(_translate("MainWindow", "元"))
        self.label_7.setText(_translate("MainWindow", "安装秘钥："))
        self.lineEdit_code.setPlaceholderText(_translate("MainWindow", "请在此输入安装秘钥"))
        self.pushButton_OK.setText(_translate("MainWindow", "安装"))
        self.label_2.setText(_translate("MainWindow", "￥"))
        self.label_prices_2.setText(_translate("MainWindow", "99"))
        self.label_3.setText(_translate("MainWindow", "仅支持微信扫码支付"))
        self.pushButton_check.setText(_translate("MainWindow", "我已支付"))
        self.pushButton_feedback.setText(_translate("MainWindow", "问题反馈 >"))
