from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDialog

class PopUp:
    @staticmethod
    def show_popup(parent, title, text, popup_type = "information", closeParent = False):
        msg = QMessageBox(parent)
        msg.setWindowTitle(title)
        msg.setText(text)

        icon = QMessageBox.Information
        if popup_type == "critical":
            icon = QMessageBox.Critical
        elif popup_type == "warning":
            icon = QMessageBox.Warning
        elif popup_type == "question":
            icon = QMessageBox.Question
        msg.setIcon(icon)
        msg.exec_()
        if closeParent:
            parent.close()
