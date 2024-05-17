import sys

from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QDialog
from PyQt6.QtGui import QFont, QFontDatabase


# Подкласс QMainWindow для настройки главного окна приложения

class Rules(QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root
        self.label = QLabel('Правила игры:\nВ игре друг другу противостоят два лагеря: опричники и мирные жители. Игра '
                       'рассчитана на 7-14 игроков. Перед началом вы можете прочитать историческую справку, '
                       'задающую контекст событий.\nВ начале игры вам будет предложено ввести количество игроков. '
                       'Далее каждому игроку предлагается по очереди ввести свое имя, сразу после этого ему будет '
                       'выдана одна из ролей.\n\nРоли в игре:\n\nОпричники:\n 1 Опричники- аналог мафии. Ночью '
                       'выбирают жертву, голосуя за одного из игроков. Если голоса разделились, жертва выбирается '
                       'случайным образом\nПри количестве от 11 игроков вы можете выбрать одну из дополнительных '
                       'ролей, при количестве от 13 игроков задействованы обе роли\n\nМирные жители:\n1 Знахарь- '
                       'ночью может спасти одного игрока на выбор от смерти, не может лечить одного игрока дважды\n2 '
                       'Дьяк- ночью может узнать роль одного игрока\n3 Священник- ночью может узнать про одного '
                       'игрока, активная у него роль или нет (крестьянин)\n4 Распутная девка- ночью может посетить '
                       'одного игрока, тем самым заблокировав его действие, если он активный, также он не может '
                       'участвовать в обсуждении днем и голосовать\n5 Крестьянин- мирный житель, не имеющий '
                       'специальных функций\n6 Боярин- мирный житель, после смерти оставляет наследство- иммунитет на '
                       'одну ночь и один день для любого игрока на выбор\n\nКоличество опричников и крестьян '
                       'определяется количеством игроков\n\nС уходом ночи публикуются события, произошедшие с '
                       'игроками, роли убитых вскрываются\n\nДнем игрокам предлагается высказаться по очереди, '
                       'далее дается время на общее обсуждение, а в конце дня игроки по очереди голосуют, игрок, '
                       'набравший наибольшее количество голосов, выбывает.\nПри равенстве голосов проводится второй '
                       'тур из нескольких кандидатов.\nЕсли один кандидат выбран не был, происходит казнь всех '
                       'кандидатов. Роли также вскрываются\n\nКонец игры:\nИгра заканчивается победой опричников, '
                       'если количество опричников равно количеству мирных. Игра заканчивается победой мирных, '
                       'если все опричники казнены\n', self)
        self.label.setStyleSheet("color: white")
        self.label.adjustSize()

class History(QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root
        self.label = QLabel(
            ("Тоя же зимы, декабря в 3 день, в неделю, царь и великий князь Иван Васильевичь\nвсеа Русии с своею царицею и "
         "великою княгинею Марьею и с своими детми поехал\nс Москвы в село в Коломенское. Подъем же его не таков был, "
         "якоже преже того\nезживал по манастырем молитися, или на которые свои потехи в объезды\nездил: взял же с "
         "собою святость, иконы и кресты, златом и камением драгам украшенные,\nи суды золотые и серебряные, "
         "и поставцы все всяких судов, золотое и серебряное,\nи платие и денги и всю свою казну повеле взята с собою. "
         "Которым же бояром и дворяном\nближним и приказным людем повеле с собою ехати, и тем многим повеле с собою "
         "ехати з женами и з детми,\nа дворяном и детем боярским выбором изо всех городов, которых прибрал государь "
         "быта с ним,\nвелел тем всем ехати с собою с людми и с коими, со всем служебным нарядом\n"), self)
        self.label.setStyleSheet("color: white")
        self.label.adjustSize()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.dialog_rules = Rules(self)
        self.history = History(self)

        # set_widgets
        QFontDatabase.addApplicationFont("TDCyrillic.otf")
        QFontDatabase.addApplicationFont("TDRukopis.otf")

        self.begin = QPushButton("начать", self)
        self.begin.setFixedSize(QSize(100, 55))
        self.begin.setStyleSheet("background-color: white; border-radius: 18px; font: 60px")
        self.begin.setFont(QFont("TD Cyrillic"))
        self.begin.move(300, 280)
        self.begin.clicked.connect(self.begin_was_clicked)

        self.name = QLabel("МАФИЯ", self)
        self.name.move(225, 154)
        self.name.setStyleSheet("color: white; font: 100px")
        self.name.setFont(QFont("TD Rukopis"))
        self.name.adjustSize()


        self.rules = QPushButton("правила", self)
        self.rules.setFixedSize(QSize(90, 44))
        self.rules.setStyleSheet("background-color: white; border-radius: 18px; font: 40px")
        self.rules.setFont(QFont("TD Cyrillic"))
        self.rules.move(10, 10)
        self.rules.clicked.connect(self.dialog_rules.open)

        self.spravka = QPushButton("справка", self)
        self.spravka.setFixedSize(QSize(90, 44))
        self.spravka.setStyleSheet("background-color: white; border-radius: 18px; font: 40px")
        self.spravka.setFont(QFont("TD Cyrillic"))
        self.spravka.move(10, 70)
        self.spravka.clicked.connect(self.history.open)

        self.setFixedSize(QSize(705, 472))
        self.setStyleSheet("background-color: black")

    def begin_was_clicked(self):
        self.begin.setStyleSheet("background-color: black; color: white; border-radius: 18px; font: 60px")
        #запускаем экран введения сколько ролей


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
