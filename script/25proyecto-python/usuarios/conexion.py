import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="master_python",
        port=3306
    )

    #print(database) #comprobar si se ha conectado
    cursor = database.cursor(buffered=True)

    return [database, cursor]