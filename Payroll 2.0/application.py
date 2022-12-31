from PyQt5 import QtWidgets
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

        # self.setWindowTitle("LabView")
        self.launchResempay()
        self.show()

    def launchResempay(self):

        self.launchLogInWindow()

    def launchLogInWindow(self):
        loginwindow = LogInWindow(self, int(self.width-((self.width*60)//100)), int(self.height-((self.height*50)//100)), self.width, self.height)
        loginwindow.initializeUIComponents()
        loginwindow.createLayout()

        # input()
        
        payrollWindow = PayrollWindow(self)
        payrollWindow.initializeUIComponents()





if __name__ == "__main__":

    app = QApplication([])
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    Resempay = Resempay(rect.width(), rect.height())
    app.exec_()