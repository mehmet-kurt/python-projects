from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QComboBox, QCheckBox, QRadioButton, QSlider, QProgressBar, QTabWidget, QStackedWidget, QScrollArea, QListWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Example")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        label = QLabel("Zero")
        label.setAlignment(Qt.AlignCenter)

        line_edit = QLineEdit()
        text_edit = QTextEdit()

        button = QPushButton("Click Me")
        button.clicked.connect(self.printer)

        combobox = QComboBox()
        combobox.addItems(["Option 1", "Option 2", "Option 3"])

        listWidget = QListWidget()
        listWidget.addItems(["1","2","3"])

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        radiobutton1 = QRadioButton('1')
        radiobutton2 = QRadioButton('2')
        radiobutton3 = QRadioButton('3')

        for r in (radiobutton1,radiobutton2,radiobutton3):
            r.toggled.connect(self.radio_changed)

        listWidget.itemClicked.connect(lambda item: print(f'Item clicked {item.text()}'))

        inner_layout.addWidget(radiobutton1)
        inner_layout.addWidget(radiobutton2)
        inner_layout.addWidget(radiobutton3)
        

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(text_edit)
        layout.addWidget(combobox)
        layout.addWidget(listWidget)
        layout.addWidget(inner_container)
        layout.addWidget(button)

    def printer(self):
        print("Button clicked")

    def radio_changed(self):
        r = self.sender()
        if r.isChecked():
            print(r.text())

app = QApplication()
window = MainWindow()
window.show()

app.exec()