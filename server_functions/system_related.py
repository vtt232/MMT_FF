from uuid import getnode as get_mac
import os

class SystemHelper:
    def GetMacAddress(self):
        mac = get_mac()
        return hex(mac)
    def Shutdown(self):
        os.system("shutdown -s -t 1")
    def Logout(self):
         os.system("shutdown -l")
    def Restart(self):
        os.system("shutdown -r -t  1")