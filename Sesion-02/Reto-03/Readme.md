`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Reto-03

# Reto 03: Operaciones CRUD

### Objetivo
- Utilizar un esquema en la base de datos SQLite
- Programar las operaciones CRUD
- Comprobar la creación de la información usando DB Browser.

### Desarrollo
Utilizando DB Browser vamos a implementar una nueva base de datos llamada librería. Esto nos servirá para repasar las instrucciones SQL que nos permiten definir un esquema de datos.

1. En una base de datos llamada librería cra una tabla llamada libro. Deberá incluir los siguientes campos:
   - id
   - titulo
   - editorial
   - numPag
   - numAutores
Utiliza los tipos de datos que mejor convengan. Asegurate de que id sea un campo llave primaria y no nulo.

2. Inserta en la base de datos los siguientes libros:
 - Titulo: Yo, Robot' Editorial: Gnome Press
 paginas: 374 autores: 1
 - Titulo: El fin de la eternida Editorial: Gnome Press
 paginas: 374 autores: 1
 - Titulo: El arte de la guerra Editorial: Gnome Press
 paginas: 374 autores: 1

3. Elimina el libro con el id 1
   - No olvides mostrar tus resultados usando una clausula select.

> *__Nota:__ No olvides instalado mysqlclient para poder realizar tus migraciones desde Django.*

```console
pip install mysqlclient
```

<details><summary>Solución</summary>

Para generar la Tabla libro

```SQL
   
   CREATE TABLE "Libro" (
      "id"	INTEGER NOT NULL,
      "titulo"	TEXT,
      "editorial"	INTEGER,
      "numPag"	TEXT,
      "numAutores"	TEXT,
      PRIMARY KEY("id" AUTOINCREMENT)
   );
```
Para ingresar los libros

```SQL

   INSERT INTO `Libro` VALUES (1,'Yo, Robot','Gnome Press',374,1),(2,'El fin de la eternidad','Gnome Press',191,1),(3,'El arte de la guerra','Obelisco',112,2);

 ```
Para eliminar el libro con ID 1

```SQL
   DELETE FROM Libro WHERE id=1
```
Para visualizar los cambios 
```SQL
   SELECT * FROM Libro
```

</details>

Si has llegado hasta este punto __FELICIDADES__, toma __otro__ respiro o ayuda a algún compañero que no lo haya logrado aún o tomate un café te lo mereces.
