from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
import sys

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def pushMessage(self):
        result = QMessageBox.question(self,"Soru","En büyük hangisi?",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
    

    def initUI(self):
        self.setGeometry(100,100,600,400)
        self.label = QLabel("",self)
        self.button = QPushButton("Click",self)
        self.button.setGeometry(50,50,100,50)
        self.button.clicked.connect(self.pushMessage)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win=Win()
    sys.exit(app.exec())