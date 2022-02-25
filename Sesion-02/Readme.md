# Sesión 2: Bases de datos SQL para Django

<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">


### :dart: Objetivos
- Identificar el uso de entornos virtuales y su aplicación.
- Instalar Django dentro de un entorno virtual.
- Construir una aplicación "Hola Mundo" aplicando los conceptos de rutas, vistas y plantillas.

### 📂 Organización de la clase
***


#### <ins>Tema 01: Bases de Datos</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

Django es un framework de alto nivel, gratuito y de código abierto que permite el desarrollo rápido de sitios web seguros y mantenibles. Al ser open source, tiene una comunidad próspera y activa, gran documentación y muchas opciones de soporte gratuito y de pago.

Django se encarga en gran medida de las complicaciones del desarrollo web, utilizar este framework permite crear código:


- Inicializando Django con SQLite3
   - [Ejemplo 01](Ejemplo-01)
 - Inicializando Django con MySQL
   - [Ejemplo 02](Ejemplo-02)
 - Inicializando Django con PostgreSQL
   - [Ejemplo 03](Ejemplo-03)

***


#### <ins>Tema 02: SQL y operaciones CRUD</ins>
<img src="img/imagen2.jpg" align="right" height="100" width="100">

El MVT (Model View Template) es un patrón de diseño de software. Es una colección de tres componentes importantes Vista de modelo y Plantilla. El modelo ayuda a manejar la base de datos. Es una capa de acceso a datos que maneja los datos. La plantilla es una capa de presentación que maneja completamente la parte de la interfaz de usuario. La vista se utiliza para ejecutar la lógica empresarial e interactuar con un modelo para transportar datos y representar una plantilla.

Inicializando un servidor MariaDB y una base de datos haciendo uso de  Contenedores
   - [Ejemplo 04](Ejemplo-04)
   - [Reto 01](Reto-01)
 - Operación READ: Lectura de datos con Python y MariaDB
   - [Ejemplo 05](Ejemplo-05)
   - [Reto 02](Reto-02)
 - Operación CREATE: Agregando datos con Python y MariaDB
   - [Ejemplo 06](Ejemplo-06)
 - Operación UPDATE: Modificando datos con Python y MariaDB
   - [Reto 03](Reto-03)

***


#### <ins>Tema 03: Conexiones a bases de datos SQL</ins>
<img src="img/imagen3.png" align="right" height="100" width="100">

Comenzaremos con la configuración de un __entorno virtual__. Utilizaremos la herramienta de python *virtualenv* y *venv*. El comando dependerá de si utilizamos un sistema UNIX o windows.

Además, analizaremos la estructura de paquetes necesaria para manejar archivos del tipo requirements.txt e instalarlos cuando colaboremos en equipos de trabajo.

Los entornos virtuales se consideran una buena práctica que nos permite seprar nuestros paquetes de desarollo de los paquetes del sistema.

- [**`EJEMPLO 3`**](Ejemplo-03/Readme.md)
- [**`RETO 1`**](Reto-01/Readme.md)

***

#### <ins>Tema 04: Introducción a las migraciones</ins>
<img src="img/imagen4.png" align="right" height="200" width="200">

Una vez que hemos configurado un entorno virtual e instalado Django, podemos comenzar con la creación de proyectos. Cada proyecto en Django contiene *Aplicaciones*. Un proyecto se compone de los siguientes archivos.

```console
mi_sitio/
    manage.py
    mi_sitio/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Cada aplicación que escribes en Django consiste en un paquete de Python que sigue una determinada convención. Django viene con una utilidad que genera automáticamente la estructura de directorios básica de una aplicación, por lo que podemos centrarnos en escribir código en lugar de crear directorios.

- [**`EJEMPLO 4`**](Ejemplo-04/Readme.md)
- [**`RETO 2`**](Reto-02/Readme.md)


***

### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesión siguiendo un proyecto guiado.

- [**`POSTWORK SESIÓN 1`**](Postwork/Readme.md)

<br/>



`Fullstack con Python` > [`Backend con Python`](../Readme.md) > `Sesión 02`
