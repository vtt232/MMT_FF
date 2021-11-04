# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_capture_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_screenUI(object):
    def setupUi(self, screenUI):
        screenUI.setObjectName("screenUI")
        screenUI.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(screenUI.sizePolicy().hasHeightForWidth())
        screenUI.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(screenUI)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.View = QtWidgets.QLabel(screenUI)
        self.View.setText("")
        self.View.setObjectName("View")
        self.horizontalLayout.addWidget(self.View)
        self.groupBox_3 = QtWidgets.QGroupBox(screenUI)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.QualitySlider = QtWidgets.QSlider(self.groupBox_3)
        self.QualitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.QualitySlider.setObjectName("QualitySlider")
        self.verticalLayout_4.addWidget(self.QualitySlider)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Capture = QtWidgets.QPushButton(self.groupBox)
        self.Capture.setObjectName("Capture")
        self.verticalLayout_3.addWidget(self.Capture)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Stream_button = QtWidgets.QPushButton(self.groupBox_2)
        self.Stream_button.setObjectName("Stream_button")
        self.verticalLayout_2.addWidget(self.Stream_button)
        self.Stop_stream_button = QtWidgets.QPushButton(self.groupBox_2)
        self.Stop_stream_button.setObjectName("Stop_stream_button")
        self.verticalLayout_2.addWidget(self.Stop_stream_button)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FPS = QtWidgets.QLabel(self.groupBox_5)
        self.FPS.setObjectName("FPS")
        self.horizontalLayout_3.addWidget(self.FPS)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.Save = QtWidgets.QPushButton(self.groupBox_3)
        self.Save.setObjectName("Save")
        self.verticalLayout_4.addWidget(self.Save)
        spacerItem = QtWidgets.QSpacerItem(20, 284, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(screenUI)
        QtCore.QMetaObject.connectSlotsByName(screenUI)

    def retranslateUi(self, screenUI):
        _translate = QtCore.QCoreApplication.translate
        screenUI.setWindowTitle(_translate("screenUI", "Form"))
        self.groupBox_3.setTitle(_translate("screenUI", "Functions"))
        self.groupBox.setTitle(_translate("screenUI", "Image"))
        self.Capture.setText(_translate("screenUI", "Capture"))
        self.groupBox_2.setTitle(_translate("screenUI", "Stream"))
        self.Stream_button.setText(_translate("screenUI", "Stream"))
        self.Stop_stream_button.setText(_translate("screenUI", "Stop stream"))
        self.groupBox_5.setTitle(_translate("screenUI", "FPS"))
        self.FPS.setText(_translate("screenUI", "None"))
        self.Save.setText(_translate("screenUI", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screenUI = QtWidgets.QWidget()
    ui = Ui_screenUI()
    ui.setupUi(screenUI)
    screenUI.show()
    sys.exit(app.exec_())

