# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'counter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(260, 300)
        Dialog.setMinimumSize(QSize(260, 300))
        Dialog.setMaximumSize(QSize(260, 300))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.countText = QLabel(Dialog)
        self.countText.setObjectName(u"countText")
        font = QFont()
        font.setPointSize(72)
        self.countText.setFont(font)
        self.countText.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.countText)

        self.increaseBtn = QPushButton(Dialog)
        self.increaseBtn.setObjectName(u"increaseBtn")

        self.verticalLayout.addWidget(self.increaseBtn)

        self.decreaseBtn = QPushButton(Dialog)
        self.decreaseBtn.setObjectName(u"decreaseBtn")

        self.verticalLayout.addWidget(self.decreaseBtn)

        self.resetBtn = QPushButton(Dialog)
        self.resetBtn.setObjectName(u"resetBtn")

        self.verticalLayout.addWidget(self.resetBtn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Counter", None))
        self.countText.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.increaseBtn.setText(QCoreApplication.translate("Dialog", u"Increase", None))
        self.decreaseBtn.setText(QCoreApplication.translate("Dialog", u"Decrease", None))
        self.resetBtn.setText(QCoreApplication.translate("Dialog", u"Reset", None))
    # retranslateUi

