`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-01
## Ejemplo 01: Bases de Datos
## Objetivo

- Conocer las bases de Datos Compatibles con Django
- Identificar los configuraciones necesarias en Django para trabajar con bases de datos.



## Desarrollo


#### Bases de Datos
***
La manera de gestionar estos datos es a través de un Sistema Gestor de Bases de Datos (SGBD), este consiste en un conjunto de programas utilizados para definir, administrar y procesar de una manera tanto práctica como eficiente una base de datos y sus aplicaciones.

Django soporta oficialmente las siguientes sistemas gestores de bases de datos:

- Postgresql
- MariaDB
- Mysql
- Oracle
- SQLite

Las bases de datos con las que trabajaremos siguen el __Modelo relacional__  Según el modelo relacional, los datos de una base de datos relacional se almacenan en relaciones, que el usuario percibe como tablas. Cada relación está compuesta por tuplas (registros) y atributos (campos).

#### Configuraciones de bases de Datos en Django
***
Para conectarse a las bases de datos Django integra una serie de configuraciones determinadas. De nuestro proyecto de la sesón anterior __Banco__ podemos analizar estar configuraciones.

Si abrimos el archivo `settings.py` y nos desplazamos al diccionario `DATABASES` nos encontraremos con el siguiente código

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Es importante identificar que DATABASES es un diccionario que contiene los parámetros de conexión que usará Django para conectarse a la base de datos principal de nuestro proyecto.

Comparemos algunos otros códigos de ejemplo para conectarnos a otras bases de datos.

Para conectarnos a __Postgresql__ usando la librería incluida con Django podemos usar el siguiente código. 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'service': 'my_service',
            'passfile': '.my_pgpass',
        },
    }
}
```

Como se mencionó antes. No existe un único paquete o forma para realizar estás conexiones. Otra librería muy utilizada es __pyscopg2__


```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '', # default is 5432
    }
}
```

> *__Nota:__ Las librerías que usamos para conectarnos a bases de datos son un tipo de API conocidas como DB API interface, y su funcionamiento está especificado en el estándar de Python PEP 249. Puedes revisarlo en el siguiente link: https://www.python.org/dev/peps/pep-0249/*

Dependiendo del tipo de base que usemos la configuración puede variar un poco. Asegurate de siempre revisar la documentación para estar informado de los cambios versión con versión: https://docs.djangoproject.com/en

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
```

#### ¡Felicidades! Ya conoces los fundamentos de Django :+1: :1st_place_medal:

