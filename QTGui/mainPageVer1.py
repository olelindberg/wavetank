# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DngViewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QListView,QAbstractItemView, QTreeView, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem
from PyQt5 import QtCore
import os
import os.path
os.system("sudo pigpiod")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QTableWidgetItem
from PyQt5.QtGui import QIcon

import stepperPigpioAcc
#import ConvertDngImageFast
#import ConvertDngImage

#from concurrent.futures import ThreadPoolExecutor
#from PySide import QtGui,
os.system("sudo Pigpiod")
def test(pixmap):
    print("2323")

class points:
    x=0
    y=0

class MainPage(QDialog):
    
    def __init__(self):
        self.point = points
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.NumberLoadedImage = 0
        self.isZoom = False
        self.selectedPath = 0
        super(MainPage, self).__init__()
        #loadUi('DngViewer.ui', self)
        self.ui = loadUi('DngViewer.ui', self)

#        self.tableWidget.doubleClicked.connect(self.loadSelectedImage)

        self.pushButton.clicked.connect(self.test1)
#        self.shortcut = QShortcut(QKeySequence("1"), self)
#        self.shortcut.activated.connect(self.openShortCutPath)
        
#        self.shortcut = QShortcut(QKeySequence("2"), self)
#        self.shortcut.activated.connect(self.openShortCutPathBack)

#        self.shortcut = QShortcut(QKeySequence("q"), self)
#        self.shortcut.activated.connect(self.openShortCutZoom)
        
#        self.shortcut = QShortcut(QKeySequence("w"), self)
#        self.shortcut.activated.connect(self.openShortCutZoomBack)        
        

    def test1(self):
        stepperPigpioAcc.runStepper()
        print("peter")
        #self.loadImge(0)
        #self.pushButton_1.setIcon(QIconScale[0])
        #self.pushButton_1.setIconSize(QtCore.QSize(bSmall,hSmall))
        
if __name__ == '__main__':        
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec_()) 
        

 

