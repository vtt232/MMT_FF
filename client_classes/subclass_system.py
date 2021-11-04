from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

from gui.client.System.client_system_ui import Ui_Form
from gui.popup import PopUp
class Subclass_sys(QWidget):
    
    def __init__(self, parent = None):
        super(Subclass_sys, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.parent = parent
        #Bind
        self.ui.Restart.clicked.connect(
            self.Restart)
        self.ui.Logout.clicked.connect(
            self.Logout)
        self.ui.Shutdown.clicked.connect(
            self.Shutdown)
    def Restart(self):
        try:
            self.parent.Command( { "state" : "Restart" } )
        except Exception as e:
            errorMsg = "Cannot restart.\n" + str(e)
            PopUp.show_popup(self, "Error", errorMsg,
                           "warning")
            
    def Logout(self):
        try:
            self.parent.Command( { "state" : "Logout" } )
        except Exception as e:
            errorMsg = "Cannot logout.\n" + str(e)
            PopUp.show_popup(self, "Error", errorMsg,
                           "warning")
    def Shutdown(self):
        try:
            self.parent.Command( { "state" : "Shutdown" } )
        except Exception as e:
            errorMsg = "Cannot shutdown.\n" + str(e)
            PopUp.show_popup(self, "Error", errorMsg,
                           "warning")