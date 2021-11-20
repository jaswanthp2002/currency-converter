from os import linesep, read
from tkinter import *
from tkinter import ttk




converter = Tk()
converter.title("unit converter")
converter.geometry("600x400")

OPTIONS = {
   "Australian Dollar":0.0184,
    "Brazilian Real":0.0731,
    "British Pound":0.01,
    "Chinese Yuan":0.086,
    "Euro":0.0116,
    "HongKong Dollar":0.1049,
    "Indonesian Rupiah":192.2143,
    "Japanese Yen":1.5314,
    "Pakistani Rupee":2.338,
    "SriLankan Rupee":2.7182,
    "Swiss Franc":0.0124,
    "Us Dollar":0.0135
          }

def ok():
    price = rupees.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ",INSERT,converted)
appName = Label(converter,text="Currency Converter",font=("times new roman",25,"bold","underline"),fg="dark orange")
appName.place(x=150, y=10)


result = Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5,fg="black")
result.place(x=125, y=60)

india = Label(converter,text="Value in indian Rupees:",font=("arial",10,"bold"),fg="black")
india.place(x=30, y=165)

rupees = Entry(converter,font=("arial",20))
rupees.place(x=200, y=160)

choice = Label(converter,text="Choice:",font=("arial",10,"bold"),fg="black")
choice.place(x=30, y=220)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter,variable1,*OPTIONS)
option.place(x=100 , y=210,width=100, height=40)

button = Button(converter,text="Convert",fg="green",font=("arial",20),bg="powder blue",command=ok)
button.place(x=200, y=210,height=40,width=150)








converter.mainloop()