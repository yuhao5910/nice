from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from mywidget import mywidget
from mybutton import *
from mymenubar import *
print("Hello World!")
print("Nice to meet you!")
if __name__=="__main__":
    # 程序入口测试
    app=QApplication(sys.argv)
    # 控件初始化
    widget = mywidget()
    playbtn=myplaybtn(widget)
    endbtn=myendbtn(widget)
    menubar=mymenubar(widget)

    # 展示主界面
    widget.show()
    sys.exit(app.exec_())



