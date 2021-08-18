import sys

from PySide6.QtWidgets import *
class myplaybtn(QPushButton):
    """开始类"""
    def __init__(self,parent=None):
        super(myplaybtn, self).__init__(parent)
        self.setText('play')
        self.move(250,200)
        self.clicked.connect(lambda :print("play"))
class myendbtn(QPushButton):
    """结束类"""
    def __init__(self,parent=None):
        super(myendbtn, self).__init__(parent)
        self.setText('end')
        self.move(250,250)
        self.clicked.connect(lambda : sys.exit())
class mysavebtn(QPushButton):
    def __init__(self,parent=None):
        super(mysavebtn, self).__init__(parent)
        self.setText("确定")
        self.move(360,50)
