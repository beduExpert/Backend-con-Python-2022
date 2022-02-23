`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Ejemplo-01
## Ejemplo 01: Django
## Objetivo

- Conocer Django
- Identificar los casos de usos de Django
- Identificar la estructura de un app Web en Django


## Desarrollo


#### Django
***
Cuando se habla de framewoks web web, se suele pensar en marcos JavaScript frontend como ReactJS, Angular o Vue. Estos frameworks se utilizan para mejorar o agregar interactividad a las páginas web ya generadas. Django se encuentra en la capa debajo de estas herramientas y es responsable de enrutar una URL, obtener datos de las bases de datos, interpretar plantillas y manejar la entrada de formularios de los usuarios.

Instalación de Django
Esta es la forma recomendada de instalar Django.
1. Instalar pip. Lo más fácil es usar el instalador pip. Si ya tienes pip instalado, es posible que debas actualizarlo si está desactualizado.
```
python -m pip install Django
```
Para verificar que tu intérprete de Python puede utilizar Django utiliza el siguiente código:
```
python
>>> import django
>>> print(django.get_version())
```
Adicionalmente es aconsejable instalar el paquete colorama. Este paquete nos ayudará a resaltar la sintaxis de Django cuando estemos utilizando la terminal.
```
python -m pip install colorama
```
Instalación de un entorno virtual venv. Esta herramienta proporciona entornos de Python aislados, que son más prácticos que instalar paquetes en todo el sistema. También permite instalar paquetes sin privilegios de administrador.

```
python -m pip install virtualenv
```
#### ¿Dónde se utiliza Django? 
***
Para crear aplicaciones web altamente escalables con una audiencia en constante crecimiento (por ejemplo, sitios de noticias), Django es uno de los frameworks web más populares de Python. Django es claro y simple, rápido y confiable, flexible y escalable. Django tiene una gran comunidad de contribuyentes leales. Según SimilarTech, había 77, 278 sitios web construidos con Django a partir de mayo de 2019. A continuación se sition algunos de los sitio web que han crecido y evolucionado utilizando Django.

![](img/Ejemplo1_1.jpg)

1. Instragram. De acuerdo con el post publicado por Instragram Engineering. Es el sitio más grande publicado en Django.Link:https://instagram-engineering.com/web-service-efficiency-at-instagram-with-python-4976d078e366

2. The Washington Post https://www.washingtonpost.com/ , Utiliza una versión llamada DJango CMS. que es utilizada por otros sitios como National Geographic, PBS y la NAsa. https://www.django-cms.org/en/

3. Reddit https://www.reddit.com/

#### ¡Felicidades! Ya conoces los fundamentos de Django :+1: :1st_place_medal:

