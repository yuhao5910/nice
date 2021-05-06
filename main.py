from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import widget
print("Hello World!")
print("Nice to meet you!")
if __name__=="__main__":
    app=QApplication(sys.argv)
    widget = QWidget()
    widget.setWindowTitle("nice")
    widget.setWindowIcon(QIcon("img/girl_0.jpg"))
    widget.setFixedSize(600, 500)
    playbtn=QPushButton("Play",widget)
    endbtn=QPushButton("end",widget)
    playbtn.move(250,200)
    endbtn.move(250,250)
    widget.show()
    sys.exit(app.exec_())



