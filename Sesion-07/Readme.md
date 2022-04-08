[`Backend con Python`](../Readme.md) > `Sesión 07`
# Sesión 7: Deploy: Pythonanywhere y AWS
<img src="img/pizarron.png" align="right" height="100" width="100" hspace="10">

## :dart: Objetivos

- Utilizar proveedores de infraestructura para publicar una aplicación web.
- Configurar una aplicación wev para producción
- Programar el entorno de producción en el proveedor para ejecutar una aplicación web


### 📂 Organización de la clase
***
#### <ins>Tema 01: Deploy</ins>
<img src="img/imagen1.png" align="right" height="100" width="100">

Una vez que tengas un sitio web en funcionamiento o una aplicación reutilizable, querrás hacerla pública. La implementación y despliegue de sitios web es una de las actividades de desarrollo más difíciles con Django, porque hay muchas partes moviendose.

- Administrar el servidor web.
- Configuración de la base de datos.
- Servicio de archivos estáticos y multimedia.
- Configuración del almacenamiento en caché.
- Configuración del envío de correo electrónico.
- Administrar dominios.

Dependiendo de la escala y complejidad del proyecto en equipos más grandes, todas esas tareas las realizan ingenieros de DevOps y requieren habilidades como comprensión de la arquitectura de redes, administración de servidores Linux, bash scripting, usar vim, etc.


  - [**`EJEMPLO 01: Proveedores, requisitos, registro y bases de datos.`**](Ejemplo-01)


***
#### <ins>Tema 02: Pythonanywhere</ins>
<img src="img/imagen2.png" align="right" height="150" width="150">


Implementar un proyecto de Django en PythonAnywhere es muy parecido a ejecutar un proyecto de Django en nuestra propia PC.

Usaremos un virtualenv, al igual que en nuestra PC.  Tendremos una copia de nuestro código en PythonAnywhere. La principal diferencia es que, en lugar de usar el servidor de desarrollo de Django con manage.py  el servidor de ejecución se creará en lo que llamamos una aplicación web a través de la pestaña Web en nuestra interfaz de usuario y luego lo configurará con un archivo WSGI.


  - [**`EJEMPLO 02: Preparando entorno de producción en el hospedaje del Proveedor. `**](Ejemplo-02)
  - [**`EJEMPLO 03: El archivo settings.py para desarrollo y producción.`**](Ejemplo-03)
  - [**`Reto 01: Carga de proyecto en PythonAnywhere.`**](Reto-01)
  - [**`EJEMPLO 04: Archivos estáticos y base de datos en producción `**](Ejemplo-04)

***
#### <ins>Tema 03: AWS</ins>
<img src="img/imagen3.png" align="right" height="100" width="130">


Amazon Web Services (AWS abreviado) es una colección de servicios de computación en la nube pública (también llamados servicios web) que en conjunto forman una plataforma de computación en la nube, ofrecidas a través de Internet por Amazon.com. Es usado en aplicaciones populares como Dropbox, Foursquare, HootSuite. Es una de las ofertas internacionales más importantes de la computación en la nube.

 - [**`EJEMPLO 05: AWS ElasticBeanstalk`**](Ejemplo-05)
 - [**`Reto 02: Carga de proyecto en AWS ElacticBeanstalk.`**](Reto-02)

### Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesión siguiendo un proyecto guiado.

- [**`POSTWORK SESIÓN 7`**](Postwork/Readme.md)
