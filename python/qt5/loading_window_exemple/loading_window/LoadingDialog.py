#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Qt5 code snippet - exemple of a loading window
#
# Written in 2019 by Rafael SENTIES MARTINELLI
#
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain 
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with
# this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 
#


from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.Qt import QDialog

from loading_window.LoadingDialogUI import Ui_LoadingDialog

class LoadingDialog(QDialog, Ui_LoadingDialog):
    
    progress_percent = pyqtSignal(int)
    
    def __init__(self, parent=None):
        
        super(LoadingDialog, self).__init__(parent)
        
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        
        self.progress_percent.connect(self.set_progress_bar_value)
        
        
    def set_progress_bar_value(self, value):
        
        if value > 100:
            value = 100
        
        self.progressBar.setValue(value)
        
        if value == 100:
            self.close()
        
         
def main(args):
    a = QApplication(args)
    f = QMainWindow()
    d=LoadingDialog(f)
    d.exec_()
    
     
if __name__=="__main__":
    
    import sys
    main(sys.argv)
    