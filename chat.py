# starting with  https://build-system.fman.io/python-qt-tutorial

from PySide2.QtWidgets import *

app = QApplication([])
layout = QVBoxLayout()
layout.addWidget(QTextEdit())
layout.addWidget(QLineEdit())
window = QWidget()
window.setLayout(layout)
window.show()
app.exec_()



# import PySide2.QtWidgets as qw 


# app = qw.QApplication([])
# text_area = qw.QTextEdit()
# text_area.show()