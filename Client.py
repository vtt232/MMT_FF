import socket
import sys
#GUI
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from gui.client.client_main_ui import Ui_ClientWindow
#from gui.client.Registry.registry_view import RegistryGUI
from gui.popup import PopUp

from client_classes.subclass_screen import Subclass_Screen
from client_classes.subclass_file import Subclass_File
from client_classes.subclass_keyboard import Subclass_Keyboard
from client_classes.subclass_processView import ProcessView
from client_classes.subclass_appView import AppView
from client_classes.subclass_registry import Subclass_registry
from client_classes.subclass_system import Subclass_sys

#from server_functions.stream_client import StreamClient
#
import json
import os
#bo tro

    
class Client(QMainWindow):
    def dict2bytes(self, aDict):
        res = json.dumps(aDict).encode('utf-8')
        return res

    def bytes2dict(self, abytes):
        res=json.loads(abytes.decode('utf-8'))
        return res

    def __init__(self):
        super(Client, self).__init__()
        self.ui = Ui_ClientWindow()
        self.ui.setupUi(self)
        self.ui.Connect_button.clicked.connect(self.Connect)
        self.ui.Disconnect_button.clicked.connect(self.Disconnect)

        #Bind system
        self.ui.Get_MAC_button.clicked.connect(
            self.GetMac)
            
        #Children
        self.sub_system = Subclass_sys(self)
        self.ui.System_button.clicked.connect(self.sub_system.show)
        
        self.sub_window_screen = Subclass_Screen(self)
        self.ui.ScreenCapture_button.clicked.connect(self.sub_window_screen.show)
        
        self.sub_window_file=Subclass_File(self)
        self.ui.File_Show_button.clicked.connect(self.sub_window_file.show)
        
        self.sub_window_keyboard = Subclass_Keyboard(self)
        self.ui.Keyboard_show_button.clicked.connect(self.sub_window_keyboard.show)

        self.processView = ProcessView(self)
        self.ui.processButton.clicked.connect(self.processView.show)

        self.appView = AppView(self)
        self.ui.appButton.clicked.connect(self.appView.show)

        self.registryView = Subclass_registry(self)
        self.ui.registryButton.clicked.connect(self.registryView.show)

        #config
        self.TCP_PORT = 10000
        self.s = None

    def GetMac(self):
        try:
            self.Command({ "state" : "MAC" })
            data = self.Recv()
            if data != None:
                data = data.decode()
                PopUp.show_popup(self, "Information", data)
        except Exception as e:
            PopUp.show_popup(self, "Error", str(e), "warning")
    def __del__(self):
        self.Disconnect()

    def Send(self, data):
        try:
            self.s.sendall(str(len(data)).zfill(12).encode())
            self.s.sendall(data)
        except Exception as e:
            raise Exception("Not connected to server")

    def Recv(self):
        try:
            data_size = int(self.s.recv(12).decode())
            data = self.s.recv(data_size)
            return data
        except Exception as e:
            raise Exception("Not connected to server")

    def Connect(self):
        if self.s != None:
            self.Disconnect()
        self.TCP_IP = self.ui.IP_input.text()
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.settimeout(5)
            self.s.connect((self.TCP_IP, self.TCP_PORT))
            self.s.settimeout(None)
            PopUp.show_popup(self, "Success", "Successfully connected")
        except Exception as e:
            msg = "Server not found.\n" + str(e)
            PopUp.show_popup(self, "Error", msg, "critical")
            self.s = None
    def Disconnect(self):
        if self.s == None:
            PopUp.show_popup(self, "Error", 
                             "Not connected to any server", 
                             "warning")
            return
        try:
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            self.s = None
            PopUp.show_popup(self, "Success", 
                             "Successfully disconnected.")
        except Exception as e:
            PopUp.show_popup(self, "Error", str(e), "warning")

    def Command(self, data):
        try:
            self.Send(self.dict2bytes(data))
        except Exception as e:
            msg = f"Cannot send command {data}.\n" + str(e)
            raise Exception(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Client()
    main_win.show()
    sys.exit(app.exec_())











