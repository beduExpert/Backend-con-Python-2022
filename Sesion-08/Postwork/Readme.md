[`Backend con Python`](../../Readme.md) > [`Sesión 08`](../Readme.md) > Postwork
## Postwork 08 - Testing

### Objetivos
- Preparar los archivos de Test Unitarios.
- Realizar pruebas a los modelos de película de beduflix y a todos los formularios de beduflix.
- Mostrar el comportamiento de las vistas y de la inyección de XSS en el sitio.


### Desarrollo

Asegúrate de Comprender:

- Cómo utilizar la clase de Pruebas y realizar pruebas dentro de clases.
- La implementación de pruebas en formularios y en modelos.
- La protección XSS.


### Indicaciones Generales

Es el momento de que pruebes tu proyecto. Para realizar esto deberás seguir las siguientes instrucciones:

Es el momento de que pruebes tu proyecto. Para realizar esto deberás seguir las siguientes instrucciones:
    - Selecciona una clase de pruebas.
        - Se aconseja utilizar unitest, pero puedes utilizar otra clase si lo deseas.
    - Implementa las pruebas para una vista.
        - Recuerda que se deben realizar las clases adecuadas y validar los códigos de retorno.
    - Implementa las pruebas para un modelo.
        - Deberás de crear el set up de datos para tu clase y validar los casos válidos para el modelo.

- Implementa protección contra XSS
    -  Utiliza la instrucción  dentro de un input de formulario <script>alert('Test alert');</script>. y asegurate de que no se ejecuta el código.


### Resultado Esperado
Pruebas para vistas
![](vista.jpg)

Pruebas para modelos
![](modelo.jpg)

Proteccion XSS
![](xss.png)