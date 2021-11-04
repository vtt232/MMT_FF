# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_system.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(138, 181)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Shutdown = QtWidgets.QPushButton(Form)
        self.Shutdown.setObjectName("Shutdown")
        self.verticalLayout.addWidget(self.Shutdown)
        self.Restart = QtWidgets.QPushButton(Form)
        self.Restart.setObjectName("Restart")
        self.verticalLayout.addWidget(self.Restart)
        self.Logout = QtWidgets.QPushButton(Form)
        self.Logout.setObjectName("Logout")
        self.verticalLayout.addWidget(self.Logout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Shutdown.setText(_translate("Form", "Shutdown"))
        self.Restart.setText(_translate("Form", "Restart"))
        self.Logout.setText(_translate("Form", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

