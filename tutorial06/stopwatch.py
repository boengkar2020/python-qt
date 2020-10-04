#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:46:45 2020

@author: sukarno
"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSlot, QTimer
from ui.stopwatch_pyqt5 import Ui_Dialog

class StopWatch(QDialog):
    def __init__(self,parent=None):
        super(StopWatch,self).__init__(parent)
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.startBtn.clicked.connect(self.start_handler)
        self.ui.stopBtn.clicked.connect(self.stop_handler)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_handler)
        
        
    def init_val(self):
        self.ms = 0
        self.second = 0
        self.minute = 0
        self.hour = 0
        
    @pyqtSlot()
    def start_handler(self):
        self.init_val()
        self.timer.start(100)
    
    @pyqtSlot()
    def stop_handler(self):
        self.timer.stop()
    
    @pyqtSlot()
    def timer_handler(self):
        self.ms = self.ms + 1
        
        if self.ms > 9 :
            self.ms = 0
            
            self.second = self.second + 1
            
            if self.second > 59:
                self.second = 0
                
                self.minute = self.minute + 1
                
                if self.minute > 59:
                    self.minute = 0
                    
                    self.hour = self.hour + 1
                    
                    if self.hour > 9:
                        self.init_val()
                        
        self.ui.countText.setText("{0}:{1:0>2d}:{2:0>2d}:{3}".format(self.hour,self.minute,self.second,self.ms))

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    dlg = StopWatch()
    dlg.show()
    sys.exit(app.exec_())    