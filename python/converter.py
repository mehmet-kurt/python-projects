import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QVBoxLayout, QLineEdit, QLabel, QGridLayout
from PySide6.QtCore import Qt

url = "https://v6.exchangerate-api.com/v6/2089a6c98a19f11127a3b1c6/latest/TRY"

response = requests.get(url,)
data = response.json()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Currency Converter")
        self.setGeometry(0,0,800,400)


        container = QWidget()
        self.setCentralWidget(container)

        main_layout = QGridLayout(container)

        label1 = QLabel("Enter amount in base current")

        self.line_edit1 = QLineEdit()

        label2 = QLabel("Enter base currency (e.g., EUR, GBP, JPY):")

        self.line_edit2 = QLineEdit()

        label3 = QLabel("Enter target currency (e.g., EUR, GBP, JPY):")
        self.line_edit3 = QLineEdit()

        button = QPushButton('Convert')
        button.clicked.connect(self.button_clicked)
        main_layout.addWidget(label1,0,0,1,1)
        main_layout.addWidget(self.line_edit1,0,1,1,2)
        main_layout.addWidget(label2,1,0,1,1)
        main_layout.addWidget(self.line_edit2,1,1,1,2)
        main_layout.addWidget(label3,2,0,1,1)
        main_layout.addWidget(self.line_edit3,2,1,1,2)
        main_layout.addWidget(button,3,1,1,1)

    def button_clicked(self):
        try:
            amount = float(self.line_edit1.text())
            base_currency = str(self.line_edit2.text())
            target_currency = str(self.line_edit3.text()).upper()

            url = f"https://v6.exchangerate-api.com/v6/2089a6c98a19f11127a3b1c6/latest/{base_currency}"

            response = requests.get(url,)
            data = response.json()

            converted_amount = amount * data['conversion_rates'][target_currency]
            QMessageBox.information(self, 'Converted Amount', f'Converted Amount: {converted_amount:.2f} {target_currency}')
        except:
            QMessageBox.information(self,"Error","Please enter valid values")

print(data)

app = QApplication()
window = MainWindow()
window.show()
app.exec()

