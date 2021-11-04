from gui.client.App_process.TableView import Ui_Form
from gui.client.App_process.InputButtonView import InputButtonView

from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QFileDialog

from gui.popup import PopUp
class AppView(QWidget):
    def __init__(self, client):
        super(AppView, self).__init__()

        self.client = client
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.view_button.clicked.connect(self.view_function)
        self.ui.kill_button.clicked.connect(self.kill_function)
        self.ui.start_button.clicked.connect(self.start_function)
        self.ui.clear_button.clicked.connect(self.clear_data)
    def clear_data(self):
        self.ui.tableWidget.setRowCount(0)
    def insert_data(self, data):
        self.clear_data()

        for i in range(len(data)):
            self.ui.tableWidget.insertRow(i)
            for j in range(len(data[i])):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
    def view_function(self):
        try:
            self.client.Command({"state": "GetApps"})
            data = self.client.bytes2dict(self.client.Recv())
            self.insert_data(data)

        except Exception as e:
            msg = "Cannot view.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)

    def kill_function(self):
        def kill_app(app_id, parent = None):
            try:
                self.client.Command({"state": "KillApp"})
                self.client.Command({"app_id": app_id})
                data = self.client.bytes2dict(self.client.Recv())
                PopUp.show_popup(parent, "SUCCESS", data["message"], 
                                 closeParent=True)
            except Exception as e:
                msg = f"Cannot kill {app_id}.\n" + str(e)
                PopUp.show_popup(parent, "Error", msg, 
                                 closeParent=True)
        self.kill_input_button_view = InputButtonView(
            "Kill app", "Enter app ID", "Kill",
            kill_app)
        self.kill_input_button_view.show()
    def start_function(self):
        def start_app(app_name, parent = None):
            try:
                self.client.Command({"state": "StartApp"})
                self.client.Command({"app_name": app_name})
                data = self.client.bytes2dict(self.client.Recv())
                PopUp.show_popup(parent, "SUCCESS", data["message"],
                                 closeParent=True)
                
            except Exception as e:
                msg = f"Cannot start {app_name}.\n" + str(e)
                PopUp.show_popup(parent, "Error", msg, 
                                 closeParent=True)
        self.start_input_button_view = InputButtonView(
            "Start app", "Enter app Name", "Start", 
            start_app)
        self.start_input_button_view.show()