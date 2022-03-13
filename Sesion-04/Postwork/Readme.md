[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Postwork
## Postwork 04: Implementación de pantallas login

### Objetivo
- Implementar elementos reutilizables.
- Implementar una pantalla de login usando autenticación.
- Agregar vistas para representar modelos de película.

### Desarrollo

Para este Postwork continuaremos con la creación de nuestra aplicación BEDUFLIX es importante que tengas los archivos que generaste durante cada sesión y la conexión válida que tienes en el desarrollo de este Postwork.

Con el modelo que generemos en sesiones pasadas __User__  vamos a implementar una pantalla de login y vincularemos esta a una sección de index, en la cual los elementos comunes, como la barra de navegación se implementaran como elementos reutilizables.

#### Asegúrate de comprender:
- Cómo funcionan los modelos en Django.
- Verificar la existencia de usuarios en tu modelo User
- La estructura de archivos que sigue un formulario
- El modelo de autenticación de Django.
- Cómo agregar vistas y plantillas y recuperar información de la BD en estas.


Indicaciones generales
<details><summary>
1. Verifica que existan usuario en tu modelo __CustomUser__, y que recuerdes la contraseña.
</details>
- Puedes hacer uso de Django Admin para verificar la información de los usuarios de tu modelo, modificar su contraseña o agregar información.
</summary>

<details><summary>
2. Implementa un formulario en la pantalla de login que generamos en la sesión 1.
</summary>
- Utiliza los métodos POST para recuperar la información de nombre de usuario.
- Utiliza las etiquetas de plantilla adecuadas para activar el manejo de variables.

 A continuación tienes un ejemplo de código para implementación de login:

```python

def login_user(request):
    # Si hay datos vía POST se procesan
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        # Se obtienen los datos del formulario
        username=request.POST["username"],
        password=request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
    if user is not None:
            login(request, user)

    else:
        # Si no hay datos POST
        msg = ""

    return render(request, "login.html",{"msg":msg,})


```
</details>

<details><summary>
3. Implementa una vista como página de inicio para los usuarios autenticados. Recupera la información de los perfiles asociados al modelo y habilita el formulario  Utiliza una barra de navegación y pie de página reutilizables.
</summary>

- Utiliza la herencia de plantillas para lograr esto.
- Puedes usar bootstrap u otra librería para para generar tus elementos de navegación y pie de página.

No olvides agregar los decoradores de login para estas plantillas de otra forma serán accesibles mediante el path directo en el navegador.

```python
@login_required()
def index(request):
    return render(request, "app/index.html")
```

Modificaciones necesarias en urls.py.
```python
urlpatterns = [
    path('', views.login_user, name="login"),
    path('index', views.index, name="index")
]
```

A continuación un ejemplo de código para que puedas guiarte un poco:

Implementación de la plantilla base

```html
{% load static %}
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <title>To do App</title>
  </head>
  <body class="d-flex flex-column h-100" data-new-gr-c-s-check-loaded="8.896.0" data-gr-ext-installed="" cz-shortcut-listen="true">

    <div state="voice" class="placeholder-icon" id="tts-placeholder-icon" title="Click to show TTS button" style="background-image: url(&quot;moz-extension://b37e2285-378e-45f4-84e0-f5b3f5e289ad/data/content_script/icons/voice.png&quot;);"><canvas class="loading-circle" id="text-to-speech-loader" style="display: none;" width="36" height="36"></canvas></div></body>
        <nav class="navbar navbar-expand-sm navbar-dark bg-dark sticky-top">
          <div class="container-fluid">
            <div class="navbar-header">
              <a class="navbar-brand" href="#">Mi Sitio</a>
            </div>
          </div>
        </nav>
        {% block content %}
        <!-- el contenido irá en este bloque-->
        {% endblock %}
        <footer class="footer mt-auto py-3 bg-light">
          <div class="container">
            <span class="text-muted">Este es un pie de página</span>
          </div>
        </footer>
  </body>
</html>


```
Modificaciones a la plantilla index. Utilizamos __extends__ para heredar de la plantilla que generamos.

```html
 {% extends 'base.html' %}
        {% block content %}
        <main class="flex-shrink-0">
          <div class="container">

            <div class="row"><h1 class="mt-5"></h1>¡Bienvenido! Tu nombre de usuario es: {{ user.username }}</h1></div>
            <div class="row"><a href="/logout/"><button type="button" class="btn btn-primary">Salir</button></a></div>
          </div>
        </main>
        {% endblock %}
```
</details>

<details><summary>
4. Recupera la información de tu usuario e imprime el listado de perfiles asociados.
</summary>


- Esto lo puedes lograr haciendo uso de etiquetas de variables. No olvides que debes de tener los elementos populados en tu base de datos.

A continuación un ejemplo del uso de etiquetas para recuperar información:
```html

        {% for profile in profiles %}
            <a href="{% url 'core:watch' profile_id=profile.uuid %}">
                <div class="w-32 h-32 m-4  bg-blue-500 flex justify-center items-center flex-col rounded-md cursor-pointer">
                    <p class='text-6xl'>
                        {{profile.name | slice:":1"}}
                    </p>
                    <p class='text-lg'>
                        {{profile.name}}
                    </p>
                </div>
            </a>
        {% endfor %}
```

</details>

<details><summary>
5. Agrega un botón que permita hacer el cierre de la sesión.
</summary>

- Recuerda agregar la vista que corresponde a logout.
- Utiliza  redirect() para regresar al login.
</details>


<details><summary>
6. Agrega una nuevs plantilla en la que puedas visualizar la información de las películas de la app.
</summary>

- Recuerda que todos los modelos están definidos en el postwork 3.
- Utiliza django admin para cargar la información necesaria y recupera en tu plantilla.
>*__Nota:__ No es necesario implementar el reproductor. Pero en caso de intentarlo puedes utilizar archivos .webm*
</details>


#### Resultado esperado:

__Pantalla de inicio de sesión funcionando:__
![](postwork1.jpg)

<p>
&nbsp;
</p>

__Pantalla post login, con los perfiles recuperados y formulario para agregar perfil__

![](postwork5.jpg)


<p>
&nbsp;
</p>

__Pantalla para mostrar un item de película__

![](postwork4.jpg)

>*__Nota:__ Recuerda que los elementos comunes como la barra de navegación o el pie de página deberán incluirse como una plantilla base*