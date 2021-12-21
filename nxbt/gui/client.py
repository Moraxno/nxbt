import sys
from threading import Thread
from time import sleep
from PyQt5.QtWidgets import QApplication, QMainWindow

from main import Ui_MainWindow

def sneaky(wind):
    sleep(5)
    wind.ui.lbl_connected.setText("I am sneaky")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

Thread(target=lambda: sneaky(window)).start()



sys.exit(app.exec())