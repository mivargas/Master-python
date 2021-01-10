import mysql.connector

#conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="master_python" #si no se define se puede creara como abajo
)
#¿la conexion ha sido correcta?
#print(database)

#crear base de datos
cursor = database.cursor()
#rrsor = database.cursor(buffered=True) #necesario cuand hay muchas consultas de diferentes consas con el curso
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

print("--------------BASES DE DATOS------------------")
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)

#crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

print("--------------TABLAS DE MASTER_PYTHON------------------")
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


#insertar datos
#cursor.execute("INSERT INTO vehiculos VALUES (null, 'opel', 'astra', 18500)")

#insecion masiva
"""
coches =[
    ('seat', 'ibiza', 5000),
    ('renaut', 'clio', 15000),
    ('citroen', 'saxo', 2000),
    ('mercedez', 'clase c', 35000)
]
cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)", coches)
database.commit()
"""

#consultas
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
print("--------------TODOS MIS COCHES-------------------")
for coche in result:
    #print(coche)
    #print(coche[1])
    print("{} - {}".format(coche[1], coche[3]))

print("-------------CONDICIONAL WHERE MENOR O IGUAL A 5000-------------------")
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000.00")
result = cursor.fetchall()

for coche in result:
    print("{} - {}".format(coche[1], coche[3]))

#borrar
cursor.execute("DELETE FROM vehiculos WHERE marca='renaut'")
database.commit()
print(cursor.rowcount, "borrados!!") # me dice cantdad de registros borrados

#actuaizar
cursor.execute("UPDATE vehiculos SET modelo='leon' WHERE marca = 'seat'")
database.commit()
print(cursor.rowcount, "actualizados!!")
