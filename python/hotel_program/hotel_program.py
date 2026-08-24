import json
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QVBoxLayout, 
                             QLineEdit, QPushButton, QGridLayout, QTabWidget, QScrollBar, 
                             QScrollArea,QGroupBox, QMessageBox)
from PyQt5.QtGui import QFont, QScrollEvent
from PyQt5.QtCore import Qt, QTime, QTimer, QSize
file_path = "customers.json"

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel Program")
        self.setGeometry(0,0,1400,600)
        self.setFixedSize(1400,600)
        self.setFont(QFont("Times"))
        self.label = QLabel("Hotel Registration System",self)
        self.entryName = QLineEdit(self)
        self.entryId = QLineEdit(self)
        self.entryBirthdate = QLineEdit(self)
        self.labeln = QLabel("Ad-Soyadı",self)
        self.labeli = QLabel("Kimlik No",self)
        self.labelb = QLabel("Doğum Tarihi",self)
        
        self.submit_button = QPushButton("Submit",self)
        self.delete_button = QPushButton("Delete",self)
        self.submit_button.clicked.connect(self.submit)
        self.delete_button.clicked.connect(self.delete)
        self.initUI()

    def initUI(self):
        self.tabs = QTabWidget(self)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1,"Main",)
        self.tabs.addTab(self.tab2,"Customers")
        layout2 = QVBoxLayout()
        gridbox = QGridLayout()
        self.tab1.setLayout(gridbox)
        self.tab2.setLayout(layout2)
        self.tab2l = QVBoxLayout()
        self.groupbox = QGroupBox()
        try:
            with open(file_path,"r") as file:
                content = json.load(file)
            print(len(content))
            for i in range(99):
                try:
                    a = QLabel(f"   Ad-Soyad: {content[f"customer{i}"][0]}   -   Kimlik No: {content[f"customer{i}"][1]}   -   Doğum Tarihi: {content[f"customer{i}"][2]}")
                    a.setStyleSheet("""
                            color:white;
                            font-size:24px;
                            font-weight:600;
                            padding:8px;
                            background-color:#1E3617;
                            border-radius:12px;

""")
                    self.tab2l.addWidget(a)
                except:
                    pass
        except:
            content=""
        
        self.tab2l.addStretch()
        self.groupbox.setLayout(self.tab2l)

        scroll = QScrollArea(self)
        scroll.setWidget(self.groupbox)
        scroll.setFixedHeight(500)
        scroll.setWidgetResizable(True)
        
        layout2.addWidget(scroll)


        gridbox.addWidget(self.label,0,0,1,4,Qt.AlignTop)
        gridbox.addWidget(self.labeln,1,0,1,1,Qt.AlignTop)
        gridbox.addWidget(self.labeli,2,0,1,1,Qt.AlignTop)
        gridbox.addWidget(self.labelb,3,0,1,1,Qt.AlignTop)
        gridbox.addWidget(self.entryName,1,1,1,3,Qt.AlignTop)
        gridbox.addWidget(self.submit_button,4,4,1,1,Qt.AlignTop)
        gridbox.addWidget(self.entryId,2,1,1,3,Qt.AlignTop)
        gridbox.addWidget(self.entryBirthdate,3,1,1,3,Qt.AlignTop)
        gridbox.addWidget(self.delete_button,4,3,1,1)
        gridbox.setHorizontalSpacing(20)
        gridbox.setVerticalSpacing(20)
        self.entryId.setPlaceholderText("A person can be removed by entering id")
        self.entryBirthdate.setPlaceholderText("DD.MM.YYYY")

        self.label.setStyleSheet(
                            "color:#939FB8;"
                            "background-color:#422857;"
                            "font-weight:800;" 
                            "font-size:64px;"
                            "padding:10px;"


        )
        self.entryName.setStyleSheet("""
                            font-size:40px;
                            margin:0;
                            padding:0;

""")
        self.entryId.setStyleSheet("""
                            font-size:40px;
                            margin:0;
                            padding:0;

""")
        self.entryBirthdate.setStyleSheet("""
                            font-size:40px;
                            margin:0;
                            padding:0;

""")

        self.labelb.setObjectName("label")
        self.labeln.setObjectName("label")
        self.labeli.setObjectName("label")
        self.setStyleSheet("""

                        QLabel#label{
                                color:#120712;
                                background-color:#64773C;
                                padding:10px;
                                border:2px solid black;
                                font-size:24px;
                                font-weight:600;
                                border-radius:10px;
                           }
                        QPushButton{
                                color: #A9A270;
                                background-color:#595194;
                                font-size:36px;
                                font-weight:600;
                                padding:10px;
                                border: 3px solid #A9A270;
                                border-radius: 10px;
                            }
                        QPushButton:hover{
                            background-color:#939FB8;
                                         
                                         }
""")

        self.label.setAlignment(Qt.AlignCenter)
        self.labeli.setAlignment(Qt.AlignCenter)
        self.labeln.setAlignment(Qt.AlignCenter)
        self.labelb.setAlignment(Qt.AlignCenter)


        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    def submit(self):
        is_digit = True
        c_name = self.entryName.text()
        c_id = self.entryId.text()
        c_birthdate = self.entryBirthdate.text()
        try:
            with open(file_path,"r") as file:
                sample_list = json.load(file)
        except:
            sample_list = {}
        id_list = []
        for i in sample_list.values():
            try:
                id_list.append(i[1])
            except:
                pass
        """print(id_list)"""
        try:
            a = len(c_id)
            c_id = int(c_id)
        except:
            is_digit = False

        
        """Date format control"""
        date_control = 0
        for i, key in enumerate(c_birthdate):
            if len(c_birthdate) != 10:
                break
            if i in [0,1,3,4,6,7,8,9]:
                if key.isdigit():
                    date_control+=1
            if i in [2,5]:
                if key ==".":
                    date_control+=1

        if c_name == "" or c_id == "" or c_birthdate == "":
            self.show_error_msg("Please fill out all sections")

        elif is_digit == False or a != 11:
            self.show_error_msg("Id is invalid")

        elif c_id in id_list:
            self.show_error_msg("This id has already been registered")

        elif date_control != 10:
            self.show_error_msg("This is not a correct form of a birth date")
        else:
            create_customer(c_name,c_id,c_birthdate)
            with open(file_path,"r") as file:
                printing_list = json.load(file)
            print(printing_list)
            self.tab2.deleteLater()
            self.tab2 = QWidget()
            tab2l = QVBoxLayout()
            groupbox = QGroupBox()
            layout2 = QVBoxLayout()
            for i in range(99):
                try:
                    a = QLabel(f"   Ad-Soyad: {printing_list[f"customer{i}"][0]}   -   Kimlik No: {printing_list[f"customer{i}"][1]}   -   Doğum Tarihi: {printing_list[f"customer{i}"][2]}")
                    a.setStyleSheet("""
                            color:white;
                            font-size:24px;
                            font-weight:600;
                            padding:8px;
                            background-color:#1E3617;
                            border-radius:12px;
""")
                    tab2l.addWidget(a)
                except:
                    pass
            tab2l.addStretch()
            groupbox.setLayout(tab2l)        
            scroll = QScrollArea(self)
            scroll.setWidget(groupbox)
            scroll.setFixedHeight(500)
            scroll.setWidgetResizable(True)
            layout2.addWidget(scroll)
            self.tab2.setLayout(layout2)
            self.tabs.addTab(self.tab2,"Customers")

    def delete(self):
        try:
            with open(file_path,"r") as file:
                content = json.load(file)
        except:
            content = {}

        del_text = self.entryId.text()

        del_text = int(del_text)
        key_f = 0
        for key in content:
            try:
                result = content[key][1]
                if del_text == result:
                    key_f = key
            except:
                pass
        
        try:
            content.pop(key_f)
            self.show_success_msg(f"Id:{del_text} was deleted succesfully")
        except:
            self.show_error_msg("This id could not be found")
        
        with open(file_path, "w") as w_file:
            json.dump(content,w_file,indent=4)

        with open(file_path,"r") as file:
                printing_list = json.load(file)

        self.tab2.deleteLater()
        self.tab2 = QWidget()
        tab2l = QVBoxLayout()
        groupbox = QGroupBox()
        layout2 = QVBoxLayout()
        for i in range(99):
            try:
                a = QLabel(f"   Ad-Soyad: {printing_list[f"customer{i}"][0]}   -   Kimlik No: {printing_list[f"customer{i}"][1]}   -   Doğum Tarihi: {printing_list[f"customer{i}"][2]}")
                a.setStyleSheet("""
                            color:white;
                            font-size:24px;
                            font-weight:600;
                            padding:8px;
                            background-color:#1E3617;
                            border-radius:12px;
""")
                tab2l.addWidget(a)
            except:
                pass
        tab2l.addStretch()
        groupbox.setLayout(tab2l)        
        scroll = QScrollArea(self)
        scroll.setWidget(groupbox)
        scroll.setFixedHeight(500)
        scroll.setWidgetResizable(True)
        layout2.addWidget(scroll)
        self.tab2.setLayout(layout2)
        self.tabs.addTab(self.tab2,"Customers")


    def show_error_msg(self,text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg_exec = msg.exec()

    def show_success_msg(self,text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg_exec = msg.exec()

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


class Customer:
    cus_num = 0
    def __init__(self,name,id,birth_date):
        self.name = name
        self.id = id
        self.birth_date = birth_date

    def __str__(self):
        return f"{self.name} is the name of this customer"

def create_customer(name,id,birth_date):
    new_customer = Customer(name=name,id=id,birth_date=birth_date)
    try:
        with open(file_path,"r") as r_file:
            final_list = json.load(r_file)
            Customer.cus_num = final_list["customer_number"] +1
    except:
        final_list = {}
    finally:

        final_list.update({"customer_number":Customer.cus_num})
        final_list.update({f"customer{Customer.cus_num}":[new_customer.name,new_customer.id,new_customer.birth_date]})

        with open(file_path,"w") as file:
            json.dump(final_list,file,indent=4)
            print("Update is succesful")


if __name__ == "__main__":
    main()