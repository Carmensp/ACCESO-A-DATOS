from tkinter import *

# Configuración inicial de la ventana
root = Tk()
root.title("GESTIÓN DE RRHH")
root.geometry('400x350')
root.resizable(0, 0)
root.iconbitmap('ACCESO A DATOS/icon.ico')  # Cambiar según la ruta correcta
root.config(bd=50)

# Configurar las columnas para centrar
#root.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)  # Distribuir espacio entre columnas

# Cargar y configurar la imagen
imagen = PhotoImage(file="icon.png").subsample(4)
Label(root, text="NOMINATOR+", font=("Arial", 16, "bold")).grid(row=0, column=3)
Label(root, image=imagen).grid(row=1, column=3)

# Ajustar diseño de los botones para centrarlos
Button(root, text="ALTAS").grid(row=3, column=2, columnspan=2, sticky=EW, padx=5, pady=5)
Button(root, text="BAJAS").grid(row=3, column=4, columnspan=3, sticky=EW, padx=5, pady=5)
Button(root, text="INFORMES").grid(row=4, column=2, columnspan=2, sticky=EW, padx=5, pady=5)
Button(root, text="NÓMINAS").grid(row=4, column=4, columnspan=3, sticky=EW, padx=5, pady=5)

root.mainloop()
