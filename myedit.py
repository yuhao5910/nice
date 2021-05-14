from PyQt5.QtWidgets import *
class myTextWidget(QTextEdit):
    """文本窗口"""
    def __init__(self,parent=None):
        super(myTextWidget, self).__init__(parent)
        self.setFixedSize(100,75)
        self.move(250,50)
