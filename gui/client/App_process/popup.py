from PyQt5.QtWidgets import QMessageBox


class PopUp:
    def __init__(self, title, text, popup_type="information"):
        self.title = title
        self.text = text
        self.type = popup_type

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle(self.title)
        msg.setText(self.text)
        icon = QMessageBox.Information
        if self.type == "critical":
            icon = QMessageBox.Critical
        elif self.type == "warning":
            icon = QMessageBox.Warning
        elif self.type == "question":
            icon = QMessageBox.Question
        msg.setIcon(icon)
        msg.exec_()
