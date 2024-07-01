from PyQt5.QtWidgets import QVBoxLayout , QLabel , QHBoxLayout ,  QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Body(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        station_name = QLabel('Zouaghi Slimane', self)
        station_name.setFont(QFont('Arial', 50))
        station_name.setAlignment(Qt.AlignLeft)
        layout.addWidget(station_name)

        icons_layout = QVBoxLayout()

        def create_icon(text, size=50, color='black', bg_color='white', border_color='black'):
            
            label = QLabel(self)
            label.setText(text)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(f'''
                QLabel {{
                    border: 2px solid {border_color};
                    border-radius: {size // 2}px;
                    text-align: center;
                    font-size: {size // 2}px;
                    background-color: {bg_color};
                    color: {color};
                    width: {size}px;
                    height: {size}px;
                }}
            ''')
            label.setFixedSize(size, size)
            return label

        icons_layout.addWidget(create_icon('B'))
        icons_layout.addWidget(create_icon('2', color='white', bg_color='#8B0000'))
        icons_layout.addWidget(create_icon('4', color='white', bg_color='#0000CD'))
        icons_layout.addWidget(create_icon('T', border_color='white'))
        icons_layout.addWidget(create_icon('T1', color='white', bg_color='green'))

        taxi_label = QLabel('TAXI', self)
        taxi_label.setFont(QFont('Arial', 30))
        taxi_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(taxi_label)

        icons_layout.addWidget(create_icon(''))
        layout.addLayout(icons_layout)

        self.setLayout(layout)
