
from tkinter import *
root = Tk()
root.title("EJEMPLO GRID")
root.geometry('550x350')
root.resizable(1,1)
root.iconbitmap('icon.ico')
root.config(bd=30)

imagen = PhotoImage(file="icon.png").subsample(4)
Label(root, image=imagen).grid(row=0, column=2)
Label(root, text="").grid(row=1, column=0)
Label(root, text="Nombre").grid(row=2, column=0)
Label(root, text="Apellidos").grid(row=3, column=0)
Label(root, text="").grid(row=4, column=0)
Label(root, text="Edad").grid(row=2, column=2)
Label(root, text="Teléfono").grid(row=3, column=2)

eti1 = Entry(root)
eti2 = Entry(root)
eti3 = Entry(root)
eti4 = Entry(root)
eti1.grid(row=2, column=1)
eti2.grid(row=3, column=1)
eti3.grid(columnspan=3, row=2, column=3)
eti4.grid(columnspan=3, row=3, column=3)

Button(root, text="ACEPTAR").grid(columnspan=2, row=5, column=0, sticky=EW)
Button(root, text="BORRAR").grid(columnspan=2, row=5, column=2, sticky=EW)

root.mainloop()