[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Postwork
## Postwork 03: Creación de un modelo e inserción de datos mediante Django Admin.

### Objetivo
- Crear las tablas de tu aplicación BEDUFLIX con el modelo de datos de Django
- Registrar un usuario admin en Django
- Ingresar un nuevo usuario usando Django Admin CRUD
- Recuperar la información mediante una consulta.

### Desarrollo

Para este Postwork continuaremos con la creación de nuestra aplicación BEDUFLIX es importante que tengas completos los archivos que generaste en los postwork anteriores.

Vamos a generar un modelo que corresponda a la aplicación BEDUFLIX, incluiremos campos de relevancia para almacenar las películas y los perfiles de usuario.

Además utilizaremos Django Admin para agregar un usuario.  Aplicaremos una inserción de datos mediante el uso del administrador de Django y posteriormente verificaremos que la información exista mediante una consulta en el shell de Django.

Finalmente agregaremos una pantalla de bienvenida al proyecto.

#### Asegúrate de comprender:
- Cómo se registra un modelo en Django y cómo se especifican los tipos de datos.
- Qué relación tiene un modelo con las migraciones y los archivos del proyecto de Django
- La estructura de archivos que sigue un proyecto de Django
- Los usuarios administradores de Django y su relación con el panel de administrador
- La consultas desde el shell de Django.



Indicaciones generales

1. Registra los modelos de la base de datos utilizando el diagrama entidad relación dado.Contempla  todos los campos y relaciones:

__Diagrama entidad relación para la app BEDUFLIX__

![](er-beduflix.png)

__Tabla CustomUser:__
- username: longitud máxima 40 y de tipo CharField.
- email: campo validado para email
- Define la representación en string regresando el username y el email.

__Tabla Perfil:__

- nombre: longitud máxima 255 y de tipo CharField.
- apellidos: longitud máxima 80, con opción para ser null.
- fechaNacimiento: una fecha con el tipo de dato para fecha
- genero:campo de tipo opción con las opciones  ('H', 'Hombre'),('M', 'Mujer'), con longitud máxima 1.
- clave: campo para la contraseña de momento de tipo char, con longitud máxima 45
- limite_edad:  campo de tipo opción con las opciones,    ('Todo Público','Todo Público'),  ('Infantil','Infantil'), con longitud máxima 99.
- uuid = campo que implemente un identificador único y aleatorio conforme a lo especificado por el estándar RFC 4122.
- define la representación en string con nombre  y el límite de edad.

>*__Nota:__ Puedes verificar la implementación de uuid en la siguiente liga: https://docs.python.org/3/library/uuid.html*


__Tabla Pelicula:__
- titulo: longitud máxima 255 y de tipo CharField.
- descripcion:campo de tipo TextField
- creacion: campo de tipo Time. Que agregué la hora actual automáticamente.
- uuid: campo que implemente un identificador único y aleatorio conforme a lo especificado por el estándar RFC 4122.
- tipo: campo de tipo opción con las opciones  ('estreno','Estreno'), ('regular','Regular'), con longitud máxima 99.
- limite_edad: campo de tipo opción con las opciones,    ('Todo Público','Todo Público'),  ('Infantil','Infantil').
- flyer: campo de tipo ImageField, con ruta de carga en 'flyers' que permita nulos y vacíos.
- videos: relación muchos a muchos con la tabla video.

>*__Nota:__ Para implementar el campo de tipo imagen deberemos utilizar el paquete pillow: https://pillow.readthedocs.io/en/stable/*



__Tabla Video:__
- titulo: longitud máxima 255 y de tipo Charfield.
- archivo: campo de tipo FileField con ruta de carga en 'peliculas'.

2. Agrega un usuario administrador a Django. Desde la interfaz de Django agrega un usuario a tu modelo, el usuario deberá llamarse Alberto.

3. Consulta desde tu shell de Django que la información que agregaste se vea reflejada y modifica la representación para que se imprima únicamente el nombre y apellido.

__Expectativa de Resultado__
El usuario que corresponde al modelo desde Django admin
![](postwork1.jpg)
El usuario desde el Shell de Django
![](postwork4.jpg)

<details>
<summary>
Solución</summary>
Para agregar un modelo debes de modificar el archivo __models.py__ y construir los siguientes modelos:

```python
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

PUBLICO =(
    ('Todo Público','Todo Público'),
    ('Infantil','Infantil')
)

TIPO_PELICULA =(
    ('estreno','Estreno'),
    ('regular','Regular')
)

GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
)

class CustomUser(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()
    perfil =models.ManyToManyField('Perfil')

    def __str__(self):
        return "{} {}".format(self.username , self.email)

class Perfil(models.Model):
    nombre=models.CharField(max_length=225)
    apellidos = models.CharField(max_length=80, null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO, default='-')
    clave = models.CharField(max_length=40, null=True, blank=True)
    limite_edad=models.CharField(max_length=30,choices=PUBLICO)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)

    def __str__(self):
        return "{} {}".format(self.nombre , self.limite_edad)

class Pelicula(models.Model):
    titulo:str=models.CharField(max_length=225)
    descripcion:str=models.TextField()
    creacion =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    tipo=models.CharField(max_length=30,choices=TIPO_PELICULA)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    limite_edad=models.CharField(max_length=99,choices=PUBLICO,blank=True,null=True)

class Video(models.Model):
    titulo:str = models.CharField(max_length=225,blank=True,null=True)
    archivo=models.FileField(upload_to='peliculas')


```
Corre las migraciónes necesarias con:

```
python manage.py makemigrations
python manage.py migrate
```

Para agregar el administrador utiliza el siguiente comando:
```
python manage.py createsuperuser
```
Introduce la contraseña de tu preferencia cuando se solicite:

```console
Nombre de usuario (leave blank to use 'betito'):
Dirección de correo electrónico: betito@gmail.com
Password: ******
Password (again): *****
```
Ingresa a localhost/admin y verás los modelos que puedes editar desde el administrador gráfico de Django.

![](postwork2.jpg)

Sin, embargo el modelo no se encuentra disponible aún, para realizar esto es necesario que se realicen modificaciones a  el archivo admin.py registra el modelo que agregarás

```python
from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(CustomUser)
```

Usa la interfaz gráfica para agregar un nuevo registro.
![](postwork3.jpg)

</summary>