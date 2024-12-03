from tkinter import *
import sqlite3
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import platform

conn = sqlite3.connect('RRHH.db')
c = conn.cursor()

def insertarEmpleado():
    try:
        # Insertar datos en la tabla
        c.execute("""INSERT INTO empleados(
        nombre, fecha_inicio, fecha_nacimiento, direccion, nif, datos_bancarios, 
        seguridad_social, genero, departamento, puesto, telefono, salario, 
        irpf, seguro_social, email, pagas_extra
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            nombre.get(),
            fIni.get(),
            fNaci.get(),
            direccion.get(),
            nif.get(),
            datosBanc.get(),
            numSs.get(),
            genero.get(),
            departamento.get(),
            puesto.get(),
            tlf.get(),
            salario.get(),
            irpf.get(),
            segSocial.get(),
            email.get(),
            pagas.get()
        ))
        conn.commit()
        print("Empleado insertado con éxito")
    except Exception as e:
        print(f"Error al insertar: {e}")
    
    nombre.set("")
    fIni.set("")
    fNaci.set("")
    direccion.set("")
    nif.set("")
    datosBanc.set("")
    numSs.set("")
    genero.set("")
    departamento.set("")
    puesto.set("")
    tlf.set("")
    salario.set("")
    email.set("")
    pagas.set("")

def altas():
    nv1 = Toplevel()
    
    global nombre, fIni, fNaci, direccion, nif, datosBanc, numSs, genero
    global departamento, puesto, tlf, salario, irpf, segSocial, email, pagas
    
    nombre = StringVar()
    fIni = StringVar()
    fNaci = StringVar()
    direccion = StringVar()
    nif = StringVar()
    datosBanc = StringVar()
    numSs = StringVar()
    genero = StringVar()
    departamento = StringVar()
    puesto = StringVar()
    tlf = StringVar()
    salario = DoubleVar()
    irpf = IntVar()
    irpf.set("10")
    segSocial = DoubleVar()
    segSocial.set("6.4")
    email = StringVar()
    pagas = DoubleVar()
    
    nv1.title("PRINCIPAL")
    nv1.geometry('1080x400')
    nv1.resizable(1,1)
    nv1.config(bd=50)
    
    Label(nv1, text="Apellidos y nombre").grid(row=0, column=2)
    Entry(nv1, textvariable=nombre).grid(row=1, column=0, columnspan=6, sticky=EW)
    
    Label(nv1, text="Fecha inicio").grid(row=2, column=0)
    Label(nv1, text="Fecha nacimiento").grid(row=2, column=1)
    Label(nv1, text="Dirección").grid(row=2, column=3)
    Entry(nv1, textvariable=fIni).grid(row=3, column=0, sticky=EW)
    Entry(nv1, textvariable=fNaci).grid(row=3, column=1, sticky=EW)
    Entry(nv1, textvariable=direccion).grid(row=3, column=2, columnspan=4, sticky=EW)
    
    Label(nv1, text="NIF").grid(row=4, column=0)
    Label(nv1, text="Datos bancarios").grid(row=4, column=2)
    Label(nv1, text="Número de afiliación SS").grid(row=4, column=5)
    Entry(nv1, textvariable=nif).grid(row=5, column=0, sticky=EW)
    Entry(nv1, textvariable=datosBanc).grid(row=5, column=1, columnspan=4, sticky=EW)
    Entry(nv1, textvariable=numSs).grid(row=5, column=5, columnspan=2, sticky=EW)
    
    Label(nv1, text="Género").grid(row=6, column=0)
    Label(nv1, text="Departamento").grid(row=6, column=2)
    Label(nv1, text="Puesto").grid(row=6, column=5)
    Entry(nv1, textvariable=genero).grid(row=7, column=0, sticky=EW)
    Entry(nv1, textvariable=departamento).grid(row=7, column=1, columnspan=4, sticky=EW)
    Entry(nv1, textvariable=puesto).grid(row=7, column=5, columnspan=2, sticky=EW)
    
    Label(nv1, text="Teléfono").grid(row=8, column=0)
    Entry(nv1, textvariable=tlf).grid(row=8, column=1, columnspan=1, sticky=EW)
    Label(nv1, text="Salario").grid(row=8, column=2)
    Entry(nv1, textvariable=salario).grid(row=8, column=3, columnspan=1, sticky=EW)
    Label(nv1, text="IRPF").grid(row=8, column=4)
    Entry(nv1, textvariable=irpf).grid(row=8, column=5, columnspan=1, sticky=EW)
    
    Label(nv1, text="Email").grid(row=9, column=0)
    Entry(nv1, textvariable=email).grid(row=9, column=1, columnspan=1, sticky=EW)
    Label(nv1, text="Pagas extra").grid(row=9, column=2)
    Entry(nv1, textvariable=pagas).grid(row=9, column=3, columnspan=1, sticky=EW)
    Label(nv1, text="Seg.Social").grid(row=9, column=4)
    Entry(nv1, textvariable=segSocial).grid(row=9, column=5, columnspan=1, sticky=EW)
    
    Label(nv1, text="Mensajes de validación", font=("Arial", 16), fg="red").grid(row=10, column=2)
    Button(nv1, text="INSERTAR", command=insertarEmpleado).grid(row=10, column=5, columnspan=2, sticky=EW)
    
    nv1.mainloop()

def darBajaEmpleado():
    try:
        c.execute("""
           UPDATE empleados
           SET fecha_baja = ?
           WHERE id = ?
        """, (fechaBaja.get(), cod.get()))
        conn.commit()
        cod.set("")
        fechaBaja.set("")
        print("Empleado dado de baja con éxito")
    except Exception as e:
        print(f"Error al dar de baja: {e}")

def bajas():
    nv2 = Toplevel()
    
    global cod,fechaBaja
    cod = IntVar()
    fechaBaja = StringVar()
    
    nv2.title("BAJAS")
    nv2.geometry('490x250')
    nv2.resizable(1,1)
    nv2.config(bd=50)
    
    Label(nv2, text="Código empleado").grid(row=0, column=0)
    Label(nv2, text="Fecha baja").grid(row=0, column=1)
    Entry(nv2, textvariable=cod).grid(row=1, column=0, columnspan=1, sticky=EW)
    Entry(nv2, textvariable=fechaBaja).grid(row=1, column=1, columnspan=1, sticky=EW)
    
    Label(nv2, text="Mensajes de validación", font=("Arial", 16), fg="red").grid(row=2, column=0)
    
    Button(nv2, text="CONFIRMAR", command=darBajaEmpleado).grid(row=3, column=0, columnspan=2, sticky=EW)
    
    nv2.mainloop()

def informes():
    nv3 = Toplevel()
    
    global emplAlta,emplBaja,edadMedia,retMedia,altaMujeres,bajaMujeres
    global edadMujeres,retMujeres,altaHombres,bajaHombres,edadHombres,retHombres
    
    emplAlta = IntVar()
    emplBaja = IntVar()
    edadMedia = DoubleVar()
    retMedia = DoubleVar()
    altaMujeres = DoubleVar()
    bajaMujeres = DoubleVar()
    edadMujeres = DoubleVar()
    retMujeres = DoubleVar()
    altaHombres = DoubleVar()
    bajaHombres = DoubleVar()
    edadHombres = DoubleVar()
    retHombres = DoubleVar()

    try:
        c.execute("""SELECT COUNT(*) FROM empleados WHERE fecha_baja IS NULL""")
        emplAlta.set(c.fetchone()[0])
        
        c.execute("""
            SELECT 
                (COUNT(CASE WHEN genero = 'Mujer' AND fecha_baja IS NULL THEN 1 END) * 100.0) / COUNT(*) 
            FROM empleados
            WHERE fecha_baja IS NULL
        """)
        altaMujeres.set(round(c.fetchone()[0] or 0, 2))
        
        c.execute("""
            SELECT 
                (COUNT(CASE WHEN genero = 'Hombre' AND fecha_baja IS NULL THEN 1 END) * 100.0) / COUNT(*) 
            FROM empleados
            WHERE fecha_baja IS NULL
        """)
        altaHombres.set(round(c.fetchone()[0] or 0, 2))
        
        c.execute("""SELECT COUNT(*) FROM empleados WHERE fecha_baja != ''""")
        emplBaja.set(c.fetchone()[0]) 
        
        c.execute("""
            SELECT 
                (COUNT(CASE WHEN genero = 'Mujer' AND fecha_baja != '' THEN 1 END) * 100.0) / COUNT(*) 
            FROM empleados
            WHERE fecha_baja != ''
        """)
        bajaMujeres.set(round(c.fetchone()[0] or 0, 2))
        
        c.execute("""
            SELECT 
                (COUNT(CASE WHEN genero = 'Hombre' AND fecha_baja != '' THEN 1 END) * 100.0) / COUNT(*) 
            FROM empleados
            WHERE fecha_baja != ''
        """)
        bajaHombres.set(round(c.fetchone()[0] or 0, 2)) 
        
        c.execute("""
            SELECT AVG(
                strftime('%Y', 'now') - strftime('%Y', 
                    substr(fecha_nacimiento, 7, 4) || '-' || substr(fecha_nacimiento, 4, 2) || '-' || substr(fecha_nacimiento, 1, 2)
                ) - 
                (strftime('%m-%d', 'now') < strftime('%m-%d', 
                    substr(fecha_nacimiento, 7, 4) || '-' || substr(fecha_nacimiento, 4, 2) || '-' || substr(fecha_nacimiento, 1, 2)
                ))
            ) 
            FROM empleados 
        """)
        edadMedia.set(round(c.fetchone()[0] or 0, 2))
        
        c.execute("""
            SELECT AVG(
                strftime('%Y', 'now') - strftime('%Y', 
                    substr(fecha_nacimiento, 7, 4) || '-' || substr(fecha_nacimiento, 4, 2) || '-' || substr(fecha_nacimiento, 1, 2)
                ) - 
                (strftime('%m-%d', 'now') < strftime('%m-%d', 
                    substr(fecha_nacimiento, 7, 4) || '-' || substr(fecha_nacimiento, 4, 2) || '-' || substr(fecha_nacimiento, 1, 2)
                ))
            ) 
            FROM empleados WHERE genero = 'Mujer'
        """)
        edadMujeres.set(round(c.fetchone()[0] or 0, 2))
        
        c.execute("""
            SELECT AVG(
                strftime('%Y', 'now') - strftime('%Y', 
                    substr(fecha_nacimiento, 7, 4) || '-' || substr(fecha_nacimiento, 4, 2) || '-' || substr(fecha_nacimiento, 1, 2)
                ) - 
                (strftime('%m-%d', 'now') < strftime('%m-%d', 
                    substr(fecha_nacimiento, 7, 4) || '-' || substr(fecha_nacimiento, 4, 2) || '-' || substr(fecha_nacimiento, 1, 2)
                ))
            ) 
            FROM empleados WHERE genero = 'Hombre'
        """)
        edadHombres.set(round(c.fetchone()[0] or 0, 2))

        c.execute("SELECT AVG(salario) FROM empleados")
        retMedia.set(round(c.fetchone()[0] or 0, 2))
        
        c.execute("SELECT AVG(salario) FROM empleados WHERE genero = 'Mujer' ")
        retMujeres.set(round(c.fetchone()[0] or 0, 2))
        
        c.execute("SELECT AVG(salario) FROM empleados WHERE genero = 'Hombre' ")
        retHombres.set(round(c.fetchone()[0] or 0, 2))
    
    except Exception as e:
        print(f"Error al obtener datos de la base de datos: {e}")
    
    nv3.title("INFORMES")
    nv3.geometry('860x350')
    nv3.resizable(1,1)
    nv3.config(bd=50)
    
    for i in range(4):
        nv3.columnconfigure(i, weight=1)
    for i in range(12):
        nv3.rowconfigure(i, weight=1)
    
    Label(nv3, text="Empleados", font=("Arial", 16, "bold")).grid(row=0, column=0)
    Label(nv3, text="Empleados", font=("Arial", 16, "bold")).grid(row=0, column=1)
    Label(nv3, text="Media", font=("Arial", 16, "bold")).grid(row=0, column=2)
    Label(nv3, text="Retribución", font=("Arial", 16, "bold"), fg="blue").grid(row=0, column=3)
    Label(nv3, text="Alta", font=("Arial", 16, "bold")).grid(row=1, column=0)
    Label(nv3, text="Baja", font=("Arial", 16, "bold")).grid(row=1, column=1)
    Label(nv3, text="Edades", font=("Arial", 16, "bold")).grid(row=1, column=2)
    Label(nv3, text="Media", font=("Arial", 16, "bold"), fg="blue").grid(row=1, column=3)
    Entry(nv3, textvariable=emplAlta).grid(row=2, column=0, columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=emplBaja).grid(row=2, column=1,  columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=edadMedia).grid(row=2, column=2,  columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=retMedia).grid(row=2, column=3,  columnspan=1, rowspan=2, sticky="nsew")
    
    Label(nv3, text="% Mujeres", font=("Arial", 16)).grid(row=4, column=0)
    Label(nv3, text="% Mujeres", font=("Arial", 16)).grid(row=4, column=1)
    Label(nv3, text="Mujeres", font=("Arial", 16)).grid(row=4, column=2)
    Label(nv3, text="Mujeres", font=("Arial", 16), fg="blue").grid(row=4, column=3)
    Entry(nv3, textvariable=altaMujeres).grid(row=5, column=0, columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=bajaMujeres).grid(row=5, column=1,  columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=edadMujeres).grid(row=5, column=2,  columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=retMujeres).grid(row=5, column=3,  columnspan=1, rowspan=2, sticky="nsew")
    
    Label(nv3, text="% Hombres", font=("Arial", 16)).grid(row=7, column=0)
    Label(nv3, text="% Hombres", font=("Arial", 16)).grid(row=7, column=1)
    Label(nv3, text="Hombres", font=("Arial", 16)).grid(row=7, column=2)
    Label(nv3, text="Hombres", font=("Arial", 16), fg="blue").grid(row=7, column=3)
    Entry(nv3, textvariable=altaHombres).grid(row=8, column=0, columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=bajaHombres).grid(row=8, column=1,  columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=edadHombres).grid(row=8, column=2,  columnspan=1, rowspan=2, sticky="nsew")
    Entry(nv3, textvariable=retHombres).grid(row=8, column=3,  columnspan=1, rowspan=2, sticky="nsew")
    
    nv3.mainloop()
    
def cargar():
    try:
        c.execute("""SELECT nombre,fecha_inicio,fecha_baja,direccion,nif,datos_bancarios,seguridad_social,pagas_extra,salario,irpf,seguro_social FROM empleados WHERE id = ?""",(codigo.get(),))
        resultado = c.fetchone()
        nom.set(resultado[0])
        fini.set(resultado[1])
        ffin.set(resultado[2])
        direc.set(resultado[3])
        numNif.set(resultado[4])
        datBan.set(resultado[5])
        afiSS.set(resultado[6])
        numPagas.set(resultado[7])
        salMes.set(resultado[8])
        porIrpf.set(resultado[9])
        segS.set(resultado[10])
    except Exception as e:
        print(f"Error al cargar empleado: {e}")

def calcular():
    try:
        c.execute("""SELECT nombre,fecha_inicio,fecha_baja,direccion,nif,datos_bancarios,seguridad_social,pagas_extra,salario,irpf,seguro_social FROM empleados WHERE id = ?""",(codigo.get(),))
        resultado = c.fetchone()
        salBruto.set(resultado[8]+(resultado[8]/12))
        proPagas.set(resultado[8]/12)
        retIrpf.set((resultado[8]+(resultado[8]/12))*0.1)
        dedSS.set((resultado[8]+(resultado[8]/12))*0.064)
        aPercibir.set((resultado[8]+(resultado[8]/12))-((resultado[8]+(resultado[8]/12))*0.1)-((resultado[8]+(resultado[8]/12))*0.064))
    except Exception as e:
        print(f"Error al calcular: {e}")

def imprimir():
    try:
        nominas_pdf = f"Nomina_{codigo.get()}.pdf"
        
        c = canvas.Canvas(nominas_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(30, 750, f"--- Nómina de {nom.get()} ---")
        
        c.drawString(30, 720, f"Código: {codigo.get()}")
        c.drawString(30, 700, f"Nombre: {nom.get()}")
        c.drawString(30, 680, f"Fecha de Inicio: {fini.get()}")
        c.drawString(30, 660, f"Fecha de Fin: {ffin.get()}")
        c.drawString(30, 640, f"Dirección: {direc.get()}")
        c.drawString(30, 620, f"NIF: {numNif.get()}")
        c.drawString(30, 600, f"Número SS: {afiSS.get()}")

        c.drawString(30, 560, f"Salario Bruto: {salBruto.get():.2f} €")
        c.drawString(30, 540, f"Pagas Extra: {numPagas.get()}")
        c.drawString(30, 520, f"IRPF (%): {porIrpf.get()} %")
        c.drawString(30, 500, f"Retención IRPF: {retIrpf.get():.2f} €")
        c.drawString(30, 480, f"Seguridad Social (%): {segS.get()} %")
        c.drawString(30, 460, f"Deducción Seguridad Social: {dedSS.get():.2f} €")
        c.drawString(30, 440, f"Salario Neto a Percibir: {aPercibir.get():.2f} €")

        c.save()
        
        if platform.system() == "Windows":
            os.startfile(nominas_pdf)
        elif platform.system() == "Darwin":  
            os.system(f"open {nominas_pdf}")
        else: 
            os.system(f"xdg-open {nominas_pdf}")
        
        print(f"Nómina generada con éxito: {nominas_pdf}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")
    
    nombre.set("")
    fIni.set("")
    fNaci.set("")
    direccion.set("")
    nif.set("")
    datosBanc.set("")
    numSs.set("")
    genero.set("")
    departamento.set("")
    puesto.set("")
    tlf.set("")
    salario.set("")
    email.set("")
    pagas.set("")

def nominas():
    nv4 = Toplevel()
    
    global codigo,nom,fini,ffin,direc,numNif,datBan,afiSS,salBruto,salMes,numPagas
    global porIrpf,retIrpf,proPagas,segS,dedSS,aPercibir
    
    codigo = IntVar()
    nom = StringVar()
    fini = StringVar()
    ffin = StringVar()
    direc = StringVar()
    numNif = StringVar()
    datBan = StringVar()
    afiSS = StringVar()
    salBruto = DoubleVar()
    salMes = DoubleVar()
    numPagas = IntVar()
    porIrpf = IntVar()
    retIrpf = DoubleVar()
    proPagas = IntVar()
    segS = DoubleVar()
    dedSS = DoubleVar()
    aPercibir = DoubleVar()
    
    nv4.title("NÓMINAS")
    nv4.geometry('1080x400')
    nv4.resizable(1,1)
    nv4.config(bd=50)
    
    Label(nv4, text="Código").grid(row=0, column=0)
    Label(nv4, text="Apellidos y nombre").grid(row=0, column=3)
    Entry(nv4, textvariable=codigo).grid(row=1, column=0, columnspan=1, sticky=EW)
    Entry(nv4, textvariable=nom, state=DISABLED).grid(row=1, column=1, columnspan=5, sticky=EW)
    
    Label(nv4, text="Fecha inicio").grid(row=2, column=0)
    Label(nv4, text="Fecha fin").grid(row=2, column=1)
    Label(nv4, text="Dirección").grid(row=2, column=3)
    Entry(nv4, textvariable=fini, state=DISABLED).grid(row=3, column=0, sticky=EW)
    Entry(nv4, textvariable=ffin, state=DISABLED).grid(row=3, column=1, sticky=EW)
    Entry(nv4, textvariable=direc, state=DISABLED).grid(row=3, column=2, columnspan=4, sticky=EW)
    
    Label(nv4, text="NIF").grid(row=4, column=0)
    Label(nv4, text="Datos bancarios").grid(row=4, column=2)
    Label(nv4, text="Número de afiliación SS").grid(row=4, column=5)
    Entry(nv4, textvariable=numNif, state=DISABLED).grid(row=5, column=0, sticky=EW)
    Entry(nv4, textvariable=datBan, state=DISABLED).grid(row=5, column=1, columnspan=4, sticky=EW)
    Entry(nv4, textvariable=afiSS, state=DISABLED).grid(row=5, column=5, columnspan=2, sticky=EW)
    
    Label(nv4, text="Salario bruto").grid(row=6, column=0)
    Entry(nv4, textvariable=salBruto, state=DISABLED).grid(row=6, column=1, columnspan=1, sticky=EW)
    Label(nv4, text="Número pagas").grid(row=6, column=2)
    Entry(nv4, textvariable=numPagas, state=DISABLED).grid(row=6, column=3, columnspan=1, sticky=EW)
    
    canvas_line = Canvas(nv4, height=2, bd=0, highlightthickness=0, bg="black")
    canvas_line.grid(row=7, column=0, columnspan=6, sticky="ew", pady=10)
    
    Label(nv4, text="Salario mes").grid(row=8, column=0)
    Entry(nv4, textvariable=salMes, state=DISABLED).grid(row=8, column=1, columnspan=1, sticky=EW)
    Label(nv4, text="%IRPF").grid(row=8, column=2)
    Entry(nv4, textvariable=porIrpf, state=DISABLED).grid(row=8, column=3, columnspan=1, sticky=EW)
    Label(nv4, text="Ret.IRPF").grid(row=8, column=4)
    Entry(nv4, textvariable=retIrpf, state=DISABLED).grid(row=8, column=5, columnspan=1, sticky=EW)
    
    Label(nv4, text="Prorrata pagas").grid(row=9, column=0)
    Entry(nv4, textvariable=proPagas, state=DISABLED).grid(row=9, column=1, columnspan=1, sticky=EW)
    Label(nv4, text="Seg.Social").grid(row=9, column=2)
    Entry(nv4, textvariable=segS, state=DISABLED).grid(row=9, column=3, columnspan=1, sticky=EW)
    Label(nv4, text="Ded.SS").grid(row=9, column=4)
    Entry(nv4, textvariable=dedSS, state=DISABLED).grid(row=9, column=5, columnspan=1, sticky=EW)
    
    Label(nv4, text="Mensajes validación", font=("Arial", 16), fg="red").grid(row=10, column=1)
    Label(nv4, text="A percibir").grid(row=10, column=4)
    Entry(nv4, textvariable=aPercibir, state=DISABLED).grid(row=10, column=5, columnspan=1, sticky=EW)
    
    Button(nv4, text="CARGAR EMPLEADO", command=cargar).grid(row=11, column=1, columnspan=2, sticky=EW)
    Button(nv4, text="CALCULAR", command=calcular).grid(row=11, column=4, sticky=EW)
    Button(nv4, text="IMPRIMIR", command=imprimir).grid(row=11, column=5, sticky=EW)
    
    nv4.mainloop()

root = Tk()
root.title("GESTIÓN DE RRHH")
root.geometry('450x350')
root.resizable(0,0)
root.iconbitmap('ACCESO A DATOS/icono.ico')
root.config(bd=50)

imagen = PhotoImage(file="icono.png").subsample(4)
Label(root, text="NOMINATOR+", font=("Arial", 16, "bold")).grid(row=0, column=4)
Label(root, image=imagen).grid(row=1, column=4)
Button(root, text="ALTAS", command=altas).grid(row=3, column=3, sticky=EW)
Button(root, text="BAJAS", command=bajas).grid(row=3, column=5, sticky=EW)
Button(root, text="INFORMES", command=informes).grid(row=4, column=3, sticky=EW)
Button(root, text="NÓMINAS", command=nominas).grid(row=4, column=5, sticky=EW)


root.mainloop()