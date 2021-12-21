from PyQt5.QtCore import QSignalMapper
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import pyqtSignal as QSignal

class ClickableLabel(QLabel):
    clicked = QSignal(str)

    def __init__(self, width, height, color):
        super(ClickableLabel, self).__init__()

    def mousePressEvent(self, event):
        self.clicked.emit(self.objectName())
