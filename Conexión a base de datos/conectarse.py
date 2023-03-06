import psycopg2

conexion = psycopg2.connect(host="localhost", database="Prueba", user="postgres", password="usuario", port='5432')
# Creamos el cursor con el objeto conexion
cur = conexion.cursor()
# Ejecutamos una consulta SQL
cur.execute( "SELECT nombre, apellidos FROM empleados" )

# Recorremos los resultados y los mostramos
for nombre, apellidos in cur.fetchall() :
    print (nombre, apellidos)

# Cerramos la conexión
conexion.close()