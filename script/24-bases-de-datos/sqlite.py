#importar modulo
import sqlite3

#conexion
conexion = sqlite3.connect('./24-bases-de-datos/pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear tabla
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY autoincrement, "+
"titulo VARCHAR(255), "+
"descripcion TEXT, "+
"precio INT(12)"+
")")
"""
#forma mas sencilla con triple comilla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY autoincrement, 
    titulo VARCHAR(255), 
    descripcion TEXT,
    precio INT(12)
)""")

#guardar cambios
conexion.commit()

#insertar datos
"""
cursor.execute("INSERT INTO productos VALUES(null, 'segundo producto', 'descripcion de mi producto', 550)")
conexion.commit()
"""
#borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

#insertar muchos registros de golpe
productos_insertar = [
    ('pc portatil', 'buen pc', 700),
    ('telefono', 'buen telefono', 140),
    ('tarjeta madre', 'buena tarjeta', 80),
    ('tablet', 'buena tablet', 300),
]
cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)", productos_insertar)
conexion.commit()

#actualizar
cursor.execute("UPDATE productos SET precio=87 WHERE precio=80")
conexion.commit()

#listar datos
cursor.execute("SELECT * FROM productos")
#print(cursor)
productos = cursor.fetchall()
#print(productos)
for producto in productos:
    #print(producto)
    print("Titulo: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")
    

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone() #se trae solo el primer producto
print(producto)

#cerrar conexion (se debe cerar para que se guarden los cambios)
conexion.close()

