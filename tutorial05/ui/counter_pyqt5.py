# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'counter.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 300)
        Dialog.setMinimumSize(QtCore.QSize(260, 300))
        Dialog.setMaximumSize(QtCore.QSize(260, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.countText = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.countText.setFont(font)
        self.countText.setAlignment(QtCore.Qt.AlignCenter)
        self.countText.setObjectName("countText")
        self.verticalLayout.addWidget(self.countText)
        self.increaseBtn = QtWidgets.QPushButton(Dialog)
        self.increaseBtn.setObjectName("increaseBtn")
        self.verticalLayout.addWidget(self.increaseBtn)
        self.decreaseBtn = QtWidgets.QPushButton(Dialog)
        self.decreaseBtn.setObjectName("decreaseBtn")
        self.verticalLayout.addWidget(self.decreaseBtn)
        self.resetBtn = QtWidgets.QPushButton(Dialog)
        self.resetBtn.setObjectName("resetBtn")
        self.verticalLayout.addWidget(self.resetBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Counter"))
        self.countText.setText(_translate("Dialog", "0"))
        self.increaseBtn.setText(_translate("Dialog", "Increase"))
        self.decreaseBtn.setText(_translate("Dialog", "Decrease"))
        self.resetBtn.setText(_translate("Dialog", "Reset"))
