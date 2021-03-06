[`Backend con Python`](../Readme.md) > `Sesi贸n 06`
# Sesi贸n 6: Middleware & GraphQL


<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">

## :dart: Objetivos

- Utilizar APIs GraphQL
- Configurar Graphene
- Emplear modulos de middleware para integrar sesiones

### 馃搨 Organizaci贸n de la clase
***


#### <ins>Tema 01: GraphQL</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

GraphQL es un lenguaje de consulta para API's y un tiempo de ejecuci贸n del lado del servidor para ejecutar consultas utilizando un sistema de tipos definidos para los datos. GraphQL no est谩 vinculado a ninguna base de datos o motor de almacenamiento espec铆fico y, en cambio, est谩 respaldado por su c贸digo y datos existentes.

  - Describir los datos proporcionados por un servidor en un esquema de tipo est谩ticos.
  - Solicitar datos en una consulta que describa exactamente sus requisitos de datos.
  - Recibir datos en una respuesta que contenga solo los datos que solicit贸.

  - [**`EJEMPLO 01: GraphQL`**](Ejemplo-01)
  - [**`RETO 01: Realizando consultas en GraphQL`**](Reto-01)


***
#### <ins>Tema 02: Graphene</ins>
<img src="img/imagen2.png" align="right" height="150" width="150">


Graphene es una biblioteca que proporciona herramientas para implementar una API GraphQL en Python utilizando un enfoque de "c贸digo primero".


En lugar de escribir lenguaje de definici贸n de esquemas GraphQL (SDL), escribimos c贸digo Python para describir los datos proporcionados por el servidor.

Graphene est谩 completamente equipado con integraciones para los marcos web y ORM m谩s populares. Graphene produce esquemas que cumplen totalmente con la especificaci贸n GraphQL y tambi茅n proporciona herramientas y patrones para crear una API compatible con Relay.

Primero se env铆a una consulta solicitando solo un campo (hello) y se especifica un valor para el argumento name.


  - [**`EJEMPLO 02: Definiendo esquemas para crear un API GraphQL y realizar consultas de datos`**](Ejemplo-02)
  - [**`RETO 02: Definiendo esquemas para crear un API GraphQL y realizar consultas de datos`**](Reto-02)
  - [**`EJEMPLO 03: Mutaciones`**](Ejemplo-03)
  - [**`RETO 03: Definiendo mutaciones (operaciones) para el API GraphQL`**](Reto-03)

***
#### <ins>Tema 03: Middleware</ins>
<img src="img/imagen3.png" align="right" height="100" width="100">


Middleware en Django se refiere a una variedad de componentes de software que intervienen en este proceso de solicitudes y sus respuestas para integrar funcionalidades importantes como la seguridad, la administraci贸n de sesiones o la autenticaci贸n. Por lo tanto, cuando escribimos una vista en Django, no tenemos que establecer expl铆citamente una funci贸n de seguridad escrita por nosotros. Por ejemplo,  la instancia de SecurityMiddleware realiza autom谩ticamente las configuraciones de seguridad al devolver la respuesta.

La implementaci贸n de los componentes de middleware permiten realizar diferentes preprocesamientos de forma autom谩timatica, de esta forma nos aseguramos de que nuestras vistas no est茅n abarrotadas c贸digo repetitivo y podemos concentrarnos en codificar la l贸gica de la aplicaci贸n en lugar de preocuparnos por el comportamiento del servidor de bajo nivel.

La filosof铆a que utiliza Django para la implementaci贸n del middleware es implementar un stack de middleware que permite que estos componentes sean opcionales y reemplazables.



 - [**`EJEMPLO 04: Manejo de Sesiones`**](Ejemplo-04)

### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesi贸n siguiendo un proyecto guiado.

- [**`POSTWORK SESI脫N 6`**](Postwork/Readme.md)


