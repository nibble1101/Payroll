import sys

from PyQt5.QtCore import QObject, QSize, QMargins
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy


class DataDisplayWindow(QObject):

    def __init__(self, applicationWindow, startWidth, startHeight, width, height):
        super(DataDisplayWindow, self).__init__()

        self.applicationWindow = applicationWindow
        self.width = width
        self.height = height
        self.applicationWindow.resize(startWidth, startHeight)
        self.applicationWindow.setWindowTitle("RESEMPAY")
        self.initializeUIComponents()
        self.createLayout()
        # self.connectUIMethods()

    def initializeUIComponents(self):

        # Creating a Central Widget
        self.applicationWindow.centralWidgetQWidget = QtWidgets.QWidget()
        # Creating a vertical layout for Central Widget.
        self.applicationWindow.centralWidgetQVBoxLayout = QtWidgets.QVBoxLayout()

        # Creating Scroll Area
        self.applicationWindow.scrollQScrollArea = QtWidgets.QScrollArea()
        # VBox Layout for scroll area
        self.applicationWindow.scrollQVBoxLayout = QtWidgets.QVBoxLayout()
        # Creating a widget to add in the scroll area.
        self.applicationWindow.scrollAreaQWidget = QtWidgets.QWidget()
        # Creating 4 required display tables
        self.applicationWindow.tipQTableWidget = QtWidgets.QTableWidget()
        self.applicationWindow.gratuityQTableWidget = QtWidgets.QTableWidget()
        self.applicationWindow.pointsQTableWidget = QtWidgets.QTableWidget()
        self.applicationWindow.hoursQTableWidget = QtWidgets.QTableWidget()

        # Push button for generating final results
        self.generateQPushButton = QtWidgets.QPushButton()
        self.generateQPushButton.setText("Generate results.")

   
    def  createLayout(self):

        self.applicationWindow.setCentralWidget(self.applicationWindow.centralWidgetQWidget)
        self.applicationWindow.centralWidgetQWidget.setLayout(self.applicationWindow.centralWidgetQVBoxLayout)

        self.applicationWindow.centralWidgetQVBoxLayout.addWidget(self.applicationWindow.scrollQScrollArea)

        self.applicationWindow.centralWidgetQVBoxLayout.addWidget(self.generateQPushButton)

        self.applicationWindow.scrollQScrollArea.setWidget(self.applicationWindow.scrollAreaQWidget)
        self.applicationWindow.scrollQScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.applicationWindow.scrollQScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.applicationWindow.scrollQScrollArea.setWidgetResizable(True)

        self.applicationWindow.scrollAreaQWidget.setLayout(self.applicationWindow.scrollQVBoxLayout)

        self.applicationWindow.scrollQVBoxLayout.addWidget(self.applicationWindow.tipQTableWidget)
        self.applicationWindow.scrollQVBoxLayout.addWidget(self.applicationWindow.gratuityQTableWidget)
        self.applicationWindow.scrollQVBoxLayout.addWidget(self.applicationWindow.pointsQTableWidget)
        self.applicationWindow.scrollQVBoxLayout.addWidget(self.applicationWindow.hoursQTableWidget)
        