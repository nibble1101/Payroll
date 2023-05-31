import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from SharedDataSingleton import SharedDataSingleton
from restaurant import Restaurant
from Utility import Utility
from payroll import Payroll

class PayrollWindow(QObject):

    # Defining a signal
    signal = pyqtSignal()

    def __init__(self, applicationWindow, maxScreenWidth, maxScreenHeight):
        super(PayrollWindow, self).__init__()
        
        self.maxScreenWidht = maxScreenWidth
        self.maxScreenHeight = maxScreenHeight
        self.applicationWindow = applicationWindow
        self.applicationWindow.setWindowTitle("RESEMPAY")
        self.initializeUIComponents()
        self.createLayout()
        # self.connectUIMethods()

    def initializeUIComponents(self):
        
        # Loading Logos:

        self.appLogo = QPixmap('../source/logo.png')

        self.meeshaLogo = QPixmap('../source/meeshaLogo.png')

        self.KricketClubLogo = QPixmap('../source/kricketClubLogo.png')


        # Central Widget
        self.applicationWindow.centralWidgetQWidget = QtWidgets.QWidget()
        # self.applicationWindow.centralWidgetQWidget.setStyleSheet('border: 2px solid red')
        self.applicationWindow.setCentralWidget(self.applicationWindow.centralWidgetQWidget)
        # Central Widget Layout
        self.applicationWindow.centralWidgetQVBoxLayout = QtWidgets.QVBoxLayout()
        self.applicationWindow.centralWidgetQVBoxLayout.setAlignment(Qt.AlignCenter)
        
        # Generate Payroll Push Button
        self.applicationWindow.generateQPushButton = QtWidgets.QPushButton()
        self.applicationWindow.generateQPushButton.setText("Generate Payroll")
        self.applicationWindow.generateQPushButton.setEnabled(False)
        
        # Container for Restaurant logo and Date input and Generate button widgets
        self.applicationWindow.logoRestaurantDateGenerateButtonQWidget = QtWidgets.QWidget()
        self.applicationWindow.logoRestaurantDateGenerateButtonQWidget.setFixedSize(int(self.maxScreenWidht - (self.maxScreenWidht*0.60)), int(self.maxScreenHeight - (self.maxScreenHeight*0.35)))
        # self.applicationWindow.logoRestaurantDateGenerateButtonQWidget.setStyleSheet('border: 2px solid red')
        # Layout for Logo Date Button Widget
        self.applicationWindow.logoDateRestaurantGenerateButtonQVBoxLayout = QtWidgets.QVBoxLayout()
        self.applicationWindow.logoDateRestaurantGenerateButtonQVBoxLayout.setAlignment(Qt.AlignCenter)
        # Label for the restaurant logo
        self.applicationWindow.restaurantLogoQLabel = QtWidgets.QLabel()
        self.applicationWindow.restaurantLogoQLabel.setPixmap(self.appLogo)
        self.applicationWindow.restaurantLogoQLabel.setFixedSize(self.applicationWindow.logoRestaurantDateGenerateButtonQWidget.width()-int(self.applicationWindow.logoRestaurantDateGenerateButtonQWidget.width()*.05), self.applicationWindow.logoRestaurantDateGenerateButtonQWidget.height() - int(self.applicationWindow.logoRestaurantDateGenerateButtonQWidget.height()*.50))
        self.restaurantLogoQLabelHeight = self.applicationWindow.restaurantLogoQLabel.height()
        self.restaurantLogoQLabelWidth = self.applicationWindow.restaurantLogoQLabel.width()
        self.applicationWindow.restaurantLogoQLabel.setAlignment(Qt.AlignCenter)
        # Rescalling images on the basis of the restaurantLogoQLabel
        self.KricketClubLogo = self.KricketClubLogo.scaled(self.restaurantLogoQLabelWidth, self.restaurantLogoQLabelHeight)
        self.meeshaLogo = self.meeshaLogo.scaled(self.restaurantLogoQLabelWidth, self.restaurantLogoQLabelHeight)
        

        # Combo box for selecting restaurant
        self.applicationWindow.restaurantQComboBox = QtWidgets.QComboBox()
        self.applicationWindow.restaurantQComboBox.addItems(["Select Restaurant", "Kricket Club", "Meesha"])


        # Container for start and end date widgets
        self.applicationWindow.dateQWidget = QtWidgets.QWidget()
        # self.applicationWindow.dateQWidget.setStyleSheet('border: 2px solid red')
        # Layout for date widget
        self.applicationWindow.dateQHBoxLayout = QtWidgets.QHBoxLayout()

        # Container for end date widget and label
        self.applicationWindow.endDateQWidget = QtWidgets.QWidget()
        # self.applicationWindow.endDateQWidget.setStyleSheet('border: 2px solid red')
        # Layout for end date input and label
        self.applicationWindow.endDateQVBoxLayout = QtWidgets.QVBoxLayout()
        # self.applicationWindow.endDateQVBoxLayout.setAlignment(Qt.AlignCenter)
        # End Date label
        self.applicationWindow.endDateQLabel = QtWidgets.QLabel()
        self.applicationWindow.endDateQLabel.setText("End Date")
        # End Date input
        self.applicationWindow.endDateQDateEdit = QtWidgets.QCalendarWidget()
        self.applicationWindow.endDateQDateEdit.setGridVisible(False)

        # Container for start date widget and label
        self.applicationWindow.startDateQWidget = QtWidgets.QWidget()
        # self.applicationWindow.startDateQWidget.setStyleSheet('border: 2px solid red')
        self.applicationWindow.startDateQVBoxLayout = QtWidgets.QVBoxLayout()
        # self.applicationWindow.startDateQVBoxLayout.setAlignment(Qt.AlignCenter)
         # Start Date label
        self.applicationWindow.startDateQLabel = QtWidgets.QLabel()
        self.applicationWindow.startDateQLabel.setText("Start Date")
        # Start Date input
        self.applicationWindow.startDateQDateEdit = QtWidgets.QCalendarWidget()
        self.applicationWindow.startDateQDateEdit.setGridVisible(False)

    
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

    def connectUIMethods(self):

        self.applicationWindow.restaurantQComboBox.currentIndexChanged.connect(lambda: self.selectRestaurantAction())
        self.applicationWindow.generateQPushButton.clicked.connect(lambda: self.invokePayrollEngine())

    def selectRestaurantAction(self):

        restaurantOption = self.applicationWindow.restaurantQComboBox.currentText()

        if restaurantOption == "Meesha":
            self.applicationWindow.generateQPushButton.setEnabled(True)
            # self.meeshaLogo = self.meeshaLogo.scaled(self.applicationWindow.restaurantLogoQLabel.width(), self.applicationWindow.restaurantLogoQLabel.height())
            self.applicationWindow.restaurantLogoQLabel.setPixmap(self.meeshaLogo)
            self.applicationWindow.restaurantLogoQLabel.setAlignment(Qt.AlignCenter)

        if restaurantOption == "Kricket Club":
            self.applicationWindow.generateQPushButton.setEnabled(True)
            self.applicationWindow.restaurantLogoQLabel.setPixmap(self.KricketClubLogo)
            self.applicationWindow.restaurantLogoQLabel.setAlignment(Qt.AlignCenter)
            
        if restaurantOption == "Select Restaurant":
            self.applicationWindow.generateQPushButton.setEnabled(False)
            self.applicationWindow.restaurantLogoQLabel.setPixmap(self.appLogo)
            self.applicationWindow.restaurantLogoQLabel.setAlignment(Qt.AlignCenter)

    def invokePayrollEngine(self):

        start_date = str(self.applicationWindow.startDateQDateEdit.selectedDate().toPyDate().strftime("%m-%d-%Y"))
        end_date = str(self.applicationWindow.endDateQDateEdit.selectedDate().toPyDate().strftime("%m-%d-%Y"))
        restaurant_name = self.applicationWindow.restaurantQComboBox.currentText()

        restaurant_name = restaurant_name.upper()
        # Replace spaces with underscores
        restaurant_name = restaurant_name.replace(" ", "_")

        # Converting the dates to RFC339 Format
        start_date, end_date = Utility.convertDateToRFC3339(start_date, end_date)

        # Creating singleton class for the first time.
        obj = SharedDataSingleton(start_date, end_date, Restaurant(restaurant_name))
        obj.pacificStartDate = start_date
        obj.pacificEndDate = end_date

        payroll_obj = Payroll()

        payroll_obj.generatePayroll()

    def emitdataDisplayWindowSignal(self):

        self.signal.emit()



        







    

