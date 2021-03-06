[`Backend con Python`](../Readme.md) > `Sesi贸n 01`
# Sesi贸n 1: Django Fundamentals

<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">


### :dart: Objetivos
- Identificar el uso de entornos virtuales y su aplicaci贸n.
- Instalar Django dentro de un entorno virtual.
- Construir una aplicaci贸n "Hola Mundo" aplicando los conceptos de rutas, vistas y plantillas.

### 馃搨 Organizaci贸n de la clase
***


#### <ins>Tema 01: Django</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

Django es un framework de alto nivel, gratuito y de c贸digo abierto que permite el desarrollo r谩pido de sitios web seguros y mantenibles. Al ser open source, tiene una comunidad pr贸spera y activa, gran documentaci贸n y muchas opciones de soporte gratuito y de pago.

Django se encarga en gran medida de las complicaciones del desarrollo web, utilizar este framework permite crear c贸digo:
-   Completo.
-   Vers谩til.
-   Seguro.
-   Escalable.

- [**`EJEMPLO 1`**](Ejemplo-01/Readme.md)

***


#### <ins>Tema 02: Fundamentos de arquitectura MVT ( Model, View, Template)</ins>
<img src="img/imagen2.jpg" align="right" height="100" width="100">

El MVT (Model View Template) es un patr贸n de dise帽o de software. Es una colecci贸n de tres componentes importantes Vista de modelo y Plantilla. El modelo ayuda a manejar la base de datos. Es una capa de acceso a datos que maneja los datos. La plantilla es una capa de presentaci贸n que maneja completamente la parte de la interfaz de usuario. La vista se utiliza para ejecutar la l贸gica empresarial e interactuar con un modelo para transportar datos y representar una plantilla.

- [**`EJEMPLO 2`**](Ejemplo-02/Readme.md)

***


#### <ins>Tema 03: Entornos virtuales e instalaci贸n de Django</ins>
<img src="img/imagen3.png" align="right" height="100" width="100">

Comenzaremos con la configuraci贸n de un __entorno virtual__. Utilizaremos la herramienta de python *virtualenv* y *venv*. El comando depender谩 de si utilizamos un sistema UNIX o windows.

Adem谩s, analizaremos la estructura de paquetes necesaria para manejar archivos del tipo requirements.txt e instalarlos cuando colaboremos en equipos de trabajo.

Los entornos virtuales se consideran una buena pr谩ctica que nos permite seprar nuestros paquetes de desarollo de los paquetes del sistema.

- [**`EJEMPLO 3`**](Ejemplo-03/Readme.md)
- [**`RETO 1`**](Reto-01/Readme.md)

***

#### <ins>Tema 04: Construir aplicaci贸n base de Django</ins>
<img src="img/imagen4.png" align="right" height="200" width="200">

Una vez que hemos configurado un entorno virtual e instalado Django, podemos comenzar con la creaci贸n de proyectos. Cada proyecto en Django contiene *Aplicaciones*. Un proyecto se compone de los siguientes archivos.

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

Cada aplicaci贸n que escribes en Django consiste en un paquete de Python que sigue una determinada convenci贸n. Django viene con una utilidad que genera autom谩ticamente la estructura de directorios b谩sica de una aplicaci贸n, por lo que podemos centrarnos en escribir c贸digo en lugar de crear directorios.

- [**`EJEMPLO 4`**](Ejemplo-04/Readme.md)
- [**`RETO 2`**](Reto-02/Readme.md)

***

#### <ins>Tema 05: Agregar p谩gina a la aplicaci贸n web mediante una plantilla</ins>
<img src="img/imagen5.png" align="right" height="200" width="200">

 Django sigue un paradigma llamado Model View Template (MVT).

1. Los Modelos (Model) de Django definen los datos de la aplicaci贸n y proporcionan una capa de abstracci贸n al acceso a la base de datos.
1. Las Vistas (View) son en donde se define la mayor parte de la l贸gica de la aplicaci贸n. Cuando un usuario visita el sitio, se enviar谩 solicitud para recuperar datos de las vistas.
1. Una plantilla (Templates) es un archivo de lenguaje de marcado de hipertexto (HTML) que contiene marcadores de posici贸n especiales que se reemplazan por variables de la aplicaci贸n.


- [**`EJEMPLO 5`**](Ejemplo-05/Readme.md)

***

### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesi贸n siguiendo un proyecto guiado.

- [**`POSTWORK SESI脫N 1`**](Postwork/Readme.md)

<br/>

