from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication,
)
from logInWindow import LogInWindow
from payrollWindow import PayrollWindow

class Resempay(QtWidgets.QMainWindow):
    def __init__(self, width, height):
        super(Resempay, self).__init__()

        self.height = height
        self.width = width
        self.isSessionStarted = False

        self.windowForm = {"Type":None}

        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.launchResempay)
        self.timer.start()

        self.show()

    def launchResempay(self):

        if self.isSessionStarted == False:
            self.launchLogInWindow()

        if self.isSessionStarted == True:
            self.launchPayrollWindow()

    def launchLogInWindow(self):

        if self.windowForm["Type"] != "LogIn" and self.isSessionStarted == False:
            loginwindow = LogInWindow(self, int(self.width-((self.width*60)//100)), int(self.height-((self.height*35)//100)), self.width, self.height)
            loginwindow.initializeUIComponents()
            loginwindow.createLayout()
            loginwindow.connectUIMethods()
            self.windowForm["Type"] = "LogIn"
    
    def launchPayrollWindow(self):

        if self.windowForm["Type"] != "Payroll" and self.isSessionStarted == True:
            payrollWindow = PayrollWindow(self, self.width, self.height)
            payrollWindow.initializeUIComponents()
            payrollWindow.createLayout()
            payrollWindow.connectUIMethods()
            self.windowForm["Type"] = "Payroll"





if __name__ == "__main__":

    app = QApplication([])
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    Resempay = Resempay(rect.width(), rect.height())
    app.exec_()