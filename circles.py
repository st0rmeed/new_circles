import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import QRect
import random


class UiCircles(object):
    def __init__(self):
        self.centralwidget = None
        self.button = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cicles")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(QVBoxLayout())
        self.button = QPushButton("WRITE", parent=self.centralwidget)
        self.button.setObjectName("button")


class Circles(QMainWindow, UiCircles):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.setupUi(self)
        self.button.clicked.connect(self.write_circles)
        self.show()

    def write_circles(self):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        diameter = random.randint(10, 100)
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, circle_color))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for x, y, diameter, color_ in self.circles:
            qp.setBrush(QBrush(QColor(color_[0], color_[1], color_[2])))
            qp.drawEllipse(QRect(x, y, diameter, diameter))
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    sys.exit(app.exec())
