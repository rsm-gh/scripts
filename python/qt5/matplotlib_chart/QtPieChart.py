#!/usr/bin/python3
# -*- coding: utf-8 -*-
   
#
# Qt5 code snippet - exemple of a matplotlib pie chart
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
        
        self.pie_chart = QtPieChart(self)
        self.vlayout.addWidget(self.pie_chart)
        
        
        #
        # Display the main window
        #
        
        self.show()
        



class QtPieChart(QWidget):
    
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
        
        labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        
        qt_subplot.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        qt_subplot.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        self.canvas.draw()
        

if __name__ == "__main__":
    
    app = QApplication([])
    w=MainWindow()
    sys.exit(app.exec())
    
