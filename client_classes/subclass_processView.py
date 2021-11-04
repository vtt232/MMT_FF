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
class ProcessView(QWidget):
    def __init__(self, client):
        super(ProcessView, self).__init__()

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
            self.client.Command({"state": "GetProcesses"})
            data = self.client.bytes2dict(self.client.Recv())
            self.insert_data(data)
        except Exception as e:
            msg = "Cannot view.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)

    def kill_function(self):
        def kill_process(process_id, parent = None):
            try:
                self.client.Command({"state": "KillProcess"})
                self.client.Command({"process_id": process_id})
                data = self.client.bytes2dict(self.client.Recv())
                PopUp.show_popup(parent, "SUCCESS", data["message"], 
                                 closeParent=True)
            except Exception as e:
                msg = f"Cannot kill {process_id}.\n" + str(e)
                PopUp.show_popup(parent, "Error", msg, 
                                 closeParent=True)

        self.kill_input_button_view = InputButtonView(
            "Kill Process", "Enter Process ID", "Kill", kill_process)
        self.kill_input_button_view.show()

    def start_function(self):
        def start_process(process_name, parent = None):
            try:
                self.client.Command({"state": "StartProcess"})
                self.client.Command({"process_name": process_name})
                data = self.client.bytes2dict(self.client.Recv())
                PopUp.show_popup(parent, "SUCCESS", data["message"],
                                 closeParent=True)
            except Exception as e:
                msg = f"Cannot start {process_name}.\n" + str(e)
                PopUp.show_popup(parent, "Error", msg, 
                                 closeParent=True)
        self.start_input_button_view = InputButtonView(
            "Start Process", "Enter Process Name", "Start", start_process)
        self.start_input_button_view.show()