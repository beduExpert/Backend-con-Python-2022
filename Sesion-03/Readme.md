[`Backend con Python`](../Readme.md) > `Sesión 03`
# Sesión 3: Modelos, migraciones, consultas y forms

<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">

## :dart: Objetivos

- Programar consultas mediante el shell de Django.
- Construir vistas que hagan uso de los modelos logrando páginas con información dinámica.
- Hacer uso de tablas en un modelo relacional creando relaciones entre estas e implementando formularios.

### 📂 Organización de la clase
***


#### <ins>Tema 01: Modelos en Django</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

Un modelo en Django es un tipo de objeto especial que se guarda en la base de datos. De acuerdo a la documentación oficial de Django, ésta define a un modelo como la fuente única y definitiva de información sobre los datos. Contiene campos y comportamientos esenciales de los datos que se están almacenando. Generalmente, cada modelo se asigna a una sola tabla de base de datos.


   - [**`EJEMPLO 01: Creando una tabla con el modelo de datos de Django`**](Ejemplo-01)
   - [**`RETO 01: Creando una tabla con el modelo de datos de Django`**](Reto-01)

***
#### <ins>Tema 02: Crear relaciones con el modelo de datos de Django</ins>
<img src="img/imagen2.png" align="right" height="150" width="150">


En una base de datos relacionales, puede haber los siguientes tipos de relaciones

- De muchos a uno
- De muchos a muchos
- Uno a uno

Esta es una de las ventajas de las bases de datos relacionales que tienen la capacidad de establecer relaciones entre los datos almacenados en las tablas.

Las relaciones ayudan a mantener la integridad de los datos al establecer las referencias correctas entre las tablas, lo que a su vez ayuda a mantener la base de datos. Las reglas de relación, por su parte, garantizan la coherencia de los datos y eviten los duplicados.

   - [**`EJEMPLO 02:  Creando relaciones con el modelo de datos de Django`**](Ejemplo-02)
   - [**`RETO 02: Creando relaciones con el modelo de datos de Django`**](Reto-02)

***
#### <ins>Tema 03: Definir las consultas usando el ORM de Django</ins>
<img src="img/imagen3.png" align="right" height="100" width="100">


Django incluye una capa de mapeo relacional de objetos predeterminada que se puede usar para interactuar con datos de aplicaciones de varias bases de datos relacionales.

¿Qué es ORM?

Object Relational Mapping (modelo de objeto relacional) es un modelo de programación que transforma los datos de un objeto a un formato adecuado para poder guardar toda esa información en una base de datos mapeándolos.  Entre sus ventajas:

Facilidad y velocidad de uso.
Abstracción de la base de datos utilizada.
Seguridad de la capa de acceso de datos contra ataques.

Aunque también cuenta con desventajas:

En entornos con gran carga, poner una capa más en el proceso puede afectar el rendimiento.
Aprende el nuevo lenguaje del ORM.



   - [**`EJEMPLO 03: Definiendo las consultas usando el ORM de Django`**](Ejemplo-03)
   - [**`RETO 03: Definiendo las consultas usando el ORM de Django`**](Reto-03)

***
#### <ins>Tema 04: Realizar Consultas en las plantillas de Django</ins>
<img src="img/imagen4.png" align="right" height="100" width="100">

Una vez que se tiene un objeto Template compilado, se puede renderizar un contexto con él. Puedes reutilizar la misma plantilla para renderizarla varias veces con diferentes contextos. Incluso si los datos que queremos presentar deben actualizarse o recuperarse desde nuestra base datos.Mediante el uso de los métodos para recuperación de datos por ejemplo all( ) podemos construir plantillas que recuperen información.



   - [**`EJEMPLO 04: : Realizar una consulta a la base de datos mediante una plantilla.`**](Ejemplo-04)
   - [**`RETO 04: El sistema de plantillas de Django`**](Reto-04)

***
#### <ins>Tema 05: Definir e implementar formularios en la aplicación</ins>
<img src="img/imagen5.png" align="right" height="100" width="100">

Un formulario HTML es una colección de elementos internos representados mediante la etiqueta `<form>` que permite al usuario hacer cosas como ingresar texto, seleccionar opciones, manipular objetos o controles y luego enviar esa información al servidor.

Algunos de estos elementos de la interfaz de formulario (entrada de texto o casillas de verificación) están integrados en el propio HTML. Otros son mucho más complejos; una interfaz que muestra un selector de fechas o que permite mover un control deslizante o manipular controles normalmente requiere de JavaScript y CSS, así como de elementos `<input>` del formulario HTML para lograr estos efectos.


   - [**`EJEMPLO 05: Definiendo y agregando una página con formulario de la aplicación web`**](Ejemplo-05)


### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesión siguiendo un proyecto guiado.

- [**`POSTWORK SESIÓN 3`**](Postwork/Readme.md)
