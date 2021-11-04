# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_keyboard_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Keyboard(object):
    def setupUi(self, Keyboard):
        Keyboard.setObjectName("Keyboard")
        Keyboard.resize(531, 385)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Keyboard)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Keyboard)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.hook_button = QtWidgets.QPushButton(Keyboard)
        self.hook_button.setObjectName("hook_button")
        self.verticalLayout.addWidget(self.hook_button)
        self.unhook_button = QtWidgets.QPushButton(Keyboard)
        self.unhook_button.setObjectName("unhook_button")
        self.verticalLayout.addWidget(self.unhook_button)
        self.show_button = QtWidgets.QPushButton(Keyboard)
        self.show_button.setObjectName("show_button")
        self.verticalLayout.addWidget(self.show_button)
        self.lock_button = QtWidgets.QPushButton(Keyboard)
        self.lock_button.setObjectName("lock_button")
        self.verticalLayout.addWidget(self.lock_button)
        self.unlock_button = QtWidgets.QPushButton(Keyboard)
        self.unlock_button.setObjectName("unlock_button")
        self.verticalLayout.addWidget(self.unlock_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 8)

        self.retranslateUi(Keyboard)
        QtCore.QMetaObject.connectSlotsByName(Keyboard)

    def retranslateUi(self, Keyboard):
        _translate = QtCore.QCoreApplication.translate
        Keyboard.setWindowTitle(_translate("Keyboard", "Form"))
        self.hook_button.setText(_translate("Keyboard", "Hook"))
        self.unhook_button.setText(_translate("Keyboard", "Unhook"))
        self.show_button.setText(_translate("Keyboard", "Show"))
        self.lock_button.setText(_translate("Keyboard", "Lock"))
        self.unlock_button.setText(_translate("Keyboard", "Unlock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Keyboard = QtWidgets.QWidget()
    ui = Ui_Keyboard()
    ui.setupUi(Keyboard)
    Keyboard.show()
    sys.exit(app.exec_())

