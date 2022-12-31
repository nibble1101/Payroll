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
        self.createLayout()
        # self.connectUIMethods()

    def initializeUIComponents(self):
        
        # Central Widget
        self.applicationWindow.centralWidgetQWidget = QtWidgets.QWidget()
        self.applicationWindow.setCentralWidget( self.applicationWindow.centralWidgetQWidget)
        # Central Widget Layout
        self.applicationWindow.centralWidgetQVBoxLayout = QtWidgets.QVBoxLayout()
        # Generate Payroll Push Button
        self.applicationWindow.generateQPushButton = QtWidgets.QPushButton()
        self.applicationWindow.generateQPushButton.setText("Generate Payroll")
        
        # Container for Restaurant logo and Date input and Generate button widgets
        self.applicationWindow.logoRestaurantDateGenerateButtonQWidget = QtWidgets.QWidget()
        # Layout for Logo Date Button Widget
        self.applicationWindow.logoDateRestaurantGenerateButtonQVBoxLayout = QtWidgets.QVBoxLayout()
        # Label for the restaurant logo
        self.applicationWindow.restaurantLogoQLabel = QtWidgets.QLabel()
        # Combo box for selecting restaurant
        self.applicationWindow.restaurantQComboBox = QtWidgets.QComboBox()
        self.applicationWindow.restaurantQComboBox.addItems(["Kricket Club", "Meesha"])


        # Container for start and end date widgets
        self.applicationWindow.dateQWidget = QtWidgets.QWidget()
        # Layout for date widget
        self.applicationWindow.dateQHBoxLayout = QtWidgets.QHBoxLayout()

        # Container for end date widget and label
        self.applicationWindow.endDateQWidget = QtWidgets.QWidget()
        # Layout for end date input and label
        self.applicationWindow.endDateQVBoxLayout = QtWidgets.QVBoxLayout()
        # End Date label
        self.applicationWindow.endDateQLabel = QtWidgets.QLabel()
        self.applicationWindow.endDateQLabel.setText("End Date")
        # End Date input
        self.applicationWindow.endDateQDateEdit = QtWidgets.QDateEdit()

        # Container for start date widget and label
        self.applicationWindow.startDateQWidget = QtWidgets.QWidget()
        self.applicationWindow.startDateQVBoxLayout = QtWidgets.QVBoxLayout()
         # Start Date label
        self.applicationWindow.startDateQLabel = QtWidgets.QLabel()
        self.applicationWindow.startDateQLabel.setText("Start Date")
        # Start Date input
        self.applicationWindow.startDateQDateEdit = QtWidgets.QDateEdit()

    
    def createLayout(self):

        self.applicationWindow.centralWidgetQWidget.setLayout(self.applicationWindow.centralWidgetQVBoxLayout)
        self.applicationWindow.centralWidgetQVBoxLayout.addWidget(self.applicationWindow.logoRestaurantDateGenerateButtonQWidget)
        self.applicationWindow.centralWidgetQVBoxLayout.addWidget(self.applicationWindow.generateQPushButton)

        self.applicationWindow.logoRestaurantDateGenerateButtonQWidget.setLayout(self.applicationWindow.logoDateRestaurantGenerateButtonQVBoxLayout)
        self.applicationWindow.logoDateRestaurantGenerateButtonQVBoxLayout.addWidget(self.applicationWindow.restaurantLogoQLabel)
        self.applicationWindow.logoDateRestaurantGenerateButtonQVBoxLayout.addWidget(self.applicationWindow.restaurantQComboBox)
        self.applicationWindow.logoDateRestaurantGenerateButtonQVBoxLayout.addWidget(self.applicationWindow.dateQWidget)

        self.applicationWindow.dateQWidget.setLayout(self.applicationWindow.dateQHBoxLayout)
        self.applicationWindow.dateQHBoxLayout.addWidget(self.applicationWindow.startDateQWidget)
        self.applicationWindow.dateQHBoxLayout.addWidget(self.applicationWindow.endDateQWidget)

        self.applicationWindow.startDateQWidget.setLayout(self.applicationWindow.startDateQVBoxLayout)
        self.applicationWindow.startDateQVBoxLayout.addWidget(self.applicationWindow.startDateQLabel)
        self.applicationWindow.startDateQVBoxLayout.addWidget(self.applicationWindow.startDateQDateEdit)

        self.applicationWindow.endDateQWidget.setLayout(self.applicationWindow.endDateQVBoxLayout)
        self.applicationWindow.endDateQVBoxLayout.addWidget(self.applicationWindow.endDateQLabel)
        self.applicationWindow.endDateQVBoxLayout.addWidget(self.applicationWindow.endDateQDateEdit)






    

