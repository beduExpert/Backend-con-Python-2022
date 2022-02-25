`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-05
## Operación CREATE: Agregando datos con Python MySQL

### OBJETIVO
Conocer el procedimiento para realizar la operación __CREATE__ en una tabla utilizando Python.

### REQUISITOS

Contar con los datos de conexión a la base de datos Biblioteca.

   __Host:__ localhost
   __User:__ Biblioteca \
   __Password:__ Biblioteca \
   __Base de datos:__ Biblioteca

Contar con la tabla __Libro__ creada y con datos muestra en la base de datos:

  ![Tabla Libro](assets/tabla-libro.jpg)



### DESARROLLO

#### Operación Create
***
 Crearemos un script `agrega-libro.py` y  otro llamado `modelomysql.py` para que se pueda agregar un nuevo registro a la tabla Libro en la base de datos Biblioteca desde la línea de comandos. Implementaremos los módulos `click`, `mysql-connector-python` y `modelomysql` así que asegurate de tenerlos instalados. 

Lo primero es realizar el archivo `modelomysql.py` con los parámetros de conexión especificados.
```python
# Datos de conexión a la base de datos
BD = {
    "database":"Biblioteca",
    "host":"localhost",
    "user":"Biblioteca",
    "password":"Biblioteca"
}

```
Como siguiente paso debemos generar una función para crear un conector a la base de datos.

```python
def conecta_bd():
    """
    Se conecta a la base de datos BD, regresa un conecto o None en caso
    de error.
    """
    try:
        conn = connect(**BD)
    except Error as err:
        print(err)
        return None

    return conn
```
El siguiente paso es agregar una función para obtener los registros de la tabla. primero nos conectamos a la BD con la función anteriormente definida

```python

def obtiene_registros(tabla):
    """
    Obtiene la lista de registros de tabla y los regresa en forma de lista
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SELECT * FROM {}".format(tabla)
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de campos y se agrega como primer posición en la
        # lista de resultados.
        registros = [[r[0].capitalize() for r in cur.description]]
        # Se obtiene la lista de resultados de la consulta SQL
        registros += cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []
```

Es importante resaltar que todos los comandos SQL, se deben de ejecutar dentro del cursor que generamos. Además, la consulta no se ejecutará hasta que no corramos el método `fetchall`

En este punto podemos probar nuestro script agregando la siguiente línea a nuestro script.

```python
if __name__ == "main":
   print(obtiene_registros("Libro"))
```
Ahora que nuestro script funciona adecuadamente procedemos a agregar una nueva función.

```python
def obtiene_tablas():
    """
    Obtiene la lista de tablas en la base de datos
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SHOW TABLES"
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de resultados de la consulta SQL
        registros = cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []
```
De la misma forma hacemos uso del cursor para correr el comando `SHOW TABLES`. Esta instrucción es dependiente del sistema gestor de base de datos que usemos. En el supuesto de que usaremos PostgresSQL el comando cambiaría.


Ejecuta el script sin argumento

```console
$ python agrega-libro.py
   Usage: agrega-libro.py [OPTIONS] TITULO EDITORIAL NUMPAG AUTORES
   Try "agrega-libro.py --help" for help.

   Error: Missing argument "TITULO".
```

Agregando un libro a la tabla

```console
   Sesion-02/Ejemplo-06 $ python agrega-libro.py "Un puente hacia el infinito" "Zeta Bolsillo" 409 1
   Se ha agregado el registro ('Un puente hacia el infinito', 'Zeta Bolsillo', 409, '1') a la tabla Libro

   Sesion-02/Ejemplo-06 $ python lista-registros.py Libro

   Tabla: Libro
   --------------
   Id | Titulo                      | Editorial     | Numpag | Autores
    1 | Yo, Robot                   | Gnome Press   |    374 |       1
    2 | El fin de la eternidad      | Gnome Press   |    191 |       1
    3 | El arte de la guerra        | Obelisco      |    112 |       2
    4 | Un puente hacia el infinito | Zeta Bolsillo |    409 |       1
   --------------
 ```
