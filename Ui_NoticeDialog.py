# Form implementation generated from reading ui file 'Ui_NoticeDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NoticeDialog(object):
    def setupUi(self, NoticeDialog):
        NoticeDialog.setObjectName("NoticeDialog")
        NoticeDialog.resize(488, 288)
        self.verticalLayout = QtWidgets.QVBoxLayout(NoticeDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=NoticeDialog)
        self.frame.setMinimumSize(QtCore.QSize(488, 288))
        self.frame.setStyleSheet("QFrame#frame{\n"
"background-color: rgb(245, 249, 254);\n"
"border-radius:25px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_3 = QtWidgets.QWidget(parent=self.frame)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setStyleSheet(".QWidget{\n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                  stop:0 rgb(105, 27, 253), \n"
"                                  stop:1 rgb(200, 160, 240));\n"
"border-radius:16px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setContentsMargins(18, 18, 18, 18)
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_title = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgba(222, 255, 255, 255)")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_5.addWidget(self.label_title)
        self.label_content = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_content.setFont(font)
        self.label_content.setStyleSheet("font-size: 22px;\n"
"color: rgb(250, 250, 250)")
        self.label_content.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_content.setObjectName("label_content")
        self.verticalLayout_5.addWidget(self.label_content)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(88, 34))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(88, 34))
        self.pushButton_cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_cancel.setStyleSheet("QPushButton {\n"
"    background-color: rgba(105, 27, 253, 180);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-family: \'Microsoft YaHei\';\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(105, 27, 253, 120);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(105, 27, 253, 250);\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 4)
        self.verticalLayout_5.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.setStretch(0, 5)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.verticalLayout_6.setStretch(0, 9)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_7.setStretch(0, 4)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(NoticeDialog)
        QtCore.QMetaObject.connectSlotsByName(NoticeDialog)

    def retranslateUi(self, NoticeDialog):
        _translate = QtCore.QCoreApplication.translate
        NoticeDialog.setWindowTitle(_translate("NoticeDialog", "Dialog"))
        self.label_title.setText(_translate("NoticeDialog", "Dialog Title"))
        self.label_content.setText(_translate("NoticeDialog", "Dialog content"))
        self.pushButton_cancel.setText(_translate("NoticeDialog", "我知道了"))
