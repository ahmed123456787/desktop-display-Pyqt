from PyQt5.QtWidgets import  QApplication 
from MainWindow import MainWindow	
import sys
 
app = QApplication(sys.argv)
window = MainWindow()
window.showFullScreen()
sys.exit(app.exec_())