import sys

from PyQt5.QtCore import QObject, QSize, QMargins
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy

class PayrollWindow(QObject):

    def __init__(self, applicationWindow):
        super(PayrollWindow, self).__init__()

        self.applicationWindow = applicationWindow
        self.applicationWindow.setWindowTitle("RESEMPAY")
        self.initializeUIComponents()
        # self.createLayout()
        # self.connectUIMethods()

    def initializeUIComponents(self):
        
        self.applicationWindow.centralWidgetQWidget = QtWidgets.QWidget()
        self.applicationWindow.setCentralWidget( self.applicationWindow.centralWidgetQWidget)