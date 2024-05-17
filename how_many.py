import sys

from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from PyQt6.QtGui import QFont, QFontDatabase

class Howmany(QMainWindow): #template for "How many?"
    def __init__(self):
        super().__init__()

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        self.enter = QLineEdit(self)
        self.enter.setFixedSize(QSize(40, 45))
        self.enter.setStyleSheet("background-color: white; border-radius: 8px; font: 50px")
        self.enter.setFont(QFont("TD Cyrillic"))
        self.enter.move(320, 280)

        self.submit = QPushButton("ввод", self)
        self.submit.setFixedSize(QSize(40, 45))
        self.submit.setStyleSheet("background-color: white; border-radius: 8px; font: 50px")
        self.submit.setFont(QFont("TD Cyrillic"))
        self.submit.move(370, 280)
        self.submit.clicked.connect(self.on_changed)

        self.number = QLabel("Сколько игроков?", self)
        self.number.move(135, 154)
        self.number.setStyleSheet("color: white; font: 70px")
        self.number.setFont(QFont("TD Rukopis"))
        self.number.adjustSize()

        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")

    def on_changed(self):
        self.submit.setStyleSheet("background-color: black; color: white; border-radius: 8px; font: 50px")
        #запускаем окно "как тебя зовут"
        return (self.enter.text()) #возвращает число игроков



app = QApplication(sys.argv)

window = Howmany()
window.show()

app.exec()