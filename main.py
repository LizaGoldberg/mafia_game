import sys
import random

import menu
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QFont, QFontDatabase, QPixmap


from mafia import globall, night_vote
from mafia import how_many
from mafia.globall import get_roles_players, get_names_players, set_roles_players, append_names_players, blya, \
    set_all_vars, get_all_vars, set_number_players
from mafia.night_vote import NightTable


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
            set_number_players(self.howmany.players_number)
        #print(get_roles_players())  # !!
        #print(get_all_vars())
        self.whatname.submit.clicked.connect(self.show_yourrole)
        self.whatname.submit.clicked.connect(self.whatname.close)
        self.whatname.show()

    def show_yourrole(self):
        self.yourrole = Yourrole()
        append_names_players(self.whatname.names_players[0])
        if len(get_names_players()) < self.howmany.players_number:
            self.yourrole.submit.clicked.connect(self.show_whatname)
            self.yourrole.submit.clicked.connect(self.yourrole.close)
            self.yourrole.show()
        elif len(get_names_players()) == self.howmany.players_number:
            self.yourrole.submit.clicked.connect(self.show_night_vote)
            self.yourrole.submit.clicked.connect(self.yourrole.close)
            set_all_vars()
            print("YESSSS")
            print(get_all_vars()[0])
            print(get_all_vars()[0].name)
            try:
                self.yourrole.show()
            except Exception as error:
                print(error)

    def show_night_vote(self):
        try:
            self.nighttable = NightTable()
            self.nighttable.show()
        except Exception as error:
            print(error)




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
    w = MainWindow()
    w.show()
    w.show_menu()
    sys.exit(app.exec())
