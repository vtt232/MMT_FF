# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:42:32 2021
@author: DELL
"""

import keyboard

class KeyboardHelper():
    
    def KeyHook(self):
        try:
            keyboard.start_recording()
            return True
        except:
            return False
    
    def Unhook(self):
        try:
            keyboard.stop_recording()
            return True
        except:
            return False
    
    def Show(self):
        try:
            preFix=keyboard.stop_recording()
            postFix=[]
            for i in range(len(preFix)):
                if(preFix[i].event_type=="down"):
                    postFix.append(preFix[i].name)
            keyboard.start_recording()
            return postFix
        except:
            return postFix.append("That bai")
            
        
    def BlockKeyBoard(self):
        try:
            for i in range (150):
                keyboard.block_key(i)
            return True
        except:
            return False

    def UnblockKeyboard(self):
        try:
            for i in range (150):
                keyboard.unblock_key(i)
            return True
        except:
            return False