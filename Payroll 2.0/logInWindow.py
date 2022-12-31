import sys

from PyQt5.QtCore import QObject, QSize, QMargins
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy

class LogInWindow(QObject):

    def __init__(self, applicationWindow, startWidth, startHeight, width, height):
        super(LogInWindow, self).__init__()

        self.applicationWindow = applicationWindow
        self.width = width
        self.height = height
        self.applicationWindow.resize(startWidth, startHeight)
        self.applicationWindow.setWindowTitle("RESEMPAY")
        self.initializeUIComponents()
        self.createLayout()
        self.connectUIMethods()

    def initializeUIComponents(self):

        # Logo
        self.pixmap = QPixmap('logo.png')
        imageHeight = self.pixmap.height()
        imageWidth = self.pixmap.width()

        # 1. Central Widget
        self.applicationWindow.centralWidgetQWidget = QtWidgets.QWidget()
        
        # 1.1 Adding Horizontal Layout to the central widget
        self.applicationWindow.horizontalLayoutHBoxLayout = QtWidgets.QHBoxLayout()

        # Logo and Application Name QFrame
        self.applicationWindow.logoNameQFrame = QtWidgets.QFrame()
        self.applicationWindow.logoNameQFrame.setMaximumSize(QSize(self.width//4, self.height//2))
        self.applicationWindow.logoNameQFrame.setContentsMargins(20,120,10,100)

        # 1.1 Logo & Application Name Vertical Box Layout
        self.applicationWindow.logoNameQVBoxLayout = QtWidgets.QVBoxLayout()

        # 1.1.1 Logo Icon Widget
        self.applicationWindow.logoQLabel = QtWidgets.QLabel()
        self.applicationWindow.logoQLabel.setPixmap(self.pixmap)
        self.applicationWindow.logoQLabel.setAlignment(Qt.AlignCenter)
        self.applicationWindow.logoQLabel.resize(QSize(imageWidth, imageHeight))

        # 1.1.2 Application Name
        self.applicationWindow.nameLabelQlabel = QtWidgets.QLabel()
        self.applicationWindow.nameLabelQlabel.setText("RESEMPAY")
        self.applicationWindow.nameLabelQlabel.setAlignment(Qt.AlignCenter)

        # Creating a VBoxLayout for the LogIn or Create Frame
        self.applicationWindow.logInOrCreateQVboxLayout = QtWidgets.QVBoxLayout()
        # 1.2 Frame for LogIn or Create Account
        self.applicationWindow.logInOrCreatQFrame = QtWidgets.QFrame()
        self.applicationWindow.logInOrCreatQFrame.setMaximumSize(QSize(self.width//4, self.height//2))
        self.applicationWindow.logInOrCreatQFrame.setContentsMargins(50,100,50,100)
        self.applicationWindow.logInOrCreateQVboxLayout.setAlignment(Qt.AlignCenter)

        # 1.2.1 LogIn or Create Account Contents

        self.applicationWindow.usernameQabel = QtWidgets.QLabel()
        self.applicationWindow.usernameQabel.setText("USERNAME")

        self.applicationWindow.usernameQLineEdit = QtWidgets.QLineEdit()
        self.applicationWindow.usernameQLineEdit.setPlaceholderText("abc@xyz.com")

        self.applicationWindow.incorrectUsernameQLabel = QtWidgets.QLabel()
        self.applicationWindow.incorrectUsernameQLabel.setText(" ")

        self.applicationWindow.passwordQlabel = QtWidgets.QLabel()
        self.applicationWindow.passwordQlabel.setText("PASSWORD")

        self.applicationWindow.passwordQLineEdit = QtWidgets.QLineEdit()
        self.applicationWindow.passwordQLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.applicationWindow.passwordQLineEdit.setPlaceholderText("************")

        self.applicationWindow.incorrectPasswordQLabel = QtWidgets.QLabel()
        self.applicationWindow.incorrectPasswordQLabel.setText(" ")

        self.applicationWindow.logInQPushButton = QtWidgets.QPushButton()
        self.applicationWindow.logInQPushButton.setText("LogIn")

        self.applicationWindow.createAccountQPushButton = QtWidgets.QPushButton()
        self.applicationWindow.createAccountQPushButton.setText("Create Account")

    def createLayout(self):

        # Setting Central Widget
        self.applicationWindow.setCentralWidget(self.applicationWindow.centralWidgetQWidget)

        # Setting Horizontal layout of the central widget
        self.applicationWindow.centralWidgetQWidget.setLayout(self.applicationWindow.horizontalLayoutHBoxLayout)

        # Adding Logo and Name to the VBoxLayout
        self.applicationWindow.logoNameQVBoxLayout.addWidget(self.applicationWindow.logoQLabel)
        self.applicationWindow.logoNameQVBoxLayout.addWidget(self.applicationWindow.nameLabelQlabel)

        self.applicationWindow.logInOrCreatQFrame.setLayout(self.applicationWindow.logInOrCreateQVboxLayout)

        # Adding Widgets to LogIn and Create Account VBoxLayout
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.usernameQabel)
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.usernameQLineEdit)
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.incorrectUsernameQLabel)
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.passwordQlabel)
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.passwordQLineEdit)
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.incorrectPasswordQLabel)
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.logInQPushButton)
        self.applicationWindow.logInOrCreateQVboxLayout.addWidget(self.applicationWindow.createAccountQPushButton)

        # Setting LogIn and Application name QFrame Layout
        self.applicationWindow.logoNameQFrame.setLayout(self.applicationWindow.logoNameQVBoxLayout)

        # Adding the QFrames to the Central Horizontal Widget Layout
        self.applicationWindow.horizontalLayoutHBoxLayout.addWidget(self.applicationWindow.logoNameQFrame)
        self.applicationWindow.horizontalLayoutHBoxLayout.addWidget(self.applicationWindow.logInOrCreatQFrame)

    def connectUIMethods(self):

        self.applicationWindow.logInQPushButton.clicked.connect(lambda: self.authenticate())


    def authenticate(self):

        isAuthenticated = True
        print("Entered")
        if isAuthenticated:
            self.applicationWindow.isSessionStarted = True

