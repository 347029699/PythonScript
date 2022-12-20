# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 313)
        font = QtGui.QFont()
        font.setPointSize(18)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 20, 481, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.clearFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearFile.setFont(font)
        self.clearFile.setObjectName("clearFile")
        self.gridLayout.addWidget(self.clearFile, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN Medium")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.passwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.gridLayout.addWidget(self.passwd, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN Medium")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 5, 1, 1, 1)
        self.userName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userName.setObjectName("userName")
        self.gridLayout.addWidget(self.userName, 0, 1, 1, 1)
        self.filePath = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.filePath.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filePath.setFont(font)
        self.filePath.setObjectName("filePath")
        self.gridLayout.addWidget(self.filePath, 2, 1, 2, 1)
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
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN Medium")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.clearFile.setText(_translate("Dialog", "清空路径"))
        self.label_3.setText(_translate("Dialog", "选择文件："))
        self.label.setText(_translate("Dialog", "用户名："))
        self.startButton.setText(_translate("Dialog", "开始"))
        self.selectFile.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "密码："))
