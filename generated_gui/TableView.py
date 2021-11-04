# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 338)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.view_button = QtWidgets.QPushButton(Form)
        self.view_button.setObjectName("view_button")
        self.verticalLayout.addWidget(self.view_button)
        self.clear_button = QtWidgets.QPushButton(Form)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout.addWidget(self.clear_button)
        self.kill_button = QtWidgets.QPushButton(Form)
        self.kill_button.setObjectName("kill_button")
        self.verticalLayout.addWidget(self.kill_button)
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Process"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Thread Count"))
        self.view_button.setText(_translate("Form", "View"))
        self.clear_button.setText(_translate("Form", "Clear"))
        self.kill_button.setText(_translate("Form", "Kill"))
        self.start_button.setText(_translate("Form", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

