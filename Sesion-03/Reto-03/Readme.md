[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Reto-03
# Reto 03: Definiendo las consultas usando el ORM de Django

### OBJETIVO
- Crear consultas entre tablas y sus relaciones
- Programar una consulta para generar un reporte.

Para este reto es necesario implementar los tablas descritas en el siguiente modelo entidad relación.

![Modelo entidad-relación para Bedutravels](assets/bedutravels-modelo-er.png)



### DESARROLLO
Para este realizaremos una consulta desde la consola de Django. Imprime la lista de todas las Zonas, en cada Zona incluir

-id
- nombre
- lista de tours que salen de esa zona.

En cada Tour incluir
- id
- nombre
- lista de salidas para ese tour.

Para cada Salida incluir
- id
- fechaInicio
- fechaFin.

Recuerda utilizar los métodos adecuados para realizar la consulta. Así como importar desde tours.models los objetos correspondientes.

>*__Nota__: Recuerda que los resultados de una consulta en Django se almacenan como un QuerySet. Este es un objeto iterable que puedes filtrar y enlistar.*


<details>
<summary>
Solución
</summary>


Importar los modelos.
   __Dentro el Shell de Django:__

   ```python
   >>> from tours.models import Zona, Tour, Salida
   ```
Para asignar asignar los objetos a una variable utilizar el método .all() pues no queremos filtrar ningún registro.
   ```
   >>> zonas = Zona.objects.all()
   >>> zonas
   <QuerySet [<Zona: Ciudad de México>, <Zona: Yucatán>, <Zona: Chiapas>, <Zona: Guanajuato>]>
   ```

Debido a que el objeto zonas es un conjunto iterable podemos utilizar un for con list comprehension y  dar formato a los tours y salidas.
   ```
   >>> for zona in zonas:
   ...     print(zona.id, zona)
   ...     for tour in zona.tours_salida.all():
   ...         print("   ", tour.id, tour)
   ...         for salida in tour.salidas.all():
   ...             print("   "*2, salida.id, salida.fechaInicio, salida.fechaFin)


   ```
   Resultado
   ```
   1 Ciudad de México
       1 Chiapas Hermoso
          1 2019-06-21 2019-06-26
          2 2019-07-03 2019-07-08
          3 2019-07-09 2019-07-14
       2 Guanajuato por siempre
          4 2019-07-21 2019-07-26
          5 2019-08-03 2019-08-03
          6 2019-08-03 2019-08-03
          7 2019-08-09 2019-08-14
       3 Yucatán y naturaleza
          8 2019-08-22 2019-08-26
          9 2019-08-22 2019-08-27
          10 2019-09-13 2019-09-19
   2 Yucatán
   3 Chiapas
   4 Guanajuato
  
   ```
</details>
