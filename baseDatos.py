import sqlite3

conn = sqlite3.connect('RRHH.db')
c = conn.cursor()

c.execute("""
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    fecha_inicio TEXT,
    fecha_baja TEXT,
    fecha_nacimiento TEXT,
    direccion TEXT,
    nif TEXT,
    datos_bancarios TEXT,
    seguridad_social TEXT,
    genero TEXT,
    departamento TEXT,
    puesto TEXT,
    telefono TEXT,
    salario REAL,
    irpf REAL,
    seguro_social REAL,
    email TEXT,
    pagas_extra REAL
)
""")

conn.commit()
conn.close()
