from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from mywidget import mywidget
from mybutton import *
print("Hello World!")
print("Nice to meet you!")
if __name__=="__main__":
    # 程序入口
    app=QApplication(sys.argv)
    # 控件初始化
    widget = mywidget()
    playbtn=myplaybtn(widget)
    endbtn=myendbtn(widget)
    # 展示主界面
    widget.show()
    sys.exit(app.exec_())



