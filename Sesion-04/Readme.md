[`Backend con Python`](../Readme.md) > `Sesi贸n 04`
# Sesi贸n 4: Django Admins, Views y Templates


<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">

## :dart: Objetivos

- Utilizar Django Admin
- Configurar super user, y grupos de usuarios con Django Admin
- Emplear autenticaciones para restringir el acceso a usuarios espec铆ficos y proveer seguridad en la aplicaci贸n
- Utilizar Bootstrap para personalizar templates

### 馃搨 Organizaci贸n de la clase
***


#### <ins>Tema 01: Django Admin</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

Durante la sesi贸n anterior exploramos c贸mo realizar consultas a la base de datos utilizando la consola de Django. Sin embargo,  el uso del shell para gestionar los datos es demasiado t茅cnico para los no programadores y la construcci贸n de p谩ginas web ser铆a un proceso laborioso ya que nos ver铆amos repitiendo la misma l贸gica de vista y caracter铆sticas de plantilla muy similares para cada tabla del modelo. Afortunadamente, una soluci贸n  a esto es Django Admin.


Django admin est谩 escrito como una aplicaci贸n Django. Ofrece una interfaz web intuitiva para dar acceso administrativo a los datos del modelo. La interfaz de administraci贸n est谩 dise帽ada para ser utilizada por los administradores del sitio web.



   - [**`EJEMPLO 01: Creando grupos en Django Admin`**](Ejemplo-01)


***
#### <ins>Tema 02: Class Based Views</ins>
<img src="img/imagen2.png" align="right" height="150" width="150">


Las vistas basadas en clases o class based views proporcionan una forma alternativa de implementar vistas como objetos de Python en lugar de funciones ya que las clases son m谩s r谩pidas y f谩ciles de usar. 脡stas no reemplazan a las vistas basadas en funciones ya que tienen ciertas diferencias y ventajas en comparaci贸n con ellas:

- La organizaci贸n de c贸digo relacionado con los m茅todos HTTP espec铆ficos (GET, POST, etc) puede abordarse mediante m茅todos separados en lugar de bifurcaci贸n condicional.

- Se pueden utilizar t茅cnicas orientadas a objetos como herencia m煤ltiple para factorizar el c贸digo en componentes reutilizables.

  - [**`EJEMPLO 02: Vistas Basadas en Clases`**](Ejemplo-02)

***
#### <ins>Tema 03: Autenticaci贸n</ins>
<img src="img/imagen3.png" align="right" height="100" width="100">


Django proporciona un sistema de autenticaci贸n de usuarios. Maneja cuentas de usuarios, grupos, permisos y sesiones de usuario basadas en cookies. Adem谩s de la autenticaci贸n, tambi茅n maneja la autorizaci贸n: la autenticaci贸n verifica que un usuarios sea quien dice ser y la autorizaci贸n determina qu茅 tanto puede hacer un usuario autenticado. Con Django, el t茅rmino autenticaci贸n se refiere a ambas tareas.

- El sistema de autenticaci贸n consta de:

  - Usuarios.
  - Permisos. Flags binarias que designan si un usuario puede realizar una determinada tarea.
Grupos. Para aplicar etiquetas y permisos a m谩s de un usuario.
  - Un sistema de hash de contrase帽a configurable.
  - Formularios y herramientas de visualizaci贸n para iniciar sesi贸n en usuarios o restringir contenido.
Un sistema backend conectable.

 - [**`EJEMPLO 03: Definiendo y agregando autenticaci贸n de entrada usando vistas personalizadas y el modelo User de Django.`**](Ejemplo-03)


- [**`RETO 01:  Definiendo y agregando autenticaci贸n de salida con vistas personalizadas.`**](Reto-01)

- [**`EJEMPLO 04: Definiendo y agregando autenticaci贸n de entrada usando vistas predefinidas por Django.`**](Ejemplo-04)

- [**`RETO 02: Definiendo y agregando autenticaci贸n de salida usando vistas predefinidas por Django.`**](Reto-02)



***
#### <ins>Tema 04: Permisos y Autorizaci贸n</ins>
<img src="img/imagen4.png" align="right" height="100" width="100">

El sistema de permisos incorporado a Django proporciona una forma de asignar permisos a usuario y grupos de usuarios espec铆ficos. Los permisos se pueden establecer no solo por tipo de objeto, sino tambi茅n por instancia de objeto espec铆fico.

- has_view_permission()
- has_add_permission()
- has_change_permission()
- has_delete_permisission()


Con estos m茅todos es posible personalizar permisos para diferentes instancias de objetos del mismo tipo.


   - [**`EJEMPLO 05: : Definiendo elementos necesarios para otorgar permisos para eliminar datos.`**](Ejemplo-05)


***
#### <ins>Tema 05: Template Styling con Bootstrap</ins>
<img src="img/imagen5.png" align="right" height="100" width="100">

Bootstrap es un marco de trabajo de hojas de estilo en cascada (CSS) de c贸digo abierto que es particularmente bueno para el dise帽o de p谩ginas responsivas que funcionan en los navegadores de escritorio y m贸viles.

Las plantillas cuentan con otra propiedad llamada herencias. Esto permite que elementos de una plantilla sean reutilizados en otra. En conjunto con bootstrap podemos usar ciertos elementos para facilitar la creaci贸n de elementos que se repiten en varias partes del sitio. Por ejemplo, una barra de navegaci贸n o un pie de p谩gina.


   - [**`EJEMPLO 06: Dando estilo a una plantilla con bootstrap`**](Ejemplo-06)


### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesi贸n siguiendo un proyecto guiado.

- [**`POSTWORK SESI脫N 4`**](Postwork/Readme.md)
