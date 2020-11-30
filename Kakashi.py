import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QKeyEvent
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('krug.ui', self)
        self.btn.clicked.connect(self.paintEvent)

    def paintEvent(self):
        r = random.randint(20, 200)
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        fiq_x = random.randint(10, 480)
        fiq_y = random.randint(10, 480)

        painter = QPainter()
        painter.begin()
        painter.setBrush(QColor(*color))
        painter.drawEllipse(fiq_x - r, fiq_y - r,
                            2 * r, 2 * r)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
