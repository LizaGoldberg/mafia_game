import sys
import random

import menu
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget, QDialog, \
    QVBoxLayout
from PyQt6.QtGui import QFont, QFontDatabase, QPixmap

from mafia import how_many
from mafia.drafts import night_vote
from mafia.seven_to_fourteen import what_role


class Whatname(QMainWindow):  # template for "What's your name?"
    def __init__(self):
        super().__init__()

        self.names_players = []  # список имен

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        self.enter = QLineEdit(self)
        self.enter.setFixedSize(QSize(80, 45))
        self.enter.setStyleSheet("background-color: white; border-radius: 8px; font: 50px")
        self.enter.setFont(QFont("TD Cyrillic"))
        self.enter.move(280, 280)

        self.submit = QPushButton("ввод", self)
        self.submit.setFixedSize(QSize(40, 45))
        self.submit.setStyleSheet("background-color: white; border-radius: 8px; font: 50px")
        self.submit.setFont(QFont("TD Cyrillic"))
        self.submit.move(370, 280)
        self.submit.clicked.connect(self.on_changed)

        self.number = QLabel("Как Вас зовут?", self)
        self.number.move(145, 154)
        self.number.setStyleSheet("color: white; font: 70px")
        self.number.setFont(QFont("TD Rukopis"))
        self.number.adjustSize()

        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")

    def on_changed(self):
        self.submit.setStyleSheet("background-color: black; color: white; border-radius: 8px; font: 50px")
        self.names_players.append(self.enter.text())


class Yourrole(QMainWindow):  # template for "Your role is..."
    def __init__(self):
        super().__init__()

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        layout = QVBoxLayout()

        string_role = "Ваша роль: " + self.what_role2()  # должна быть функция говорящая кто игрок
        self.number = QLabel(string_role, self)
        self.number.setStyleSheet("color: white; font: 70px")
        self.number.setFont(QFont("TD Rukopis"))
        self.number.adjustSize()
        self.number.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.number)

        image_path = "pictures/" + self.what_role() + ".png"  # в зависимости от определяемой роли получ картинку
        self.image = QLabel(self)
        pixmap = QPixmap(image_path)
        pixmap4 = pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio,
                                Qt.TransformationMode.SmoothTransformation)
        self.image.setPixmap(pixmap4)
        # self.image.setScaledContents(True)
        self.image.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.image)

        self.submit = QPushButton("окей", self)
        self.submit.setFixedSize(QSize(40, 45))
        self.submit.setStyleSheet("background-color: white; border-radius: 8px; font: 50px")
        self.submit.setFont(QFont("TD Cyrillic"))
        self.submit.clicked.connect(self.on_changed)
        connect_box = QVBoxLayout(self)
        connect_box.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        connect_box.addWidget(self.submit, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(connect_box)

        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_changed(self):
        self.submit.setStyleSheet("background-color: black; color: white; border-radius: 8px; font: 50px")
        # запускаем приветствие

    def what_role(self):
        role = get_roles_players()
        return role[(len(get_names_players()) - 1)]

    def what_role2(self):
        if self.what_role() == "Oprich":
            return "опричник"
        elif self.what_role() == "Boyar":
            return "боярин"
        elif self.what_role() == "Dyak":
            return "дьяк"
        elif self.what_role() == "GirlX":
            return "распутница"
        elif self.what_role() == "Healer":
            return "знахарь"
        elif self.what_role() == "Peasant":
            return "крестьянин"
        else:
            return "священник"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.nightvote = None
        self.yourrole = None
        self.whatname = None
        self.howmany = None
        self.menuw = None

        self.setWindowTitle('MainWindow')

    def show_menu(self):
        self.menuw = menu.Menuwindow()
        self.menuw.begin.clicked.connect(self.show_howmany)
        self.menuw.begin.clicked.connect(self.menuw.close)
        self.menuw.show()
        self.close()

    def show_howmany(self):
        self.howmany = how_many.Howmany()
        self.howmany.submit.clicked.connect(self.show_whatname)  # здесь запустить цикл
        self.howmany.submit.clicked.connect(self.howmany.close)
        self.howmany.show()

    # def show_hellos(self):
    # for i in range (self.howmany.players_number-1):
    # self.show_whatname()

    def show_whatname(self):
        self.whatname = Whatname()
        if len(get_roles_players()) == 0:
            set_roles_players(decide_roles(self.howmany.players_number))
        global number_players
        number_players = self.howmany.players_number
        print(get_roles_players())  # !!
        self.whatname.submit.clicked.connect(self.show_yourrole)
        self.whatname.submit.clicked.connect(self.whatname.close)
        self.whatname.show()

    def show_yourrole(self):
        self.yourrole = Yourrole()
        append_names_players(self.whatname.names_players[0])
        if len(get_names_players()) < self.howmany.players_number:
            self.yourrole.submit.clicked.connect(self.show_whatname)
            self.yourrole.submit.clicked.connect(self.yourrole.close)
        else:
            self.yourrole.submit.clicked.connect(self.show_night_vote)
            self.yourrole.submit.clicked.connect(self.yourrole.close)
        self.yourrole.show()

    def show_night_vote(self):
        self.nightvote = night_vote.NightTable()
        self.nightvote.show()


class blya():
    def method(self):
        self.nn = get_number_players()
        self.aa = get_roles_players()
        self.all_vars = get_all_vars()


def get_number_players():
    global number_players
    return number_players


def get_names_players():
    global names_players
    return names_players


def get_roles_players():
    global roles_players
    return roles_players


def append_names_players(m):
    global names_players
    names_players.append(m)


def set_roles_players(m):
    global roles_players
    roles_players = m


def get_all_vars():
    global all_vars
    n = get_number_players()
    a = get_roles_players()
    c = create_dict()
    if n >= 7:
        player1 = None
        player1 = what_role(a, 0, player1, c)
        all_vars.append(player1)
        player2 = None
        player2 = what_role(a, 1, player2, c)
        all_vars.append(player2)
        player3 = None
        player3 = what_role(a, 2, player3, c)
        all_vars.append(player3)
        player4 = None
        all_vars.append(player4)
        player5 = None
        player5 = what_role(a, 4, player5, c)
        all_vars.append(player5)
        player6 = None
        player6 = what_role(a, 5, player6, c)
        all_vars.append(player6)
        player7 = None
        player7 = what_role(a, 6, player7, c)
        all_vars.append(player7)
        if n >= 8:
            player8 = None
            player8 = what_role(a, 7, player8, c)
            all_vars.append(player8)
            if n >= 9:
                player9 = None
                player9 = what_role(a, 8, player9, c)
                all_vars.append(player9)
                if n >= 10:
                    player10 = None
                    player10 = what_role(a, 9, player10, c)
                    all_vars.append(player10)
                    if n >= 11:
                        player11 = None
                        player11 = what_role(a, 10, player11, c)
                        all_vars.append(player11)
                        if n >= 12:
                            player12 = None
                            player12 = what_role(a, 11, player12, c)
                            all_vars.append(player12)


def create_dict():
    c = {}
    for i in get_names_players():
        for j in get_roles_players():
            c[str(i)] = str(j)
    return c


def decide_roles(n):
    with open('roles.txt', 'r') as f:
        i = 0
        b = []
        while i < n:
            b.append(f.readline().strip())
            i = i + 1
    random.shuffle(b)
    return b


if __name__ == '__main__':
    app = QApplication(sys.argv)
    roles_players = []
    names_players = []
    all_vars = []
    number_players = 0
    w = MainWindow()
    w.show()
    w.show_menu()
    sys.exit(app.exec())
