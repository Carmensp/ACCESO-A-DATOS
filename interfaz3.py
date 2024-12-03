
from tkinter import *

def sumar():
    res.set(float(num1.get()) + float(num2.get()))

def restar():
    res.set(float(num1.get()) - float(num2.get()))

def borrar():
    num1.set("")
    num2.set("")
    res.set("")

def configurar():
    nv1 = Toplevel()
    imagen = PhotoImage(file="icon.png").subsample(4)
    Label(nv1, image=imagen).grid(row=0, column=2)

    nv1.mainloop()

def altas():
    nv2 = Toplevel()

    Label(nv2, text="Primer número").pack()
    Entry(nv2, justify=CENTER, textvariable=num1).pack()
    Label(nv2, text="Segundo número").pack()
    Entry(nv2, justify=CENTER,  textvariable=num2).pack()
    Label(nv2, text="Resultado").pack()
    Entry(nv2, justify=CENTER, state=DISABLED, textvariable=res).pack()
    Button(nv2, text="Sumar", command=sumar).pack(side=LEFT)

    nv2.mainloop()

root = Tk()
root.title("CALCULATOR")
root.geometry('550x350')
root.resizable(0,0)
root.iconbitmap('icon.ico')
root.config(bd=50)

num1 = StringVar()
num2 = StringVar()
res = StringVar()

Label(root, text="Primer número").pack()
Entry(root, justify=CENTER, textvariable=num1).pack()
Label(root, text="Segundo número").pack()
Entry(root, justify=CENTER,  textvariable=num2).pack()
Label(root, text="Resultado").pack()
Entry(root, justify=CENTER, state=DISABLED, textvariable=res).pack()

Label(root, text="").pack()

Button(root, text="Sumar", command=sumar).pack(side=LEFT)
Button(root, text="Restar", command=restar).pack(side=LEFT)
Button(root, text="Borrar", command=borrar).pack(side=LEFT)
Button(root, text="Configuración", command=configurar).pack(side=LEFT)
Button(root, text="Altas", command=altas).pack(side=LEFT)

root.mainloop()