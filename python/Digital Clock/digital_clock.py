import sys
import time
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt, QTime, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock")
        self.setGeometry(800,400,200,200)
        self.setStyleSheet("background-color:black;")
        self.timer = QTimer(self)
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.label1 = QLabel("",self)
        font_id =  QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.label1.setFont(my_font)
        self.label1.setStyleSheet("""
                                color:green;
                                font-weight:bold;

                                
                             
        """)
        self.label1.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.label1)

        central_widget.setLayout(hbox)

        self.timer.timeout.connect(self.setTime)
        self.timer.start(1000)
        self.setTime()
    def setTime(self):
            now = datetime.datetime.now().strftime("%H:%M:%S")
            self.label1.setText(now)


def main():
    global window
    window = MainWindow()
    window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    final = main()
    app.exec_()