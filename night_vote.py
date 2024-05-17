import sys

from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PyQt6.QtGui import QFont, QFontDatabase

class NameButton(QPushButton):
    def __init__(self, player):
        super().__init__()

        QFontDatabase.addApplicationFont("TDCyrillic.otf")

        self.setText(player)
        self.setFixedSize(QSize(60, 60))
        self.setStyleSheet("background-color: white; border-radius: 8px; font: 20px")
        self.setFont(QFont("TD Cyrillic"))
        self.move(370, 280)
        self.clicked.connect(self.on_changed)

    def on_changed(self):
        self.setStyleSheet("background-color: black; color: black; border-radius: 8px; font: 50px") #дизейблится
        # запускаем окно "кого хошь убить"


class NightTable(QMainWindow): #template for "How many?"
    def __init__(self):
        super().__init__()

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        layout = QGridLayout()
        number_of_players = 11 # как-то его получаем
        x = 0
        y = 0
        for i in range (number_of_players):
            layout.addWidget(NameButton("лиза"+str(i)),x,y) # из списка с именами
            if x < int(number_of_players**0.5):
                x+=1
            else:
                y+=1
                x=0

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")



app = QApplication(sys.argv)

window = NightTable()
window.show()

app.exec()