import sys

from mafia.globall import blya, get_all_vars, get_number_players
from roles_shells import *
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget, QDialog
from PyQt6.QtGui import QFont, QFontDatabase


class Peasant_night(QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        with open('peasant.txt', 'r', encoding="utf-8") as file:
            array = [row.strip() for row in file]
        self.label = QLabel(random.choice(array), self)
        self.label.setStyleSheet("color: white")
        self.label.adjustSize()


class NameButton(QPushButton):
    name_clicked = 0

    def __init__(self, a):
        super().__init__()
        self.individual_table = None
        self.name_clicked = a
        self.role_clicked = None
        self.counter = None
        self.peasant_night = Peasant_night(self)


        QFontDatabase.addApplicationFont("TDCyrillic.otf")

        for i in range(len(get_all_vars())):
            for k in get_all_vars():
                if k.name == self.name_clicked:
                    self.role_clicked = k.role

        self.setText(a)
        self.setFixedSize(QSize(60, 60))
        self.setStyleSheet("background-color: white; border-radius: 8px; font: 40px")
        self.setFont(QFont("TD Cyrillic"))
        self.move(370, 280)
        self.clicked.connect(self.on_changed)
        self.clicked.connect(self.name_clicked_blya)
        if self.role_clicked != 'Peasant':
            self.clicked.connect(self.show_ind_table)
        else:
            self.clicked.connect(self.peasant_night.open)


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
        self.setStyleSheet("background-color: white; border-radius: 8px; font: 40px")
        self.setFont(QFont("TD Cyrillic"))
        self.move(370, 280)

    def on_changed(self):
        self.setStyleSheet("background-color: black; color: black; border-radius: 8px; font: 50px")  # дизейблится


    def cliiiick(self):
        if self.ability == True:
            for i in range(len(get_all_vars())):
                for k in get_all_vars():
                    if k.name == self.name_victim:
                        if get_all_vars()[i].name == blya.name_clicked:
                            if get_all_vars()[i].role == 'Healer':
                                get_all_vars()[i].to_heal(k)
                            if get_all_vars()[i].role == 'Priest':
                                get_all_vars()[i].active_or_not(k)
                            if get_all_vars()[i].role == 'Dyak':
                                get_all_vars()[i].find_what_role(k)
                            if get_all_vars()[i].role == 'GirlX':
                                get_all_vars()[i].to_block(k)
                            if get_all_vars()[i].role == 'Boyar':
                                get_all_vars()[i].inherit(k)
                            if get_all_vars()[i].role == 'Oprich':
                                get_all_vars()[i].to_kill(k)

        NameButtonIndividual.ability = False


class NightTable(QMainWindow):  # template for "How many?"
    def __init__(self):
        super().__init__()
        self.individual_table = None

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        layout = QGridLayout()
        x = 0
        y = 0
        z = 0
        for i in range(len(get_all_vars())):
            for k in get_all_vars():
                print(get_all_vars())
                print(get_all_vars()[i].name)
                try:
                    if get_all_vars()[i].name == k.name and k.status != 'dead':
                        layout.addWidget(NameButton(get_all_vars()[i].name), x, y)
                        z += 1
                except Exception as error:
                    print(error)
                    print("pizdec")

            if x < int(get_number_players() ** 0.5):
                x += 1
            else:
                y += 1
                x = 0
        blya.max_alive = z

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
        for i in range(len(get_all_vars())):
            for k in get_all_vars():
                if get_all_vars()[i].name == k.name and k.status != 'dead' and get_all_vars()[i].name != blya.name_clicked:
                    layout.addWidget(NameButtonIndividual(get_all_vars()[i].name), x, y)
            if x < int(get_number_players() ** 0.5):
                x += 1
            else:
                y += 1
                x = 0

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")
