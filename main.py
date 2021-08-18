import PySide6
import PySide6.QtCore
from PySide6 import QtWidgets,QtGui
import sys
from mywidget import mywidget
if __name__=='__main__':
    app=QtWidgets.QApplication([])
    widget=mywidget()
    widget.show()
    sys.exit(app.exec())

