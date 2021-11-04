from gui.client.FileExplorer.client_fileExplorer import Ui_File_ui

from collections import namedtuple
import sys
import os
import shutil

from datetime import datetime
from os.path import abspath
from base64 import b64encode
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from pathlib import Path
from gui.popup import PopUp
from PyQt5.QtWidgets import QFileDialog


class Subclass_File(QWidget):
      
    #TAO GUI
    def __init__(self, parent = None):
        super(Subclass_File, self).__init__()
        self.ui = Ui_File_ui()
        self.ui.setupUi(self)
        
        self.parent = parent
        #bind
        
        self.ui.Del.clicked.connect(lambda: self.delete())      
        self.ui.content.doubleClicked.connect(lambda : 
                                       self.item_doubleClicked())
        self.ui.Reload.clicked.connect(lambda: self.Handle(str(self.currentPath)))
        self.ui.Back.clicked.connect(self.BackToParent)
        self.ui.pathEdit.returnPressed.connect(lambda: self.Handle(self.ui.pathEdit.text()))
        self.ui.Upload.clicked.connect(self.Upload)
        self.ui.Home.clicked.connect(self.BackHome)
        
        #setup
        self.currentPath =  None
        self.data = None
    def GetParentPath(self, path):
        respath = Path(path)
        return (respath.parent.absolute())
    def BackToParent(self):
        self.Handle(self.GetParentPath(self.currentPath))
    def Upload(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", 
                                                      options=options)            
            if not fileName:
                return
            filesize=int(os.path.getsize(fileName))
            with open(fileName, 'rb') as f:
                bytesToSend = f.read(filesize)
            destFileName = str(Path(os.path.join(self.currentPath, Path(fileName).name)))
            self.parent.Command({"state" : "UploadFile", "filename" : destFileName})
            self.parent.Send(bytesToSend)
            resData = self.parent.bytes2dict(self.parent.Recv())
            PopUp.show_popup(self, "Information", 
                             resData["msg"])
            self.Handle(str(self.currentPath))
        except Exception as e:
           msg = "Cannot upload file.\n" + str(e)
           PopUp.show_popup(self, "Error", msg, 
                            "critical")
    def BackHome(self):
        try:
            self.parent.Command({"state" : "BackHome"})
            resData = self.parent.bytes2dict(self.parent.Recv())
            if (resData["status"] == "success"):
                self.data = resData["paths"]
                self.insert_data(self.data)
                self.currentPath  = Path("")
                self.ui.pathEdit.setText(str(self.currentPath))
            elif (resData["status"] == "failed"):
                PopUp.show_popup(self, "Error", 
                             resData["msg"], 
                             "warning")
        except Exception as e:
            msg = "Cannot go back home.\n" + str(e)
            PopUp.show_popup(self, "Error", 
                             msg, 
                             "critical")
    def Handle(self, pathName):
        try:
            path = Path(pathName)
            self.parent.Command({"state" : "FileHandle", "path" : str(path)})
            resData = self.parent.bytes2dict(self.parent.Recv())
            if (resData["status"] == "success"):
                self.data = resData["paths"]                
                self.insert_data(self.data)

                self.currentPath  = path
                self.ui.pathEdit.setText(str(self.currentPath))
            elif (resData["status"] == "failed"):
                PopUp.show_popup(self, "Error", 
                             resData["msg"], 
                             "warning")
        except Exception as e:
            msg = "Cannot go to destinatio.\n" + str(e)
            PopUp.show_popup(self, "Error", 
                             msg, 
                             "critical")
    def delete(self):
        try:
            filename = self.data[self.ui.content.currentRow()][0]
            filename = Path(os.path.join(self.currentPath, filename))
            self.parent.Command({"state" : "DeleteFile", "filename" : str(filename)})
            resData = self.parent.bytes2dict(self.parent.Recv())
            PopUp.show_popup(self, "Information", 
                             resData["msg"], )
            self.Handle(str(self.currentPath))
        except Exception as e:
            msg = "Cannot delete file.\n" + str(e)
            PopUp.show_popup(self, "Error", 
                             msg, 
                             "critical")
    def insert_data(self, data):
        self.clear_data()
        for i in range(len(data)):
            self.ui.content.insertRow(i)
            for j in range(len(data[i])):
                if (j == 0 and data[i][3] == False):
                    itemContent =  QTableWidgetItem("📁" + str(data[i][j]))
                else:
                    itemContent = QTableWidgetItem(str(data[i][j]))
                self.ui.content.setItem(i, j, itemContent)
    def clear_data(self):
        self.ui.content.setRowCount(0)
    def item_doubleClicked(self):
        if (self.data[self.ui.content.currentRow()][3] == False):
            name = self.data[self.ui.content.currentRow()][0].replace("📁", "")
        else:
            name = self.data[self.ui.content.currentRow()][0]
        proposedPath = Path(os.path.join(self.currentPath, name))
        self.Handle(proposedPath)
#Kich hoat
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Subclass_File()
    main_win.show()
    sys.exit(app.exec_())