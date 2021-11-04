import sys
#GUI
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from gui.server.server_main_ui import Ui_MainWindow
from gui.popup import PopUp

#Socket & others
import socket
import threading
import pickle
import json
import base64
#Side functions 
from server_functions.system_related import SystemHelper
from server_functions.image_capture import CaptureHelper
from server_functions.file_related import FileHelper
from server_functions.keyboard_related import KeyboardHelper
from server_functions.process_manager import ProcessManager
from server_functions.app_manager import AppManager
from server_functions.registry_manager import RegistryManager
from server_functions.stream_server import StreamServer

#from server_functions.stream_server import StreamServer

def dict2bytes(aDict):
    res = json.dumps(aDict).encode('utf-8')
    return res

def bytes2dict(abytes):
    res=json.loads(abytes.decode('utf-8'))
    return res

class Server(QMainWindow):
    def __init__(self):
        super(Server, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Server_checkbox.stateChanged.connect(self.on_change_state);
        #config
        self.hostname = ''
        self.port = 10000
        self.conn = None
        self.socket = None
        #side functions
        self.captureHelperPointer = CaptureHelper()
        self.systemHelperPointer = SystemHelper()
        self.fileHelperPointer= FileHelper()
        self.keyboardHelperPointer= KeyboardHelper()
        self.process_manager = ProcessManager()
        self.app_manager = AppManager()
        self.registry_manager = RegistryManager()
        #display ip
        self.ui.My_IP.setText(socket.gethostbyname(socket.gethostname()))
        #default tickbox
        self.ui.Server_checkbox.setChecked(True)
    def on_change_state(self, state):
        if state == QtCore.Qt.Checked:
            self.openServer()
        else:
            self.closeServer()

    def closeEvent(self, event):
        self.closeServer()
        super(QMainWindow, self).closeEvent(event)
        
    def openServer(self):
        print("opening server")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostname, self.port))        
        self.running = True
        self.listen = threading.Thread(target=self.listenThread, 
                                       args=(lambda: not self.running, ))
        self.listen.start()
        
    def listenThread(self, stop):
        try:
            self.socket.listen()
            while (True):
                conn, address = self.socket.accept()
                self.conn = conn
                tmp = threading.Thread(target=self.handleCommandThread,
                                       args=(conn, lambda: not self.running, address))
                tmp.start()
        except Exception as e:
            return
        
    def handleCommandThread(self, conn, stop, addr):
        try:
            while (True):
                data = self.recv(conn)
                data = bytes2dict(data)
                if (data["state"] == "MAC"):
                    resData = self.systemHelperPointer.GetMacAddress()
                    self.res(resData.encode(), conn)
                elif (data["state"] == "Logout"):
                    self.systemHelperPointer.Logout()
                elif (data["state"] == "Shutdown"):
                    self.systemHelperPointer.Shutdown()
                elif (data["state"] == "Restart"):
                    self.systemHelperPointer.Restart()
                elif (data["state"] == "Capture"):
                    resData = self.captureHelperPointer.image_to_byte_array(data["quality"])
                    self.res(resData, conn)
                elif (data["state"] == "BackHome"):
                    homeList = self.fileHelperPointer.back_to_drives()
                    listReturn=dict2bytes(homeList)
                    self.res(listReturn, conn)
                elif (data["state"] == "FileHandle"):
                    downOnelevelList = self.fileHelperPointer.Handle(data["path"])
                    listReturn=dict2bytes(downOnelevelList)
                    self.res(listReturn, conn)
                elif (data["state"] == "DeleteFile"):
                    check = self.fileHelperPointer.deleteFile(data["filename"])
                    checkReturn=dict2bytes(check)
                    self.res(checkReturn,conn)
                elif (data["state"] == "UploadFile"):
                    fileData = self.recv(conn)
                    check = self.fileHelperPointer.download(data["filename"], fileData)
                    check = dict2bytes(check)
                    self.res(check, conn)
                elif (data["state"]=="DownloadFile"):
                    myfile=base64.b64decode(data["data"])
                    check=self.fileHelperPointer.receiveFileFromClient(data["filename"], myfile)
                    checkReturn=dict2bytes(check)
                    self.res(checkReturn,conn)
                elif (data["state"]=="Hook"):
                    check=self.keyboardHelperPointer.KeyHook()
                    checkReturn=dict2bytes(check)
                    self.res(checkReturn,conn)
                elif (data["state"]=="Unhook"):
                    check=self.keyboardHelperPointer.Unhook()
                    checkReturn=dict2bytes(check)
                    self.res(checkReturn,conn)
                elif (data["state"]=="Show"):
                    data=self.keyboardHelperPointer.Show()
                    listReturn=dict2bytes(data)
                    self.res(listReturn,conn)
                elif (data["state"]=="Lock"): 
                    check=self.keyboardHelperPointer.BlockKeyBoard()
                    checkReturn=dict2bytes(check)
                    self.res(checkReturn,conn)
                elif (data["state"]=="Unlock"): 
                    check=self.keyboardHelperPointer.UnblockKeyboard()
                    checkReturn=dict2bytes(check)
                    self.res(checkReturn,conn)
                elif (data["state"] == "GetProcesses"):
                    processes_byte_list = dict2bytes(self.process_manager.get_running_processes_list())
                    self.res(processes_byte_list, conn)
                elif (data["state"] == "KillProcess"):
                    data = self.recv(conn)
                    data = bytes2dict(data)
                    process_id = data["process_id"]
                    self.process_manager.kill_process(process_id)
                    self.res(dict2bytes({"message": f'Kill process with id = {process_id} successfully'}), conn)
                elif (data["state"] == "StartProcess"):
                    data = self.recv(conn)
                    data = bytes2dict(data)
                    process_name = data["process_name"]
                    self.process_manager.start_process(process_name)
                    self.res(dict2bytes({"message": f'Start {process_name} successfully'}), conn)
                elif (data["state"] == "GetApps"):
                    apps_byte_list = dict2bytes(self.app_manager.get_running_app_list())
                    self.res(apps_byte_list, conn)

                elif (data["state"] == "KillApp"):
                    data = self.recv(conn)
                    data = bytes2dict(data)
                    app_id = data["app_id"]
                    self.app_manager.kill_app(app_id)
                    self.res(dict2bytes({"message": f'Kill app with id = {app_id} successfully'}), conn)

                elif (data["state"] == "StartApp"):
                    data = self.recv(conn)
                    data = bytes2dict(data)
                    app_name = data["app_name"]
                    self.app_manager.start_app(app_name)
                    self.res(dict2bytes({"message": f'Start {app_name} successfully'}), conn)

                elif (data["state"] == "Sending File"):
                    file_name = self.recv(conn).decode()
                    file_data = self.recv(conn).decode()
                    file = open(file_name, "w")
                    file.write(file_data)
                    file.close()

                    self.registry_manager.import_registry_file(file_name)
                    self.res(dict2bytes({"message": f'Import {file_name} successfully'}), conn)

                
                elif (data["state"] == "GetSubkeyValue"):
                    try:
                        data = self.recv(conn)
                        data = bytes2dict(data)
                        hive = self.registry_manager.get_hive(data["hive"])
                        value = self.registry_manager.get_subkey_value(hive, data["key"], data["subkey"])
                        self.res(dict2bytes({"value": value}), conn)
                    except Exception as e:
                        self.res(dict2bytes({"value": "ERROR"}), conn)

                elif (data["state"] == "SetSubkey"):
                    try:
                        data = self.recv(conn)
                        data = bytes2dict(data)
                        self.registry_manager.set_subkey_value(self.registry_manager.get_hive(
                            data["hive"]), data["key"], data["subkey"], data["value"], data_type=self.registry_manager.get_data_type_number(data["data_type"]))
                        self.res(dict2bytes({"value": "Set subkey successfully"}), conn)
                    except Exception as e:
                        self.res(dict2bytes({"value": "ERROR"}), conn)

                elif data["state"] == "DeleteValue":
                    try:
                        data = self.recv(conn)
                        data = bytes2dict(data)
                        self.registry_manager.delete_subkey(
                            self.registry_manager.get_hive(data["hive"]), data["key"], data["subkey"])
                        self.res(dict2bytes({"value": "Delete subkey successfully"}), conn)
                    except Exception as e:
                        self.res(dict2bytes({"value": "ERROR"}), conn)

                elif data["state"] == "DeleteKey":
                    try:
                        data = self.recv(conn)
                        data = bytes2dict(data)
                        self.registry_manager.delete_key(
                            self.registry_manager.get_hive(data["hive"]), data["key"])
                        self.res(dict2bytes({"value": "Delete key successfully"}), conn)
                    except Exception as e:
                        self.res(dict2bytes({"value": "ERROR"}), conn)

                elif data["state"] == "CreateKey":
                    try:
                        data = self.recv(conn)
                        data = bytes2dict(data)
                        self.registry_manager.create_key(
                            self.registry_manager.get_hive(data["hive"]), data["key"])
                        self.res(dict2bytes({"value": "Create key successfully"}), conn)
                    except Exception as e:
                        self.send_text(conn, "ERROR")
                elif data["state"] == "StartStream":
                    try:
                        ip, port = addr 
                        self.res(dict2bytes({"ip": ip, "port": port}), conn)
    
                        self.stream_server = StreamServer(ip, port)
                        self.stream_server.start_stream()
                    except:
                        return
                elif data["state"] == "StopStream":
                    try:
                        self.stream_server.end_stream()
                    except:
                        return
        except Exception as e:
            return
        
    def closeServer(self):
        if self.conn != None:
            self.conn.close()
        if self.socket != None:
            print("closing server")
            try:
                 self.socket.shutdown(socket.SHUT_RDWR)
            except:
                print("Socket is not connected")
            self.socket.close()
    def res(self, data, conn):
        try:
            conn.sendall(str(len(data)).zfill(12).encode())
            conn.sendall(data)
        except:
            raise Exception('')
    def recv(self, conn):
        try:
            data_size = int(conn.recv(12).decode())
            data = conn.recv(data_size)
            return data
        except:
            raise Exception('')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Server()
    main_win.show()
    sys.exit(app.exec_())
