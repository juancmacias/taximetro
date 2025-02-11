import psycopg2
import conf.sql as pas_sql

connection = psycopg2.connect(f"postgresql://{pas_sql.user_sql}:{pas_sql.password_sql}@alpha.europe.mkdb.sh:5432/{pas_sql.table_sql}")
cursor = connection.cursor()
# borrar datos de la tabla
#sql ='''TRUNCATE TABLE usuarios'''
#cursor.execute(sql)

# crear tabla de precios si no existe 
sql ='''CREATE TABLE IF NOT EXISTS precios(
    id SERIAL PRIMARY KEY,
    estado CHAR(20) NOT NULL,
    precio FLOAT
)'''
cursor.execute(sql)
# crear tabla de trayectos si no existe 
sql ='''CREATE TABLE IF NOT EXISTS trayecto(
    id SERIAL PRIMARY KEY,
    fecha TIMESTAMP NOT NULL DEFAULT NOW(),
    precio DECIMAL(10,2) NOT NULL
)'''
cursor.execute(sql)
# crear tabla de usuarios si no existe 
sql ='''CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) UNIQUE NOT NULL
)'''
cursor.execute(sql)
# insertar datos
def insertar_sql(sql):
    cursor.execute(sql)
    connection.commit()

#insertar_sql('''INSERT INTO usuarios(nombre, usuario) VALUES('Juan', 'a94652aa97c7211ba8954dd15a3cf838')''')
#insertar_sql('''INSERT INTO precios(estado, precio) VALUES('parado', 0.02)''')
#insertar_sql('''INSERT INTO precios(estado, precio) VALUES('marcha', 0.05)''')

#cursor.execute("SELECT * FROM precios")

#for query in cursor:
#    print(query[2])

#query = cursor.execute("SELECT * FROM precios")
#cursor.close()