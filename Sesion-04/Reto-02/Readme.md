[`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Reto-02
## Reto 02:  Definiendo y agregando autenticación de salida usando la vista auth_views.login de Django.

### OBJETIVO
- Crear autenticación de salida usando la vista auth_views.logout de Django.


### DESARROLLO
En este ejemplo continuaremos con las definiciones de nuestro sistema de autenticación. Por lo cual vamos a agregar una vista que nos permita hacer logout esta ves utilizaremos auth_views que ya viene incluido con Django. Realiza estas modificación en tu proyecto _Bedutravels_ provisto en los ejemplos de clase.

Para lograr esto debemos hacer lo siguiente:

- Modifica la ruta `/logout` para hacer uso de la vista auth_views. No olvides que debes de incluir en el código los módulos de autenticación en los import.


<details>
<summary>Solución</summary>
   recuerda importar en tu archivos views.py lo siguiente:

   ```python.
   from django.contrib.auth import authenticate, login, logout
   ```

   En el archivo urls.py __Se modifica la ruta:__
   ```python
   path("logout/", auth_views.logoutView.as_view(next_page="/login/"), name="logout"),
   ```
   De igual forma no se requiere la la vista `logout_user()` .

   __Borra la vista `logout_user() del archivos views.py`__

    Verifica que el proceso de login y logout sigue funcionando
</details>