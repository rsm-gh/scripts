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


import sys
from time import sleep
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from main_window.MainWindowUI import Ui_main_window
from loading_window.LoadingDialog import LoadingDialog

class MainWindow(QMainWindow, Ui_main_window):
    
    
    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        ##
        ## Center the main window: https://gist.github.com/saleph/163d73e0933044d0e2c4
        ##
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
        ##
        ## Display the LoadingDialog
        ##
        
        self.__loading_dialog = LoadingDialog(self)
        
        self.__loading_dialog.set_progress_bar_value(0)
        Thread(target=self.__initialize_data).start()
        self.__loading_dialog.exec_()
        
        
        ##
        ## Display the main window
        ##
        
        self.show()
        
        
    def __initialize_data(self):
        
        if self.__loading_dialog is None:
            return
        
        i = 0
        while i < 100:
            i+=15
            self.__loading_dialog.progress_percent.emit(i)
            sleep(0.55)
         
         
         
def main():
    
    app = QApplication([])
    w=MainWindow()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
    