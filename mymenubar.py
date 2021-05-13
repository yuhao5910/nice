from PyQt5.QtWidgets import *
class mymenubar(QMenuBar):
    """菜单类"""
    def __init__(self,parent=None):
        super(mymenubar, self).__init__(parent)
        myfile = self.addMenu("文件(F)")
        myedit = self.addMenu("编辑(E)")
        mynew=myfile.addAction("新建(N)")
        myopen=myfile.addAction("打开(O)")
        mysave=myfile.addAction("保存(S)")
        myedit.addAction("剪切(T)")
        myedit.addAction("复制(C)")

        """功能实现"""
        mynew.triggered.connect(lambda :print("新建"))
        myopen.triggered.connect(lambda: print("打开"))
        mysave.triggered.connect(lambda: print("保存"))


