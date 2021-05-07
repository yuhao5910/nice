from PyQt5.QtWidgets import *
class mymenubar(QMenuBar):
    def __init__(self,parent=None):
        super(mymenubar, self).__init__(parent)
        myfile = self.addMenu("文件(F)")
        myedit = self.addMenu("编辑(E)")
        myfile.addAction("新建(N)")
        myfile.addAction("打开(O)")
        myfile.addAction("保存(S)")


