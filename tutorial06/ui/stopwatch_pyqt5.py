# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopwatch.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 186)
        Dialog.setMinimumSize(QtCore.QSize(434, 186))
        Dialog.setMaximumSize(QtCore.QSize(434, 186))
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.countText = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.countText.setFont(font)
        self.countText.setStyleSheet("color: rgb(85, 170, 255);")
        self.countText.setAlignment(QtCore.Qt.AlignCenter)
        self.countText.setObjectName("countText")
        self.verticalLayout.addWidget(self.countText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startBtn = QtWidgets.QPushButton(Dialog)
        self.startBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.startBtn.setStyleSheet("background-color: #7e7e7e;\n"
"color: rgb(255, 255, 255);")
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.stopBtn = QtWidgets.QPushButton(Dialog)
        self.stopBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.stopBtn.setStyleSheet("background-color: #7e7e7e;\n"
"color: rgb(255, 255, 255);")
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout.addWidget(self.stopBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stop Watch"))
        self.countText.setText(_translate("Dialog", "0.00.00.0"))
        self.startBtn.setText(_translate("Dialog", "Start"))
        self.stopBtn.setText(_translate("Dialog", "Stop"))
