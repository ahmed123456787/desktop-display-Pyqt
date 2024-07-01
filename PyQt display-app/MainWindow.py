from PyQt5.QtWidgets import  QMainWindow, QVBoxLayout, QWidget
from header import Header
from Body import Body


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display")
        self.setGeometry(100, 100, 800, 200)

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)

        header = Header(self)
        body = Body(self)
        
        central_layout.addWidget(header)
        central_layout.addWidget(body)
        
        central_layout.addStretch()  # This pushes the content down, keeping the header at the top

        self.setCentralWidget(central_widget)
