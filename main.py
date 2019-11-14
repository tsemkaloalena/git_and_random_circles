import random

from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QKeyEvent
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.WIDTH, self.HEIGHT = 650, 700
        Form.setGeometry(100, 100, self.WIDTH, self.HEIGHT)

        self.btn = QPushButton('Новый жёлтый кружочек 😁', self)
        self.btn.move(200, 50)
        self.btn.resize(200, 50)


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и случайные окружности')
        self.flag = False
        self.btn.clicked.connect(self.paint_circle)

    def paint_circle(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(0, self.WIDTH)
        self.y = random.randint(0, self.HEIGHT)
        self.d = random.randint(20, 400)
        self.flag = True
        self.repaint()

    def paintEvent(self, QPaintEvent):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(*self.color))
            painter.drawEllipse(self.x, self.y, self.d, self.d)
            painter.end()
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
