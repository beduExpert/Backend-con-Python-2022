[`Backend con Python`](../Readme.md) > `Sesión 01`
# Sesión 1: Django Fundamentals

<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">


### :dart: Objetivos
- Identificar el uso de entornos virtuales y su aplicación.
- Instalar Django dentro de un entorno virtual.
- Construit una aplicación "Hola Mundo" aplicando los conceptos de rutas, vistas y plantillas.

### 📂 Organización de la clase
***

#### <ins>Entornos Virtuales</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

Comenzaremos con la configuración de un __entorno virtual__. Utilizaremos la herramienta de python *virtualenv* y *venv*. El comando dependerá de si utilizamos un sistema UNIX o windows.

Además, analizeremos la estructura de paquetes necesaria para manejar archivos del tipo requirements.txt e instalarlos cuando colaboremos en equipos de trabajo.

Los entornos virtuales se consideran una buena práctica que nos permite seprar nuestros paquetes de desarollo de los paquetes del sistema.

- [**`EJEMPLO 1`**](Ejemplo-01/Readme.md)

***

#### <ins>Estructura de un Proyecto en Django</ins>
<img src="img/imagen2.png" align="right" height="200" width="200">

Una vez que hemos configurado un entorno virtual e instalado Django, podemos comenzar con la creación de proyectos. Cada proyecto en Django contiene *Aplicaciones*. Una proyecto se compone de los siguientes archivos.

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

- [**`EJEMPLO 2`**](Ejemplo-02/Readme.md)
- [**`RETO 2`**](Reto-02/Readme.md)

***

#### <ins>Arquitectura MVT (Model,View,Template) </ins>
<img src="img/imagen3.png" align="right" height="200" width="200">

 Django sigue un paradigma llamado Model View Template (MVT).

1. Los Modelos (Model) de Django definen los datos de la aplicación y proporcionan una capa de abstracción al acceso a la base de datos.
1. Las Vistas (View) son en donde se define la mayor parte de la lógica de la aplicación. Cuando un usuario visita el sitio, se enviará solicitud para recuperar datos de las vistas.
1. Una plantilla (Templates) es un archivo de lenguaje de marcado de hipertexto (HTML) que contiene marcadores de posición especiales que se reemplazan por variables de la aplicación.


- [**`EJEMPLO 3`**](Ejemplo-03/Readme.md)

***

### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesión siguiendo un proyecto guidado.

- [**`POSTWORK SESIÓN 1`**](Postwork/Readme.md)

<br/>

[`Anterior`](../Readme.md) | [`Siguiente`](../Sesion-02/Readme.md)

