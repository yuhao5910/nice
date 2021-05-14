from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from mywidget import mywidget
from mybutton import *
from mymenubar import *
from myedit import *
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
    # 用户第一次登录
    try:
        f=open("user.date",'r')
    except:
        text = myTextWidget(widget)
        def saveText():
            f = open("user.date", 'w')
            f.write(text.toPlainText())
            f.close()
        menubar.mysave.triggered.connect(saveText)
    else:
        f.close()

    # 展示主界面
    widget.show()
    sys.exit(app.exec_())



