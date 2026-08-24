import tkinter as tk
from tkinter import messagebox
a = ""
def s(num):
    enter.insert(tk.END,num)

def to():
    global sayi1,a
    try:
        sayi1 = float(sayi_var.get())
    except:
        messagebox.showerror('Python Error', "lutfen sayi giriniz, ondalik sayilar icin . kullanin")
    sayi_var.set("")
    a=1
def ci():
    global sayi1,a
    try:
        sayi1 = float(sayi_var.get())
    except:
        messagebox.showerror('Python Error', "lutfen sayi giriniz, ondalik sayilar icin . kullanin")
    sayi_var.set("")
    a=2
def ca():
    global sayi1,a
    try:
        sayi1 = float(sayi_var.get())
    except:
        messagebox.showerror('Python Error', "lutfen sayi giriniz, ondalik sayilar icin . kullanin")
    sayi_var.set("")
    a=3
def bo():
    global sayi1,a
    try:
        sayi1 = float(sayi_var.get())
    except:
        messagebox.showerror('Python Error', "lutfen sayi giriniz, ondalik sayilar icin . kullanin")
    sayi_var.set("")
    a=4




root = tk.Tk()
root.title("Calculator")
sayi_var = tk.StringVar()
def submit():
    global sayi1,a
    try:
        sayi2 = float(sayi_var.get())
        if a == "":
            sayi_var.set(sayi2)
        elif a == 1:
            sayi_var.set(sayi1+sayi2)
        elif a == 2:
            sayi_var.set(sayi1-sayi2)
        elif a == 3:
            sayi_var.set(sayi1*sayi2)
        elif a == 4:
            sayi_var.set(sayi1/sayi2)
        a = 0
    except:
        messagebox.showerror('Python Error', "lutfen sayi giriniz, ondalik sayilar icin . kullanin")
        

enter = tk.Entry(root,textvariable=sayi_var,font=('Times New Roman',24,'bold'))
enter.pack(side=tk.TOP,fill="x",padx="5",pady="10")
frame1 = tk.Frame(root,bg="red")
frame1.pack()
buton1 = tk.Button(frame1,text="1",command=lambda:s(1),width=24,height=5,font=('Times New Roman',12,'bold'))
buton2 = tk.Button(frame1,text="2",command=lambda:s(2),width=24,height=5,font=('Times New Roman',12,'bold'))
buton3 = tk.Button(frame1,text="3",command=lambda:s(3),width=24,height=5,font=('Times New Roman',12,'bold'))
buton4 = tk.Button(frame1,text="4",command=lambda:s(4),width=24,height=5,font=('Times New Roman',12,'bold'))
buton5 = tk.Button(frame1,text="5",command=lambda:s(5),width=24,height=5,font=('Times New Roman',12,'bold'))
buton6 = tk.Button(frame1,text="6",command=lambda:s(6),width=24,height=5,font=('Times New Roman',12,'bold'))
buton7 = tk.Button(frame1,text="7",command=lambda:s(7),width=24,height=5,font=('Times New Roman',12,'bold'))
buton8 = tk.Button(frame1,text="8",command=lambda:s(8),width=24,height=5,font=('Times New Roman',12,'bold'))
buton9 = tk.Button(frame1,text="9",command=lambda:s(9),width=24,height=5,font=('Times New Roman',12,'bold'))
buton0 = tk.Button(frame1,text="0",command=lambda:s(0),width=24,height=5,font=('Times New Roman',12,'bold'))
butondot = tk.Button(frame1,text=".",command=lambda:s("."),width=24,height=5,font=('Times New Roman',12,'bold'))
butoneq=tk.Button(frame1,text="=",command=submit,width=24,height=5,font=('Times New Roman',12,'bold'))
butonto=tk.Button(frame1,text="+",command=to,width=24,height=5,font=('Times New Roman',12,'bold'))
butonci=tk.Button(frame1,text="-",command=ci,width=24,height=5,font=('Times New Roman',12,'bold'))
butonca=tk.Button(frame1,text="x",command=ca,width=24,height=5,font=('Times New Roman',12,'bold'))
butonbo=tk.Button(frame1,text="/",command=bo,width=24,height=5,font=('Times New Roman',12,'bold'))
buton0.grid(row=3,column=0)
buton1.grid(row=2,column=0)
buton2.grid(row=2,column=1)
buton3.grid(row=2,column=2)
buton4.grid(row=1,column=0)
buton5.grid(row=1,column=1)
buton6.grid(row=1,column=2)
buton7.grid(row=0,column=0)
buton8.grid(row=0,column=1)
buton9.grid(row=0,column=2)
butondot.grid(row=3,column=1)
butoneq.grid(row=3,column=2)
butonto.grid(row=0,column=3)
butonci.grid(row=1,column=3)
butonca.grid(row=2,column=3)
butonbo.grid(row=3,column=3)
root.mainloop()