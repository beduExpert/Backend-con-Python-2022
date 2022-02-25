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

Podemos probar nuestro código de la misma forma que lo hicimos con la función anterior.
```python
if __name__ == "main":
   print(obtiene_tablas("Libro"))
```

Las funciones que acabamos de definir interactuaran con los archivos `lista-registros.py` y `stdout.py`.

El primero importa las funciones de nuestro archivo de modelos y verifica la existencia de una tabla como parámetro en caso de existir. Nos mostrará la información de la tabla y en caso contrario las tablas disponibles para consultarse.



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Archivo lista registros.py 

import click
from modelomysql import obtiene_registros, obtiene_tablas
from stdout import imprime_registros

@click.command()
@click.argument("tabla", required=False)
def lista_registros(tabla):
    """
    Imprime la lista de registros de TABLA  en la salida estándar, si no se
    proporciona una tabla, se imprime la Lista de tablas disponibles.
    """
    if tabla:
        # Se obtiene la lista de registros de tabla
        registros = obtiene_registros(tabla)
        # Se imprimen los registros en formato texto en la salida estándar
        imprime_registros(registros, "Tabla: {}".format(tabla))
    else:
        tablas = obtiene_tablas()
        imprime_registros(tablas, "Tablas disponibles")

if __name__ == '__main__':
    lista_registros()
```

Analizando el archivo `stdout.py` podemos observar que este script realiza un formateo a los resultados de los registros.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo encargado de realizar imprimir información a la salida estándar (STDOUT)
"""

def imprime_registros(registros, titulo=None):
    """
    Imprime la lista de registros en la salida estándar en formato texto, cada
    registro es de tipo lista.

    titulo - Es de tipo str y si es proporcionado se imprime como título
    """
    # Se calcula el ancho máximo para cada columna
    anchos = [[len(str(campo)) for campo in reg] for reg in registros]
    anchos = [max(col) for col in zip(*anchos)]

    # Se imprime la lista
    print()
    if titulo: print(titulo)
    print("-" * len(titulo))
    for reg in registros:
        # Se formatea cada registro en una línea de texto
        reg = zip(reg, anchos)
        reg = ["{:{}}".format(*campo) for campo in reg]
        print(" | ".join(reg))
    print("-" * len(titulo))
    print()
```

Finalmente podemos ejecutar el script `agrega-libro.py`

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import agrega_registro


@click.command()
@click.argument("titulo")
@click.argument("editorial")
@click.argument("numpag", type=int)
@click.argument("autores")
def agrega_usuario(titulo, editorial, numpag, autores):
    """
    Agrega un nuevo registro a la tabla Libro con los campos TITULO,
    EDITORIAL, NUMPAG y AUTORES. Imprime un mensaje si el registro se agrega
    exitosamente a la tabla.
    """
    tabla = "Libro"
    registro = (titulo, editorial, numpag, autores)
    if agrega_registro(tabla, registro):
        print("Se ha agregado el registro {} a la tabla {}".format(
            registro, tabla))

if __name__ == '__main__':
    agrega_usuario()
```

El resultado de ejecutar el al script sin ningún parámetro debería ser el siguiente.

```console
$ python agrega-libro.py
   Usage: agrega-libro.py [OPTIONS] TITULO EDITORIAL NUMPAG AUTORES
   Try "agrega-libro.py --help" for help.

   Error: Missing argument "TITULO".
```

Agregando un libro a la tabla

```console
   $ python agrega-libro.py "Un puente hacia el infinito" "Zeta Bolsillo" 409 1
   Se ha agregado el registro ('Un puente hacia el infinito', 'Zeta Bolsillo', 409, '1') a la tabla Libro

   $ python lista-registros.py Libro

   Tabla: Libro
   --------------
   Id | Titulo                      | Editorial     | Numpag | Autores
    1 | Yo, Robot                   | Gnome Press   |    374 |       1
    2 | El fin de la eternidad      | Gnome Press   |    191 |       1
    3 | El arte de la guerra        | Obelisco      |    112 |       2
    4 | Un puente hacia el infinito | Zeta Bolsillo |    409 |       1
   --------------
 ```
