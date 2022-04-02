[`Backend con Python`](../../Readme.md) > [`Sesión 07`](../Readme.md) > Reto-01
## Reto 01: Carga de proyecto en PythonAnywhere
### Objetivos
- Obtener una cuenta en PythonAnywhere
- Generar un nuevo registra para servir una aplicación web
- Inicializar una base de Datos en PythonAnywhere

### Desarrollo
En este reto utilizaremos PythonAnywhere para servir en internet nuestra aplicación en Django. Recuerda haber generado tu cuenta gratuita siguiendo los pasos del prework.

![](img/img1.jpg)

Con tu cuenta de PythonAnywhere realiza las siguientes operaciones:

- Clona un repositorio a tu cuenta de PythonAnywhere.
    - Recuerda que es necesario que tengas tu código listo en alguna aplicación como github y que configures la consola de PythonAnywhere para poder clonar repositorios.
- Genera una base de datos en PythonAnywhere para tu proyecto.
    - Crea una base de datos nueva. Asegurate de guardar la configuración de usuario, nombre y contraseña para que puedas vincular tu aplicación en el futuro.
- Agrega una aplicación web manual a PythonAnyhwere.
    - Agrega una aplicación manual y realiza las configuraciónes necesarias en el archivo WSGI.
    - Utiliza los valores correctos para apuntar a tu ruta ( dentro de PythonAnywhere)
    - Verifica que puedes acceder a tu proyecto desde la URL


<details>
<summary>
Solución
</summary>
Para registrarse en PythonAnywhere sigue los pasos del prework.

Para clonar el repositorio. Inicializa una consola en Python Anywhere desde la siguiente pantalla.
![](img/img2.jpg)

Corre el comando siguiente de git.

```
$git clone https://github.com/myusername/myproject.git
```

Inicializa un ambiente virtual e instala Django.

![](img/img3.jpg)

```
$ mkvirtualenv --python=/usr/bin/python3.8 mysite-virtualenv
(mysite-virtualenv)$ pip install django
# o, si tienes un archivo requierements.txt:
(mysite-virtualenv)$ pip install -r requirements.txt
```

Genera una aplicación manual en PythonAnywhere
![](img/img4.jpg)

Vincula el ambiente virtual que generaste.
![](img/img5.jpg)

Edita el archivo WSGI para utilizar Django.
![](img/img6.jpg)

Configura tu base de datos corriente las migraciones necesarias.
![](img/img7.jpg)

No olvides editar tu archivo settings.py con el usuario y contraseña que generaste en tu base de datos.

</details>