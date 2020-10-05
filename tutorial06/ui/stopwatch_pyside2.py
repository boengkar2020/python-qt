# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stopwatch.ui'
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
        Dialog.resize(434, 186)
        Dialog.setMinimumSize(QSize(434, 186))
        Dialog.setMaximumSize(QSize(434, 186))
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.countText = QLabel(Dialog)
        self.countText.setObjectName(u"countText")
        font = QFont()
        font.setPointSize(72)
        self.countText.setFont(font)
        self.countText.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.countText.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.countText)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startBtn = QPushButton(Dialog)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(150, 0))
        self.startBtn.setStyleSheet(u"background-color: #7e7e7e;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.startBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stopBtn = QPushButton(Dialog)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setMinimumSize(QSize(150, 0))
        self.stopBtn.setStyleSheet(u"background-color: #7e7e7e;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.stopBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Stop Watch", None))
        self.countText.setText(QCoreApplication.translate("Dialog", u"0.00.00.0", None))
        self.startBtn.setText(QCoreApplication.translate("Dialog", u"Start", None))
        self.stopBtn.setText(QCoreApplication.translate("Dialog", u"Stop", None))
    # retranslateUi

