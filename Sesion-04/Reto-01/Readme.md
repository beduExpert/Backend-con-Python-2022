[`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Reto-01
## Definiendo y agregando autenticación de salida usando el modelo User de Django

### OBJETIVO
- Crear autenticación de salida para una página de la aplicación


### DESARROLLO
En este ejemplo continuaremos con las definiciones de nuestro sistema de autenticación. Por lo cual vamos a agregar una vista que nos permita hacer logout. Realiza estas modificación en tu proyecto _Bedutravels_ provisto en los ejemplos de clase.

Para lograr esto debemos hacer lo siguiente:

- Agrega la ruta para la url `/logout/`. Implementa la variable request que se demostró en los ejemplos.



- Agrega la vista `views.logout_user` para la ruta `logout/`

<details>
<summary>Solución</summary>


   __Se modifica el archivo `Bedutravels/tours/views.py` con lo siguiente:__
   ```python
   def logout_user(request):
       """ Atiende las peticiones de GET /logout/ """
       # Se cierra la sesión del usuario actual
       logout(request)

       return redirect("/login/")
   ```

Para agregar la url:

      __Se modifica el archivo `Bedutravels/tours/urls.py` con lo siguiente:__
   ```python
   path("logout/", views.logout_user, name="logout_user"),
   ```

   __Se tiene que importar la función `logout()` de la siguiente forma:__
   ```python
   from django.contrib.auth import authenticate, login, logout
   ```

   Validar que mediante el menú se pueda entrar y salir del sistema.

Eso es todo, ya cuentas con un sistema con entrada y salida de usuarios.
</details>