""" 
Denyse Huezo 
id:dah12 
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import sys, os, random

def main():
 class SineGui(QMainWindow):
    def __init__(self, pp=None):
        QMainWindow.__init__(self, pp)
        self.colorNum = 1
        self.ap = 1.0     
        self.ph = 0.0
        self.fr = 1.0
        self.Frame()
        self.draw()
    def convert(self):
        self.fr = float(self.fEdit.text())
        self.ap = float(self.ampEdit.text())
        self.ph = float(self.phsEdit.text())
        self.draw()
    def Frame(self):
       self.setWindowTitle("Let's plot the Sine function!") 
       self.f= Figure() 
       self.canvas= FigureCanvas(self.f) 
       self.colorNum=1 
       self.mf= QWidget() 
       self.canvas.setParent(self.mf) 
       self.axes= self.f.add_subplot(111) 
       self.toolbar=NavigationToolbar(self.canvas, self.mf) 
       self.plotButton = QPushButton('Plot Sine Wave', self)
       self.clearButton = QPushButton('Clear', self)
       v=QVBoxLayout() 
       v.addWidget(self.canvas) 
       v.addWidget(self.toolbar) 
       self.mf.setLayout(v) 
       self.setCentralWidget(self.mf) 
       phs= QLabel("Phase:") 
       amp=QLabel("Amplitude:") 
       f=QLabel("Frequency:") 
       self.phsEdit= QLineEdit() 
       self.ampEdit=QLineEdit() 
       self.fEdit= QLineEdit() 
       g = QGridLayout()
       g.addWidget(self.fEdit,2,1)
       g.addWidget(self.ampEdit,1,1)
       g.setSpacing(10)
       g.addWidget(amp,1,0)
       g.addWidget(phs,3,0)
       g.addWidget(f,2,0)
       g.addWidget(self.phsEdit,3,1)
       self.setLayout(g)
       v.addLayout(g)
       h= QHBoxLayout()
       h.addWidget(self.clearButton)
       h.addWidget(self.plotButton)
       v.addLayout(h)
       self.clearButton.clicked.connect(self.Frame)
       self.plotButton.clicked.connect(self.convert)
       t = np.arange(0, 5, .001) 
       self.axes.axis([0, 2, -1.5, 1.5])

    def draw(self):
        if self.colorNum > 6:
            self.colorNum = self.count % 6
        if self.colorNum == 1:
            self.color = 'b'
        if self.colorNum == 2:
            self.color = 'r'
        if self.colorNum == 3:
            self.color = 'g'
        if self.colorNum == 4:
            self.color = 'y'
        if self.colorNum == 5:
            self.color = 'm'
        if self.colorNum == 6:
            self.color = 'k'
        cl=np.arange(0,5,.0001)
        self.axes.axis([0,2,-1.5,1.5]) 
        self.axes.plot(cl, self.ap*np.sin(2*np.pi*self.fr*cl + self.ph),self.color) 
        self.colorNum+=1 
        self.canvas.draw()
       
 app = QApplication(sys.argv)
 window = SineGui()
 window.show()
 app.exec_()

if __name__ == "__main__": 
   main()    

   
