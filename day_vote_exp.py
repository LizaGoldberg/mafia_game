import sys
from idk import *
from seven_to_fourteen import *
from roles_shells import *
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget, QDialog
from PyQt6.QtGui import QFont, QFontDatabase


class NameButton(QPushButton):
    name_clicked = 0

    def __init__(self, a):
        super().__init__()
        self.individual_table = None
        self.name_clicked = a
        self.role_clicked = None



        QFontDatabase.addApplicationFont("TDCyrillic.otf")

        # for i in range(len(blya.all_vars)):
        #     for k in blya.all_vars:
        #         if k.name == self.name_clicked:
        #             self.role_clicked = k.role

        self.setText(a)
        self.setFixedSize(QSize(60, 60))
        self.setStyleSheet("background-color: white; border-radius: 8px; font: 20px")
        self.setFont(QFont("TD Cyrillic"))
        self.move(370, 280)
        self.clicked.connect(self.on_changed)
        self.clicked.connect(self.name_clicked_blya)
        self.clicked.connect(self.show_ind_table)


    def show_ind_table(self):
        self.individual_table = IndividualTable()
        self.individual_table.show()

    def on_changed(self):
        self.setStyleSheet("background-color: black; color: black; border-radius: 8px; font: 50px")  # дизейблится
        # запускаем окно "кого хошь убить"

    def name_clicked_blya(self):
        blya.name_clicked = self.name_clicked


class NameButtonIndividual(QPushButton):
    ability = True

    def __init__(self, a):
        super().__init__()
        self.name_victim = a
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        self.clicked.connect(self.cliiiick)
        if self.clicked.connect(self.cliiiick):
            self.clicked.connect(self.on_changed)
        self.setText(a)
        self.setFixedSize(QSize(60, 60))
        self.setStyleSheet("background-color: white; border-radius: 8px; font: 20px")
        self.setFont(QFont("TD Cyrillic"))
        self.move(370, 280)

    def on_changed(self):
        self.setStyleSheet("background-color: black; color: black; border-radius: 8px; font: 50px")  # дизейблится


    def cliiiick(self):
        if self.ability == True:
            for k in blya.all_vars:
                if k.name == self.name_victim:
                    k.to_vote()
        NameButtonIndividual.ability = False


class NightTable(QMainWindow):  # template for "How many?"

    def __init__(self):
        super().__init__()

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        layout = QGridLayout()
        x = 0
        y = 0
        for i in range(len(blya.all_vars)):
            for k in blya.all_vars:
                if blya.all_vars[i].name == k.name and k.status != 'dead':
                    layout.addWidget(NameButton(blya.all_vars[i].name), x, y)
            if x < int(blya.nn ** 0.5):
                x += 1
            else:
                y += 1
                x = 0

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")


class IndividualTable(QMainWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        layout = QGridLayout()
        x = 0
        y = 0
        for i in range(len(blya.all_vars)):
            for k in blya.all_vars:
                if blya.all_vars[i].name == k.name and k.status != 'dead' and blya.all_vars[i].name != blya.name_clicked:
                    layout.addWidget(NameButtonIndividual(blya.all_vars[i].name), x, y)
            if x < int(blya.nn ** 0.5):
                x += 1
            else:
                y += 1
                x = 0

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")


app = QApplication(sys.argv)

window = NightTable()
window.show()

app.exec()