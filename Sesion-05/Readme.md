[`Backend con Python`](../Readme.md) > `Sesi贸n 05`
# Sesi贸n 5: Django Rest framework, ( serializadores, generic field, viewsets)


<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">

## :dart: Objetivos

- Utilizar Django Rest Framework
- Construir una API para realizar operaciones CRUD a los modelos de un proyecto usando Django Rest Framework


### 馃搨 Organizaci贸n de la clase
***


#### <ins> Django REST Framework</ins>
<img src="img/imagen3.png" align="right" height="100" width="100">

Las aplicaciones web suelen tener el frontend creado con una biblioteca completamente independiente, como ReactJS o AngularJS. Estas bibliotecas proporcionan herramientas poderosas para construir interfaces de usuario din谩micas; sin embargo, no se comunican directamente con nuestro c贸digo o base de datos de backend Django. El c贸digo frontend simplemente se ejecuta en el navegador web y no tiene acceso directo a ning煤n dato en nuestro servidor backend. Por lo tanto, necesitamos crear una forma para que estas aplicaciones "hablen" con nuestro c贸digo backend. Una de las mejores maneras de hacer esto en Django es mediante el uso de API REST.


Django cuenta con un framework que permite realizar nuestra propia API RESTful de una manera sencilla, se trata de Django REST Framework. A continuaci贸n conoceremos m谩s sobre esta herramienta, desde conceptos b谩sicos, como qu茅 es un framework, hasta comprender su funcionamiento con el objetivo de adquirir los conocimientos necesarios para desarrollar una API REST por cuenta propia utilizando este framework.


   - [**`EJEMPLO 01: Configuraci贸n inicial DRF`**](Ejemplo-01)


***
#### <ins>API REST</ins>
<img src="img/imagen2.png" align="right" height="150" width="150">

API significa Interfaz de programaci贸n de aplicaciones. Las API se utilizan para facilitar la interacci贸n entre diferentes piezas de software, y se comunican mediante HTTP (Protocolo de transferencia de hipertexto). Este es el protocolo est谩ndar para la comunicaci贸n entre servidores y clientes y es fundamental para la transferencia de informaci贸n en la web. Las API reciben solicitudes y env铆an respuestas en formato HTTP.


- [**`EJEMPLO 02: Creando un API para realizar las operaciones CRUD de una tabla tipo cat谩logo`**](Ejemplo-02)

- [**`RETO 01`**](Reto-01)

- [**`EJEMPLO 03: Implementando las relaciones una tabla con relaciones uno a muchos.`**](Ejemplo-03)

- [**`EJEMPLO 04: Visualizando las relaciones de una tabla en la API`**](Ejemplo-04)




### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesi贸n siguiendo un proyecto guiado.

- [**`POSTWORK SESI脫N 5`**](Postwork/Readme.md)

