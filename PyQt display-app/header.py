import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSpacerItem , QSizePolicy
from PyQt5.QtCore import Qt, QTimer, QTime

class Header(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
       
        b_label = QLabel(self)
        b_label.setText('B')
        b_label.setAlignment(Qt.AlignCenter)
        b_label.setStyleSheet('''
            QLabel {
                border: 6px solid black;
                border-radius: 50px;
                text-align: center;
                font-size: 60px;
                background-color: white;
            }
        ''')
        b_label.setFixedSize(100, 100)

        # Yellow circle with 1
        one_label = QLabel(self)
        one_label.setText('1')
        one_label.setAlignment(Qt.AlignCenter)
        one_label.setStyleSheet('''
            QLabel {
                border: 2px solid #DAA520;
                border-radius: 50px;
                text-align: center;
                font-size: 60px;
                background-color: #DAA520;
                color: black;
            }
        ''')
        one_label.setFixedSize(100, 100)

        # Text Label "Constantine Airport"
        text_label = QLabel('Constantine Airport', self)
        text_label.setFont(QFont('Arial', 50))
        text_label.setAlignment(Qt.AlignLeft | Qt.AlignLeft)

        # Time Label
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet('''
            QLabel {
                border: 2px solid black;
                border-radius: 30px;
                background-color: black;
                color: #DAA520;
                font-size: 50px;
            }
        ''')
        self.time_label.setFixedSize(200, 100)

        # Timer to update the time
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()

        layout.addWidget(b_label)
        layout.addWidget(one_label)
        spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer)
        layout.addWidget(text_label)
        layout.addStretch()
        layout.addWidget(self.time_label)

        self.setLayout(layout)

    def update_time(self):
        current_time = QTime.currentTime().toString('HH:mm')
        self.time_label.setText(current_time)
