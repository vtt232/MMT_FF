import os
import shutil
import string

from ctypes import windll
from pathlib import Path
from collections import namedtuple
from datetime import datetime
DataTuple = namedtuple('Data', ['name', 'date',
                                        'size', 'type' ])
class FileHelper:
    def __init__(self):
        return
    def get_drives(self):
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter+":\\")
            bitmask >>= 1
        return drives
    def back_to_drives(self):
        try:
            folders =[]
            for i in self.get_drives():
                folders.append([i, None, None, False]) # not file
            return {"status" : "success", "msg" : ".",
                    "paths" : folders}
        except Exception as e:
             return {"status" : "failed", "msg" : str(e)}
    def download(self, filename, data):
        try:
            with open(filename, "wb") as f:
                f.write(data)
                return {"status" : "success", "msg" : f"{filename} created"}
        except Exception as e:
            return {"status" : "failed", "msg" : str(e)}
    def deleteFile(self, filename):
        try:
            if os.path.isfile(filename):
                os.unlink(filename)
            elif os.path.isdir(filename):
                shutil.rmtree(filename)
            return {"status" : "success", "msg" : f"{filename} deleted"}
        except Exception as e:
            return {"status" : "failed", "msg" : str(e)}
    def Handle(self, pathName):
        try:
            path = Path(pathName) #Path(self.ui.pathEdit.text())
            if (not os.path.exists(path)):
                return {"status" : "failed", "msg" : "Path not existed or cannot access"}
            if (os.path.isfile(path)):
                return {"status" : "failed", "msg" : "Not a folder"}
            data = []
            folders = []
            files = [] 
            for i in os.listdir(path):
                curpath = os.path.join(path , i)
                curpath = Path(curpath)
                time = datetime.fromtimestamp(os.path.getmtime(curpath)).strftime('%d-%m-%Y-%H:%M')
                isFile = os.path.isfile(curpath)
                if not isFile: 
                    size = 0
                    folders.append(DataTuple(i, time, size, isFile))
                else:
                    size = os.path.getsize(curpath)
                    files.append(DataTuple(i, time, size, isFile))
            data = folders + files
            return {"status" : "success", "msg" : ".",
                    "paths" : data}
        except Exception as e:
             return {"status" : "failed", "msg" : str(e)}