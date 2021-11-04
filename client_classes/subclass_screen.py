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


from vidstream import StreamingServer 
from PIL import Image

import sys
import PIL
import io
import time
import os
#threading
import threading
from gui.client.Capture_Stream.client_screen_ui import Ui_screenUI
from gui.popup import PopUp
class Subclass_Screen(QWidget):
    
    def __init__(self, parent = None):
        super(Subclass_Screen, self).__init__()
        self.ui = Ui_screenUI()
        self.ui.setupUi(self)
        
        self.parent = parent
        #Bind
        self.quality = self.ui.QualitySlider.value()
        self.ui.QualitySlider.valueChanged.connect(self.asign)
        self.ui.Capture.clicked.connect(
            self.CaptureScreen)
        self.ui.Save.clicked.connect(
            self.Save)
        self.ui.Stream_button.clicked.connect(
            self.Stream)
        self.ui.Stop_stream_button.clicked.connect(
            self.stopStream)
        self.stop = False
        self.stream = None
        self.img = None
    def asign(self):
        self.quality = self.ui.QualitySlider.value()
    def show(self):
        self.stop = False
        super().show()
    def closeEvent(self, event):
        self.stopStream()
    def image_from_bytes(self, data):
        image = PIL.Image.open(io.BytesIO(data))
        return image
    def decode(self, data): #return a pixmap
        self.img = self.image_from_bytes(data)
        img = self.img.copy()
        
        size = (self.ui.View.width(), self.ui.View.height())
        img.thumbnail(size, Image.ANTIALIAS)
        qim = ImageQt(img)
        
        pixmap = QtGui.QPixmap.fromImage(qim).copy()
        return pixmap    
    def display(self, data):
        self.ui.View.setPixmap(self.decode(data))
    def CaptureScreen(self):
        try:
            self.parent.Command( { "state" : "Capture", "quality" : 
                                  self.ui.QualitySlider.value()} )
            data = self.parent.Recv()
            self.display(data)
        except Exception as e:
            errorMsg = "Cannot capture screen.\n" + str(e)
            PopUp.show_popup(self, "Error", errorMsg,
                           "warning")
    def Save(self):
        if self.img != None:
            filename, _ = QFileDialog.getSaveFileName(
                        self, filter='*.jpg;;*.png;;*.jpeg',
                        directory=os.getenv('HOME'))
            
            if filename:
                self.img.save(filename)
    def Stream(self):
        try:
            self.parent.Command({"state": "StartStream"})
    
            data = self.parent.bytes2dict(self.parent.Recv())
            host, port = data["ip"], data["port"]
            self.stream = StreamingServer(host, port, 1)
    
            self.thread = threading.Thread(target=self.stream.start_server)
            self.thread.start()
        except Exception as e:
            msg = str(e)
            PopUp.show_popup(self, "Error", msg,
                           "warning")
            
    def stopStream(self):
        self.ui.Capture.setEnabled(True)
        self.ui.Save.setEnabled(True)
        try:
            if(self.stream==None):
                return
            self.parent.Command({"state": "StopStream"})
            self.stream.stop_server()
            self.CaptureScreen()
        except Exception as e:
            msg = str(e)
            PopUp.show_popup(self, "Error", msg,
                           "warning")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Subclass_Screen()
    main_win.show()
    sys.exit(app.exec_())