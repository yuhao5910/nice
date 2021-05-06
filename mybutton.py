from PyQt5.QtWidgets import *
class myplaybtn(QPushButton):
    def __init__(self,parent=None):
        super(myplaybtn, self).__init__(parent)
        self.setText('play')
        self.move(250,200)
class myendbtn(QPushButton):
    def __init__(self,parent=None):
        super(myendbtn, self).__init__(parent)
        self.setText('end')
        self.move(250,250)
