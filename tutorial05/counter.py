#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:46:07 2020

@author: sukarno
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from ui.counter_pyqt5 import Ui_Dialog

class Counter(QDialog):
    def __init__ (self,parent=None):
        super(Counter,self).__init__(parent)
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.increaseBtn.clicked.connect(self.increase)
        self.ui.decreaseBtn.clicked.connect(self.decrease)
        self.ui.resetBtn.clicked.connect(self.reset)
        
        self.__counter = 0
        
        
    @pyqtSlot()
    def increase(self):
        if self.__counter > 999:
            return
        self.__counter = self.__counter + 1
        
        self.ui.countText.setText("{0}".format(self.__counter))
    
    @pyqtSlot()
    def decrease(self):
        if self.__counter == 0:
            return
        self.__counter = self.__counter - 1
        self.ui.countText.setText("{0}".format(self.__counter))
    
    @pyqtSlot()
    def reset(self):
        self.__counter = 0
        self.ui.countText.setText("{0}".format(self.__counter))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Counter()
    dlg.show()
    sys.exit(app.exec_())
