#!/usr/bin/python3
# -*- coding: utf-8 -*-
   
#
# Qt5 code snippet - exemple of a matplotlib pie chart
#
# Written in 2020 by Rafael SENTIES MARTINELLI
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
from datetime import datetime


from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MainWindow(QMainWindow):
    #
    # Class for testing QtPieChart()
    #
    
    
    def __init__(self, parent=None) :


        #
        # Init the main window and a layout
        #        
        super(MainWindow, self).__init__(parent)

        widget = QWidget()
        self.vlayout = QVBoxLayout()
        widget.setLayout(self.vlayout)
        
        self.setCentralWidget(widget)
    
        #
        # Add some random widget
        #
        
        label = QLabel()
        label.setText("Exemple")
        self.vlayout.addWidget(label)
        
        
        #
        # Add the pie chart
        #
        
        self.bar_chart = QtBarChart(self)
        self.vlayout.addWidget(self.bar_chart)
        
        
        #
        # Display the main window
        #
        
        self.show()
        



class QtBarChart(QWidget):
    
    def __init__(self, parent):
         
 
        super(QWidget, self).__init__(parent)
 
        self.qt_chart_height = 250
        self.qt_chart_width = 250

        #
        # The sizie of the widget must be at least
        # as bigger as the figure for displaying the chart.
        #
        self.setMinimumHeight(self.qt_chart_height)
        self.setMinimumWidth(self.qt_chart_width)
 
        self.figure = plt.figure(figsize=(3, 3), dpi=80)
        self.canvas = FigureCanvasQTAgg(self.figure)
 
        self.canvas.setParent(self)
        
        self.draw()
         
 
    def draw(self):
         
        self.figure.clear()
 
        qt_subplot = self.figure.add_subplot(111)
        

        x = ['01/01', '01/02', '01/03', '01/04', '01/05', '01/06']
        energy = [5, 6, 15, 22, 24, 8]
        x_pos = [i for i, _ in enumerate(x)]

        qt_subplot.bar(x_pos, energy, color=['red','green','blue','green','red','purple'])
        qt_subplot.set_xticklabels(x, rotation=90)

        
        self.canvas.draw()
        

if __name__ == "__main__":
    
    app = QApplication([])
    w=MainWindow()
    sys.exit(app.exec())
    
