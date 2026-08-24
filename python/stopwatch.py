import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt, QTime, QTimer

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")
        self.setGeometry(600,200,600,400)
        self.time = QTime(0,0,0,0)
        self.label = QLabel("00:00:00:00",self)
        self.startb = QPushButton("Start",self)
        self.stopb = QPushButton("Stop",self)
        self.resetb = QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.startb)
        vbox.addWidget(self.stopb)
        vbox.addWidget(self.resetb)
        
        self.setLayout(vbox)

        self.label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.startb)
        hbox.addWidget(self.stopb)
        hbox.addWidget(self.resetb)

        vbox.addLayout(hbox)
        self.startb.setObjectName("b1")
        self.stopb.setObjectName("b2")
        self.resetb.setObjectName("b3")

        self.setStyleSheet("""
                    QLabel{
                           color:black;
                           background-color:hsl(205, 100%, 60%);
                           font-size:64px;
                           font-weight:bold;
                           border-radius:15px;

                           }
                    QPushButton{
                           color:black;
                           border: 3px solid;
                           border-radius: 15px;
                           font-size:24px;
                            background-color: hsl(290, 100%, 60%);
                           
                           }
                
                    QPushButton:hover{
                                font-size:24px;
                                background-color: hsl(290, 100%, 81%);
                                
                           } 

    """)
        
        self.startb.clicked.connect(self.start)
        self.stopb.clicked.connect(self.stop)
        self.resetb.clicked.connect(self.reset)
        self.timer.timeout.connect(self.updateTime)
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.label.setText(self.formatTime(self.time))
    def formatTime(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{miliseconds:02}"
    def updateTime(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.formatTime(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())