from tkinter import *
root = Tk()
root.title("CARMEN")
root.resizable(1,1) #si pones 1 se puede estirar la pantalla, con 0 no se puede
#root.geometry('850x550+300x500')
root.iconbitmap('icon.ico')

texto = Text(root)
texto.pack()
texto.config(width=50, height=20, font=('consola',12), selectbackground="red")

root.mainloop()