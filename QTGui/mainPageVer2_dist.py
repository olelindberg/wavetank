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
import distanceSensorTest
import time
import os
import os.path
os.system("sudo pigpiod")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
from PyQt5.QtCore import QTimer

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QTableWidgetItem
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

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
TIME_LIMIT = 100

class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(float)

    def run(self):
        count = 0
        peter = 0
        while True:
            count +=1
            time.sleep(0.2)
            dist = distanceSensorTest.distance()
            self.countChanged.emit(dist)

class ExternalStepper(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(float)

    def run(self):
        count = 0
        peter = 1       
        stepperPigpioAcc.runStepper()
        print("peter12345")


class MainPage(QDialog):
#    def updateDate():
#        print("update data")
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
        

        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

        #self.calcStepper = ExternalStepper()
        #self.calcStepper.countChanged.connect(self.onCountChanged)
        #self.calcStepper.start()

    def onCountChanged(self, value):
        print("peter"+str(value))
        dist = distanceSensorTest.distance()
        self.label_Full.setText(str('{0:.1f}'.format(value))+" cm")
        print ("Measured Distance = %.1f cm" % dist)

#        self.progress.setValue(value)

    def readListValues(self):
        print("peter")
    def test1(self):

#        self.calcStepper.peter = 2
#        stepperPigpioAcc.runStepper()
        print("peter")
        self.label_Full.setText("peter1234")
        self.calcStepper = ExternalStepper()
        #self.calc.countChanged.connect(self.onCountChanged)
        self.calcStepper.start()
        #self.loadImge(0)
        #self.pushButton_1.setIcon(QIconScale[0])
        #self.pushButton_1.setIconSize(QtCore.QSize(bSmall,hSmall))
        
if __name__ == '__main__':        
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec_()) 
        

 

