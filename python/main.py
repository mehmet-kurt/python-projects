from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("pyside")

        menubar = self.menuBar()

        menubar.setNativeMenuBar(False)

        container = QWidget()

        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        fileMenu = menubar.addMenu("File")
        editMenu = menubar.addMenu("Edit")
        showMenu = menubar.addMenu("Show")

        subfile = fileMenu.addMenu('subfile')
        exitAction = subfile.addAction('Exit')

        exitAction.triggered.connect(lambda: self.close())

        button = QPushButton('Click')

        button.clicked.connect(lambda: QMessageBox.information(self,'Clicked','You clicked'))

        layout.addWidget(button)

app = QApplication()
window = MainWindow()
window.show()
app.exec()