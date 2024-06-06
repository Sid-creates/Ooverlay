from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        #self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setStyleSheet("background-color: rgba(0, 0, 255, 25);")  # 75% opacity blue

        layout = QVBoxLayout()

        # Add a text label
        text_label = QLabel("Hello, World!", self)
        text_label.setStyleSheet("color: black; background-color: white;")
        text_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        text_label.setFixedWidth(int(self.width() * 0.5))  # Convert to int
        text_label.setFixedHeight(int(self.height() * 0.5))  # Convert to int
        layout.addWidget(text_label)

        text_label = QLabel("Hello, World22!", self)
        text_label.setStyleSheet("color: black; background-color: white;")
        text_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        text_label.setFixedWidth(int(self.width() * 0.5))  # Convert to int
        text_label.setFixedHeight(int(self.height() * 0.5))  # Convert to int
        layout.addWidget(text_label)

        self.setLayout(layout)

app = QApplication([])
overlay = Overlay()
overlay.showFullScreen()  # Show the overlay as full screen
app.exec_()