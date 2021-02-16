#from flask import Flask #importando flask
from flask import Flask, redirect, url_for, request, flash, render_template #modulos necesarios para redireccionar, la ultima render_template es para poder renderizar plantillas html (nota request es opcionas si vamos a hacer uso de comprobaciones o manipular elementos del mismo y flash para usar los mensajes flash)
from datetime import datetime #modulo para mostrar fecha
from flask_mysqldb import MySQL #importar driver de mysql previamente se debe instalarpor terminal el mismo con: pip3 install flask-mysqldb

app = Flask(__name__) #crear la aplicacion

app.secret_key = 'clave_secreta_flask' #clave secreta interna (necesaria para ciertas funciones entre ellas las sesiones de mensajes flash)

#conexion DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app) #itanciar la conexion


#context procesor

@app.context_processor #declarar un context processor (codigo que estara disponible todo el tiempo en la pagina cuando se le llame en una template, no importa si se recarga estara ahi)
def date_now():
    return {
        'now': datetime.utcnow() #now sera el nombre de variable de invocacion
    }


#endpoints

@app.route('/') #declarar ruta
def index(): #vinclar metodo a la ruta

    edad = 18
    personas = ['Miguel', 'Maria', 'Manuel', 'Mercedez']
    
    #return "Aprendiendo flask"
    return render_template('index.html', 
                            edad=edad,
                            personas=personas,
                            dato="valor", 
                            dato2="valor2", 
                            lista=["uno", "dos", "tres"]) #no hace falta indicarle que el diractorio es template el por defecto lo toma

#@app.route('/informacion/<nombre>') #pasar parametro por ruta
#@app.route('/informacion/<string:nombre>/<int:dato>')  #puedes usar el prefijo string para restringir que sera un dato estring o int para restringir que el parametro solo sera entero

@app.route('/informacion')
@app.route('/informacion/<nombre>') #se declaran turas necesarias para los parametros opcionales
@app.route('/informacion/<nombre>/<apellido>')
def informacion(nombre = None, apellido = None): #el parametro debe llamarse igual en la ruta como en la funcion, NOTA aqui hay parametros opcionales
    
    texto = ""
    if nombre != None and apellido != None:
        #texto= f"<h3>Bienvenido {nombre} {apellido}</h3>" #si lo quiero pasar asi se deberia usar la |safe en la plantilla despues de a variable
        texto= f"Bienvenido {nombre} {apellido}"

    return render_template('informacion.html', texto = texto) #de esta manera pasamos variables a las plantillas

    """
    return f"<h1>Página de información</h1>
    <p>Esta e una pagina de informacion</p>
    {texto}"
    """

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    if redireccion is not None:

        return redirect(url_for('lenguajes')) #asi podemos redireccionar en flask


    #return "<h1>Página de contacto</h1>"
    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    
    #return "<h1>Página de lenguajes</h1>"
    return render_template('lenguajes.html')


#añadir un coche
@app.route('/crear-coche', methods=['GET', 'POST']) #se debe pasar el parametro methods cuando se va a enviar daos al formulario en especioal si se uasra post
def crear_coche():
    
    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        
        #return f"{marca} {modelo} {precio} {ciudad}"

        #insertar datos
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)", (marca, modelo, precio, ciudad))
        cursor.connection.commit()
        flash(f'Has creado el coche {marca} {modelo} correctamente con el n° de regitro {cursor.lastrowid}')

        return redirect(url_for('index'))
        
    return render_template('crear-coche.html', titulo='Crear coche')


#lista de coches
@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches ORDER BY ID  DESC")
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coches.html', coches = coches)


#ver detalle del coche
@app.route('/coche/<int:id>')
def coche(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (id,))
    coche = cursor.fetchall()
    cursor.close()

    return render_template('coche.html', coche = coche[0]) #se coloca [0] porque el la consuta devuelce una tupla previa antes de la tupla de los datos


#borrar un coche
@app.route('/borrar-coche/<int:id>')
def borrar_coche(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM coches WHERE id = %s", (id,))
    cursor.connection.commit()
    cursor.close()

    flash(f'El coche n° {id} ha sido eliminado')


    return redirect(url_for('coches')) 


#editar un coche
@app.route('/editar-coche/<int:id>', methods=['GET', 'POST'])
def editar_coche(id):

    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE coches 
            SET marca = %s, 
                modelo = %s, 
                precio = %s, 
                ciudad = %s 
            WHERE id = %s
        """,(marca, modelo, precio, ciudad, id))
        
        cursor.connection.commit()
        flash(f'Has editado el coche {marca} {modelo} correctamente con el n° de regitro {id}')

        return redirect(url_for('coches'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (id,))
    coche = cursor.fetchall()
    cursor.close()

    return render_template('crear-coche.html', coche = coche[0], titulo='Editar coche') 


if __name__ == '__main__': #identifica que este archivo es el fichero principal
    app.run(debug=True) #le indicamos que se ejecutara la ejecucion en modo desarrollo