from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

input1 = QLineEdit()
input2 = QLineEdit()
button = QPushButton("result")

mainLine = QVBoxLayout()
mainLine.addWidget(input1)
mainLine.addWidget(input2)



window.setLayout(mainLine)
window.show()
app.exec_()