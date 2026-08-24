from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
import sys

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def buttonClicked(self,message):
        self.label.setText(message)

    def initUI(self):
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Button Click")
        self.label = QLabel("",self)
        self.button = QPushButton("click",self)
        self.button.setGeometry(10,20,100,50)
        self.button.clicked.connect(lambda:self.buttonClicked("hi"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec())