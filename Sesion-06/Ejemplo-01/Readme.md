[`Backend con Python`](../../Readme.md) > [`Sesión 06`](../Readme.md) > Ejemplo-01
## Ejemplo 01: Configuración Inicial GraphQL

### Objetivo
- Conocer Django Grahene
- Instalar Django Grahene

### Desarollo

GraphQL es parte de una especificación de una tecnología de lenguaje aplicado a APIs. Aunque suele interpretarse un lenguaje como tal, en realidad está divido en una serie de librerias que implementan la especificación de GraphQL.

Un servicio GraphQL se crea definiendo tipos y campos en esos tipos, y luego proporcionando funciones para cada campo en cada tipo. Por ejemplo, un servicio graphQL que regresa información sobre un usuario puede verse así.

```javascript
type Query {
  me: User
}

type User {
  id: ID
  name: String
}
```

A diferencia de REST se obtiene toda la información desde un solo endpoint y esta sigue una estructura cliente servidor.

![](img/Ejemplo01.jpg)


Para este ejemplo correremos GraphQL accediendo a la API de GitHub en la siguiente liga: https://docs.github.com/en/graphql/overview/explorer


![](img/Ejemplo02.jpg)

Accede con tu cuenta de Github y corre la Query de ejemplo. Tu nombre de usuario debería de visualizarse en la aplicación.

En la parte izquierda del explorador podremos escribir nuestras consultas en GraphQL. Escribamos una consulta para conocer nuestro id y nuestra ubicación.

```javascript
query { 
  viewer { 
    login
    id
    location
  }
}
```

![](img/Ejemplo03.jpg)

Las consultas en GraphQL tienen 3 partes importantes, Campos, Argumentos y Resolvers.

- Campo: Un campo simplemente indica que estamos pidiendo al servidor una información particular. A continuación se muestra un ejemplo de GraphQL de un campo en la consulta graphQL.

```javascript
consulta {
    equipo {
        id nombre
    }
}

"datos": {
    "equipo":[ {
        "id": 1, 
        "nombre": "Betis"
    }
    ,
    ...
]
}
}
```

En el ejemplo GraphQL anterior, pedimos al servidor el campo llamado equipo y sus subcampos como id y nombre. El servidor GraphQL devuelve los datos que le pedimos.

- Argumentos: En REST, sólo podemos pasar un único conjunto de argumentos. Para obtener un perfil una llamada REST típica será como la siguiente

```python
GET /api'equipo?id=2 Content-Type: application JSON
 {
    "id": 2, 
    "name": "Rayo Vayecano".
}
```

- Resolver: Los resolutores proporcionan las direcciones para convertir la operación GraphQL en datos. Resuelven la consulta a los datos mediante la definición de funciones de resolución.


Utilizando los conceptos anteriormente dichos construyamos una consulta que nos permita recuperar la cantidad de usuarios que han hecho fork a un repositorio.

```javasvript
{
  repositoryOwner(login: "apollographql") {
    repository(name: "apollo-client"){
      forks{
        totalCount
      }
    }
  }
}
```


El repositorio al que estaremos consultando será este.
![](img/Ejemplo04.jpg)


Utilizando la API de Github, supongamos que queremos obtener la información sobre las personas que han hecho click en Star (stargazers) dentro de un repositorio de github.El código de GraphQL que usaremos será el siguiente.

```javascript
{
  repositoryOwner(login: "apollographql") {
    repository(name: "apollo-client"){
      stargazers(first:10){
        edges{
          node{
            login
            company
          }
        }
      }
    }
  }
}
```

Notarás que además de los campos y parametros que hemos descrito anteriormente se introdujeron los conceptos de edges y node.

Podemos entender los edges como un arreglo de registros que nos provee con la flexibilidad para utilizar nuestros nodos (la data que queremos consultar)

Cada edge posse lo siguiente:
 - Nodo: registros
 - Cursor: un string base64 para realizar la páginación.

 >*__Nota__* Si te interesa conocer más sobre la espeficación de nodos GraphQL visita. https://relay.dev/graphql/connections.html
 