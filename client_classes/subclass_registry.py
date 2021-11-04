from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
from PIL.ImageQt import ImageQt
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QFileDialog

from gui.client.Registry.registry_view import RegistryGUI
from gui.popup import PopUp
import sys
import os
class Subclass_registry(QMainWindow):
    def __init__(self, parent = None):
        super(Subclass_registry, self).__init__()
        self.ui = RegistryGUI()
        self.ui.setupUi(self)
        
        self.parent = parent
        self.removed_option_item = False
        
        #Bind
        self.ui.options_combobox.currentTextChanged.connect(
            self.on_option_combobox_changed)
        self.ui.clear_button.clicked.connect(self.clear_text)
        self.ui.browse_button.clicked.connect(self.get_file_data)
        self.ui.send_file_data_button.clicked.connect(self.send_file_data)
        
    def clear_text(self):
        self.ui.result_textbox.clear()

    def get_file_data(self):
        file_path = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        file = open(file_path, "r")
        data = file.read()
        self.ui.file_data.setText(data)
        self.ui.path_input.setText(file_path)
        self.file_path = file_path
        
    def send_file(self, file_path):
        self.parent.Command({"state": "Sending File"})
        try:
            file_name = os.path.basename(file_path)
            self.parent.Send(str.encode(file_name))
            file = open(file_path, "r")
            data = file.read()
            self.parent.Send(str.encode(data))
        except Exception as e:
            print(str(e))
            raise Exception("No file found")
            
    def send_file_data(self):
        try:
            self.send_file(self.file_path)
            data = self.parent.bytes2dict(self.parent.Recv())
            PopUp.show_popup(self, "SUCCESS", data["message"])

        except Exception as e:
            PopUp.show_popup(self, "ERROR", str(e), "critical")

    def on_option_combobox_changed(self):
        if not self.removed_option_item:
            self.removed_option_item = True
            self.ui.options_combobox.removeItem(0)
            return
        cur_text = self.ui.options_combobox.currentText()

        try:
            self.ui.send_button.clicked.disconnect()
        except:
            pass

        if cur_text == "Delete value" or cur_text == "Get value":
            self.ui.name_value_input.show()
            self.ui.value_input.hide()
            self.ui.data_type_combobox.hide()
            if cur_text == "Get value":
                self.ui.send_button.clicked.connect(self.get_subkey_value)
            else:
                self.ui.send_button.clicked.connect(self.delete_value)

        elif cur_text == "Create key" or cur_text == "Delete key":
            self.ui.name_value_input.hide()
            self.ui.value_input.hide()
            self.ui.data_type_combobox.hide()
            if cur_text == "Create key":
                self.ui.send_button.clicked.connect(self.create_key)
            else:
                self.ui.send_button.clicked.connect(self.delete_key)

        else:
            self.ui.name_value_input.show()
            self.ui.value_input.show()
            self.ui.data_type_combobox.show()
            self.ui.send_button.clicked.connect(self.set_subkey)

    def get_subkey_value(self):
        try:
            path = self.ui.registry_path_input.text().replace('\\', '/')
            hive, key = path.split('/')
            subkey = self.ui.name_value_input.text()
            self.parent.Command({"state": "GetSubkeyValue"})
            self.parent.Command({"hive": hive, "key": key, "subkey": subkey})
            data = self.parent.bytes2dict(self.parent.Recv())
            self.ui.result_textbox.append(data["value"])
        except:
            self.ui.result_textbox.append("ERROR")


    #TODO: delete_value, create_key, delete_key
    def set_subkey(self):
        try:
            path = self.ui.registry_path_input.text().replace('\\', '/')
            hive, key = path.split('/')
            subkey = str(self.ui.name_value_input.text())
            value = str(self.ui.value_input.text())
            data_type = str(self.ui.data_type_combobox.currentText())
            hive = str(hive)
            key = str(key)

            self.parent.Command({"state": "SetSubkey"})
            self.parent.Command({"hive": hive, "key": key, "subkey": subkey, "value": value, "data_type": data_type})
            data = self.parent.bytes2dict(self.parent.Recv())
            self.ui.result_textbox.append(data["value"])
        except:
            self.ui.result_textbox.append("ERROR")

    def delete_value(self):
        try:
            path = self.ui.registry_path_input.text().replace('\\', '/')
            hive, key = path.split('/')
            subkey = self.ui.name_value_input.text()

            self.parent.Command({"state": "DeleteValue"})
            self.parent.Command({"hive": hive, "key": key, "subkey": subkey})

            data = self.parent.bytes2dict(self.parent.Recv())
            self.ui.result_textbox.append(data["value"])

        except:
            self.ui.result_textbox.append("ERROR")

    def create_key(self):
        try:
            path = self.ui.registry_path_input.text().replace('\\', '/')
            hive, key = path.split('/')

            
            self.parent.Command({"state": "CreateKey"})
            self.parent.Command({"hive": hive, "key": key})

            data = self.parent.bytes2dict(self.parent.Recv())
            self.ui.result_textbox.append(data["value"])
        except:
            self.ui.result_textbox.append("ERROR")

    def delete_key(self):
        try:
            path = self.ui.registry_path_input.text().replace('\\', '/')
            hive, key = path.split('/')

            self.parent.Command({"state": "DeleteKey"})
            self.parent.Command({"hive": hive, "key": key})

            data = self.parent.bytes2dict(self.parent.Recv())
            self.ui.result_textbox.append(data["value"])
        except:
            self.ui.result_textbox.append("ERROR")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Subclass_registry()
    main_win.show()
    sys.exit(app.exec_())