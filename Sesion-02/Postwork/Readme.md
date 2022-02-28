`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Postwork
## Postowrk 02: Creación de una aplicación sencilla en Django

### OBJETIVOS
- Inicializar una base de datos SQL para el proyecto To-DO APP.
- Configurar la conexión a la base de datos.
- Validar la conexión realizando una migración inicial

### DESARROLLO
La finalidad de la siguiente actividad es aplicar los conceptos vistos en esta sesión a tu proyecto ToDo App, por lo que es necesario seguir las siguientes instrucciones.

Recuerda que en tu postwork pasado ya inicializaste un ambiente virtual y cargaste una primer pantalla. En este ejercicios nos vamos a centrar en el backend de la aplicación. Configurando la base de datos y la conexión hacia esta desde Django.

#### Asegúrate de comprender:
- Cómo instalar una base de datos en tu equipo.
- Entender la estructura del archivo settings.py
- Conocer los engines y librerías asociadas a las conexiones de Django.
- Qué se necesita configurar una conexión bases de datos en Django.

<details><summary>
1. Inicializar un servidor PostgreSQL, MySQL o SQLite y la base de datos de tu elección Puedes utilizar contenedores, un servidor o SQLite.
</summary>
Instala la base de datos de tu preferencia. Es importante que verifiques que el usuario exista y tenga los permisos adecuados. Además debe de estar expuesta y accesible mediante el host y los puertos que Django espera recibir en el string de conexión.
</details>


<details><summary>
2. Realiza una conexión desde Django a tu base de datos.

</summary>
Para lograr esto debes de instalar el modulo de conexión a base de datos que corresponda al engine que decidiste usar. Estos se instalan con `pip` dentro del entorno virtual donde ejecutas la app.

Posteriormente modifica el archivo settings.py para copiar los parámetros de conexión de la base que configuraste anteriormente.
</details>


<details><summary>
3. Validar la conexión corriendo una primera migración.

</summary>
Una vez configurada la conexión puedes verificarla haciendo la migración inicial. Recuerda que las opciones a tu disposición están asociadas a `python manage.py`
</details>

``
<details>
<summary>
Solución</summary>
TBD
</details>