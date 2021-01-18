# 

import os
os.system("sudo pigpiod -t 0")

import stepperPigpioAcc
import SquareWave
import CosineWave
import StepForward

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

import sys
import os.path
import random

def test(pixmap):
    print("2323")

class points:
    x=0
    y=0

class MainPage(QDialog):
    
    def __init__(self):
        self.point = points
        self.left   = 10
        self.top    = 10
        self.width  = 640
        self.height = 480
        self.NumberLoadedImage = 0
        self.isZoom = False
        self.selectedPath = 0
        super(MainPage, self).__init__()
        self.ui = loadUi('DngViewer.ui', self)

        self.squareWaveButton.clicked.connect(self.squareWave)
        self.cosineWaveButton.clicked.connect(self.cosineWave)
        self.plusButton.clicked.connect(self.stepForward)
        self.minusButton.clicked.connect(self.stepBackward)
        
        self.strokeLengthSpinBox.setRange(0.01,0.22)
        self.strokeLengthSpinBox.setValue(0.10)
        self.strokeLengthSpinBox.setDecimals(2)
        self.strokeLengthSpinBox.setSingleStep(0.01)
        
        self.strokePeriodSpinBox.setRange(0.1,10.0)
        self.strokePeriodSpinBox.setValue(1.0)
        self.strokePeriodSpinBox.setDecimals(2)
        self.strokePeriodSpinBox.setSingleStep(0.1)

        self.numberOfStrokesSpinBox.setRange(1,100)
        self.numberOfStrokesSpinBox.setValue(4)
        self.numberOfStrokesSpinBox.setSingleStep(1)
        
    def stepForward(self):
        StepForward.runStepper(0)

    def stepBackward(self):
        StepForward.runStepper(1)

    def squareWave(self):
        stroke     = self.strokeLengthSpinBox.value()
        period     = self.strokePeriodSpinBox.value()
        numStrokes = self.numberOfStrokesSpinBox.value()
        SquareWave.runStepper(stroke,period,numStrokes)
        
    def cosineWave(self):
        stroke     = self.strokeLengthSpinBox.value()
        period     = self.strokePeriodSpinBox.value()
        numStrokes = self.numberOfStrokesSpinBox.value()
        CosineWave.runStepper(stroke,period,numStrokes)
        
if __name__ == '__main__':        
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec_()) 
        

 

