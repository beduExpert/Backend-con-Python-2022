[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Ejemplo 05

## Ejemplo 05: Definiendo y agregando una página con formulario de la aplicación web

## Objetivo
- Crear la ruta y vista para generar el formulario de login
- Crear la ruta y vista para procesar la información de un formulario vía POST


### Desarrollo

Los formularios están presentes en casi cualquier sitio web al menos que sea un sitio web estático que solo publique contenido y no acepte comentarios de los visitantes.

En este ejemplo vamos a conocer como implementar los métodos GET y POST. GET y POST se utilizan típicamente para diferentes propósitos.

Cualquier solicitud que pueda usarse para cambiar el estado del sistema, por ejemplo, una solicitud que realiza cambios en la base de datos, debes usar POST. GET debe usarse sólo para solicitudes que no afecten el estado del sistema.

Para este ejercicio conviene tener a la mano el siguiente.

Diagrama del modelo entidad-relación para el proyecto __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](assets/bedutravels-modelo-er.png)



#### Implementando un formulario
***


Dada la url `http://localhost/login/` se deberá mostrar la siguiente página para hacer __login__ al sistema:

![Bedutravels - Login](assets/login-01.png)

Y posteriormente al proporcionar el usuario __bedutravels__ y clave __bedutravels__ deberá mostrar la página de inicio o un mensaje de error en caso de que no se proporciones los datos de forma correcta.

Creamos la ruta para la url `/login/`

 __Se modifica el archivo `Bedutravels/tours/urls.py` agregando la línea siguiente:__

```python
   path("login/", views.login, name="login"),
```


Creamos la vista `views.login`

   __Se modifica el archivo `Bedutravels/tours/views.py` agregando las función login():__

```python
   def login(request):
       """ Atiende las peticiones de GET /login/ """

       msg = ""

       return render(request, "registration/login.html",
           {
               "msg":msg,
           }
       )
```


#### Creación de una plantilla `login.html`
***

Se crea el archivo `Bedutravels/tours/templates/tours/registration/login.html` copiándolo desde la carpeta `Bedutravels/public_html/` y se modifica de la siguiente forma:

```html
   <section class="profile-container padding-top-lg" style="height: -webkit-fill-available;">
     <div>
       {% if msg %}
       <aside class="text-center">
         {{ msg }}
       </aside>
       {% endif %}
       <div class="margin-bottom-sm">
         <p class="title-font margin-bottom-lg margin-top-lg text-center">Entra al sistema</p>
       </div>
       <div class="profile-info">
         <form class="profile-inputs" method="post">
               {% csrf_token %}
               Usuario: <input type="text" name="usuario" value="" required>
               Clave: <input type="password" name="clave" value="" required>
               <button class="button-tour margin-top-sm" style="align-self: center; width:50%;" type="submit" name="button">
                 Entrar
               </button>
         </form>
       </div>
     </div>
   </section>
  ```
Recordar incluir la etiqueta `csrf_token`, ya que de lo contrario el contenido del formulario no será aceptado por parte de Django.



#### Agregando los archivos estáticos a la página.
***

Es necesario copiar dos archivos de estilos más desde la carpeta `Bedutravels/public_html/css/`, que son `forms.css` y `profile.css` a la carpeta `Bedutravels/tours/static/tours/css/`

```console
   Bedutravels/tours/static/tours $ cp ../../../public_html/css/forms.css css/
   Bedutravels/tours/static/tours $ cp ../../../public_html/css/profile.css css/
   Bedutravels/tours/static/tours $
```
Recargar nuevamente la página (posiblemente sea necesario usar Control+Shift+R) y ahora si la página ya tiene que verse de forma correcta.

#### Procesamiento de los datos en el formulario
***

 Ajustamos la vista `views.login` para que valide los datos del formulario.

__Se procesan los datos POST en la vista:__

```python
   # Se definen los datos de un usuario válido
   usuario_valido = ("bedutravels", "bedutravels")  # (username, password)

   # Si hay datos vía POST se procesan
   if request.method == "POST":
       # Se obtienen los datos del formulario
       usuario_form = (request.POST["username"],
           request.POST["password"])
       if usuario_form == usuario_valido:
           # Tenemos usuario válido, redireccionamos a index
           return redirect("/")
       else:
           # Usuario malo
           msg = "Datos incorrectos, intente de nuevo!"
   else:
       # Si no hay datos POST
       msg = ""
```

 Y así se debería de ver cuando el usuario es incorrecto:

   ![Bedutravels - Login - Error](assets/login-02.png)

