[`Backend con Python`](../Readme.md) > `Sesión 04`
# Sesión 4: Class Based Views y User Authentication


<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">

## :dart: Objetivos

- Utilizar Django Admin
- Configurar super user, y grupos de usuarios con Django Admin
- Emplear autenticaciones para restringir el acceso a usuarios específicos y proveer seguridad en la aplicación
- Utilizar Bootstrap para personalizar templates

### 📂 Organización de la clase
***


#### <ins>Tema 01: Django Admin</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

Durante la sesión anterior exploramos cómo realizar consultas a la base de datos utilizando la consola de Django. Sin embargo,  el uso del shell para gestionar los datos es demasiado técnico para los no programadores y la construcción de páginas web sería un proceso laborioso ya que nos veríamos repitiendo la misma lógica de vista y características de plantilla muy similares para cada tabla del modelo. Afortunadamente, una solución  a esto es Django Admin.


Django admin está escrito como una aplicación Django. Ofrece una interfaz web intuitiva para dar acceso administrativo a los datos del modelo. La interfaz de administración está diseñada para ser utilizada por los administradores del sitio web.



   - [**`EJEMPLO 01: Creando grupos en Django Admin`**](Ejemplo-01)


***
#### <ins>Tema 02: Class Based Views</ins>
<img src="img/imagen2.png" align="right" height="150" width="150">


Las vistas basadas en clases o class based views proporcionan una forma alternativa de implementar vistas como objetos de Python en lugar de funciones ya que las clases son más rápidas y fáciles de usar. Éstas no reemplazan a las vistas basadas en funciones ya que tienen ciertas diferencias y ventajas en comparación con ellas:

- La organización de código relacionado con los métodos HTTP específicos (GET, POST, etc) puede abordarse mediante métodos separados en lugar de bifurcación condicional.

- Se pueden utilizar técnicas orientadas a objetos como herencia múltiple para factorizar el código en componentes reutilizables.

  - [**`EJEMPLO 02: Creando grupos en Django Admin`**](Ejemplo-02)

***
#### <ins>Tema 03: Autenticación</ins>
<img src="img/imagen3.png" align="right" height="100" width="100">


Django proporciona un sistema de autenticación de usuarios. Maneja cuentas de usuarios, grupos, permisos y sesiones de usuario basadas en cookies. Además de la autenticación, también maneja la autorización: la autenticación verifica que un usuarios sea quien dice ser y la autorización determina qué tanto puede hacer un usuario autenticado. Con Django, el término autenticación se refiere a ambas tareas.

- El sistema de autenticación consta de:

  - Usuarios.
  - Permisos. Flags binarias que designan si un usuario puede realizar una determinada tarea.
Grupos. Para aplicar etiquetas y permisos a más de un usuario.
  - Un sistema de hash de contraseña configurable.
  - Formularios y herramientas de visualización para iniciar sesión en usuarios o restringir contenido.
Un sistema backend conectable.

 - [**`EJEMPLO 03: Definiendo y agregando autenticación de entrada usando vistas personalizadas y el modelo User de Django.`**](Ejemplo-03)


- [**`RETO 01:  Definiendo y agregando autenticación de salida con vistas personalizadas.`**](Reto-01)

- [**`EJEMPLO 04: Definiendo y agregando autenticación de entrada usando vistas predefinidas por Django.`**](Ejemplo-04)

- [**`RETO 02: Definiendo y agregando autenticación de salida usando vistas predefinidas por Django.`**](Reto-02)



***
#### <ins>Tema 04: Permisos y Autorización</ins>
<img src="img/imagen4.png" align="right" height="100" width="100">

El sistema de permisos incorporado a Django proporciona una forma de asignar permisos a usuario y grupos de usuarios específicos. Los permisos se pueden establecer no solo por tipo de objeto, sino también por instancia de objeto específico.

- has_view_permission()
- has_add_permission()
- has_change_permission()
- has_delete_permisission()


Con estos métodos es posible personalizar permisos para diferentes instancias de objetos del mismo tipo.


   - [**`EJEMPLO 05: : Definiendo elementos necesarios para otorgar permisos para eliminar datos.`**](Ejemplo-05)


***
#### <ins>Tema 05: Template Styling con Bootstrap</ins>
<img src="img/imagen5.png" align="right" height="100" width="100">

Bootstrap es un marco de trabajo de hojas de estilo en cascada (CSS) de código abierto que es particularmente bueno para el diseño de páginas responsivas que funcionan en los navegadores de escritorio y móviles.

Las plantillas cuentan con otra propiedad llamada herencias. Esto permite que elementos de una plantilla sean reutilizados en otra. En conjunto con bootstrap podemos usar ciertos elementos para facilitar la creación de elementos que se repiten en varias partes del sitio. Por ejemplo, una barra de navegación o un pie de página.


   - [**`EJEMPLO 06: Dando estilo a una plantilla con bootstrap`**](Ejemplo-06)


### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesión siguiendo un proyecto guiado.

- [**`POSTWORK SESIÓN 3`**](Postwork/Readme.md)


## Postwork
 - Aplicar los conceptos de la clase a tú Proyecto
   - [Ver lineamientos](Postwork)
