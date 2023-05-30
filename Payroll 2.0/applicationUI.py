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

        # AVAILABLE SCREEN WIDTH AND HEIGHT
        self.height = height
        self.width = width

        # STARTING WIDHT AND HEIGHT OF THE SCREEN
        self.startWidth = int(self.width-((self.width*60)//100))
        self.startHeight = int(self.height-((self.height*35)//100))

        # UI CLASS RESPONSIBLE FOR LOGIN INTERFACE.
        self.loginwindow = LogInWindow(self, self.startWidth, self.startHeight, self.width, self.height)

        # UI CLASS RESPONSIBLE FOR TAKING RESTAURANT AND DATE INPUT.
        self.payrollWindow = PayrollWindow(self, self.width, self.height)

        # UI CLASS RESPONSIBLE FOR DISPLAYING DATA FROM THE API.
        self.dataDisplayWindow = DataDisplayWindow(self, self.startWidth, self.startHeight, self.width, self.height)

        # UI RESPONSES CONNECTED WITH METHODS.
        self.connectUIMethods()

        self.show()


    def connectUIMethods(self):
        """
        Description: Connects the UI events with methods.

        Parameters
        ----------
        *****

        Returns
        -------
        *****

        Raises
        ------
        *****
        """

        self.loginwindow.signal.connect(lambda: self.payrollWindowSignalRecieved())
        self.payrollWindow.signal.connect(lambda: self.dataDisplayWindowSignalRecieved())

    def launchResempay(self):
        """
        Description: Launches the Resempay application.

        Parameters
        ----------
        *****

        Returns
        -------
        *****

        Raises
        ------
        *****
        """

        self.launchLogInWindow()

    def launchLogInWindow(self):
        """
        Description: Invoked by 'launchResempay' method. Initializes UI components, creates layout and connects
                     UI events to methods.

        Parameters
        ----------
        *****

        Returns
        -------
        *****

        Raises
        ------
        *****
        """

        self.loginwindow.initializeUIComponents()
        self.loginwindow.createLayout()
        self.loginwindow.connectUIMethods()
    
    def launchPayrollWindow(self):

        """
        Description: Invoked when successful login event signal received. Initializes UI components, creates layout and connects
                     UI events to methods.

        Parameters
        ----------
        *****

        Returns
        -------
        *****

        Raises
        ------
        *****
        """

        self.payrollWindow.initializeUIComponents()
        self.payrollWindow.createLayout()
        self.payrollWindow.connectUIMethods()

    def launchDataDisplayWindow(self):

        """
        Description: Invoked when generate payroll event signal received. Initializes UI components, creates layout and connects
                     UI events to methods.

        Parameters
        ----------
        *****

        Returns
        -------
        *****

        Raises
        ------
        *****
        """

        self.dataDisplayWindow.initializeUIComponents()
        self.dataDisplayWindow.createLayout()



    def payrollWindowSignalRecieved(self):
        """
        Description: Recieves the signal from 'LogInWindow' and invokes 'launchPayrollWindow'.

        Parameters
        ----------
        *****

        Returns
        -------
        *****

        Raises
        ------
        *****
        """
        self.launchPayrollWindow()

    def dataDisplayWindowSignalRecieved(self):

        """
        Description: Recieves the signal from 'LogInWindow' and invokes 'launchDataDisplayWindow'.

        Parameters
        ----------
        *****

        Returns
        -------
        *****

        Raises
        ------
        *****
        """

        self.launchDataDisplayWindow()

    
############################### PROGRAM EXECUTION POINT ###############################

if __name__ == "__main__":

    app = QApplication([])
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    resempay = Resempay(rect.width(), rect.height())
    resempay.launchResempay()
    app.exec_()