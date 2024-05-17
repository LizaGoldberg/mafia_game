import sys

from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QFont, QFontDatabase, QPixmap

class Whatname(QMainWindow): #template for "What's your name?"
    def __init__(self):
        super().__init__()

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
        #запускаем приветствие
        return (self.enter.text()) #возвращает число игроков

class Yourrole(QMainWindow): #template for "Your role is..."
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
        pixmap4 = pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image.setPixmap(pixmap4)
        #self.image.setScaledContents(True)
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
        #запускаем приветствие

    def what_role(self):
        return "Oprich"

    def what_role2(self):
        return "опричник"

app = QApplication(sys.argv)

window = Yourrole()
window.show()

app.exec()