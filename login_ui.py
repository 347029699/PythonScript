# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(530, 298)
        font = QtGui.QFont()
        font.setPointSize(18)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 10, 519, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.passwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.passwd.setFont(font)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.gridLayout.addWidget(self.passwd, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Medium")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Medium")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.filePath = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.filePath.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filePath.setFont(font)
        self.filePath.setObjectName("filePath")
        self.gridLayout.addWidget(self.filePath, 2, 1, 2, 1)
        self.userName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.userName.setFont(font)
        self.userName.setObjectName("userName")
        self.gridLayout.addWidget(self.userName, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.selectFile = QtWidgets.QToolButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.selectFile.setFont(font)
        self.selectFile.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.selectFile.setAutoRaise(False)
        self.selectFile.setObjectName("selectFile")
        self.gridLayout.addWidget(self.selectFile, 2, 2, 1, 1)
        self.clearFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearFile.setFont(font)
        self.clearFile.setObjectName("clearFile")
        self.gridLayout.addWidget(self.clearFile, 3, 2, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 8, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton3.setFont(font)
        self.radioButton3.setObjectName("radioButton3")
        self.horizontalLayout.addWidget(self.radioButton3)
        self.radioButton2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout.addWidget(self.radioButton2)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.radioButton4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton4.setFont(font)
        self.radioButton4.setObjectName("radioButton4")
        self.gridLayout.addWidget(self.radioButton4, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN Medium")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setMidLineWidth(0)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "交易系统录入程序Design by Demon"))  # title
        Dialog.setWindowIcon(QIcon('tool.ico'))  # icon
        self.label_3.setText(_translate("Dialog", "选择文件："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.label.setText(_translate("Dialog", "用户名："))
        self.selectFile.setText(_translate("Dialog", "..."))
        self.clearFile.setText(_translate("Dialog", "清空路径"))
        self.startButton.setText(_translate("Dialog", "开始"))
        self.radioButton.setText(_translate("Dialog", "转让单资产"))
        self.radioButton3.setText(_translate("Dialog", "转让资产包"))
        self.radioButton2.setText(_translate("Dialog", "出租单租赁"))
        self.radioButton4.setText(_translate("Dialog", "出租租赁包"))
        self.label_4.setText(_translate("Dialog", "录入类型："))
