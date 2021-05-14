from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class mywidget(QWidget):
    """窗口类"""
    def __init__(self):
        super(mywidget, self).__init__()
        self.setWindowTitle("nice")
        self.setWindowIcon(QIcon("img/girl_0.jpg"))
        self.setFixedSize(600,500)
