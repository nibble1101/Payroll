from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication,
)
from logInWindowUI import LogInWindow
from payrollWindowUI import PayrollWindow
from dataDisplayUI import DataDisplayWindow

class Resempay(QtWidgets.QMainWindow):
    def __init__(self, width, height):
        super(Resempay, self).__init__()

        self.height = height
        self.width = width

        self.loginwindow = LogInWindow(self, int(self.width-((self.width*60)//100)), int(self.height-((self.height*35)//100)), self.width, self.height)
        self.payrollWindow = PayrollWindow(self, self.width, self.height)
        self.dataDisplayWindow = DataDisplayWindow(self, int(self.width-((self.width*60)//100)), int(self.height-((self.height*35)//100)), self.width, self.height)
        self.loginwindow.signal.connect(lambda: self.payrollWindowSignalRecieved())
        self.payrollWindow.signal.connect(lambda: self.dataDisplayWindowSignalRecieved())

        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(10)
        # self.timer.timeout.connect(self.launchResempay)
        # self.timer.start()

        self.show()

    def launchResempay(self):

        self.launchLogInWindow()

    def launchLogInWindow(self):
        
        
        self.loginwindow.initializeUIComponents()
        self.loginwindow.createLayout()
        self.loginwindow.connectUIMethods()
    
    def launchPayrollWindow(self):

        self.payrollWindow.initializeUIComponents()
        self.payrollWindow.createLayout()
        self.payrollWindow.connectUIMethods()

    def launchDataDisplayWindow(self):

        self.dataDisplayWindow.initializeUIComponents()
        self.dataDisplayWindow.createLayout()



    def payrollWindowSignalRecieved(self):

        self.launchPayrollWindow()

    def dataDisplayWindowSignalRecieved(self):

        print("Here")
        self.launchDataDisplayWindow()

    





if __name__ == "__main__":

    app = QApplication([])
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    resempay = Resempay(rect.width(), rect.height())
    resempay.launchResempay()
    app.exec_()