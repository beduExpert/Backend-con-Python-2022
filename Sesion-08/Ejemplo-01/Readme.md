[`Backend con Python`](../../Readme.md) > [`Sesión 08`](../Readme.md) > Ejemplo-01
## Ejemplo 01: Unittest

### Objetivos
- Analizar la estructura unitest
- Implementar un caso de pruebas
- Unterpretar los mensajes de consola resultantes de la ejecución de pruebas.

### Desarrollo

Las pruebas unitarias son un tiop de pruebas en las que verificamos la funcionalidad minimina de una parte de neustro software. Las pruebas nos permiten asegruarnos de que nuestro software funciona como debería y dotan de más confianza a nuestro erquipo de trabajo para colaborar en un futuro con nosotros.

unittest es el paquete que se integra por defecto en Python. Para integrarlo en un proyecto solo basta importarlo de la siguiente forma.

```
import unittest
```
unittest es una funcionalidad independiente de Django y podemos utilizar el paquete de forma independiente. Para demostrar su funcionalidad escribiremos un script de pruebas para una programa en python llamado calc.py

```python
def suma(x,y):
    return x + y

def resta(x,y):
    return x-y

def multiplica(x,y):
    return x*y

def divide(x,y):
    return x/y

```
Este es el contenido de nuestro programa calculadora. Consiste en las funciones suma, resta,multiplica y divide. Para inicializar un caso de pruebas generaremos un nuevo archivo de nombre `test_calc.py`. Esta nomenclatura test_ permite a modulos como unittest o pytest descubrir automáticamente casos de prueba.

```python
import unittest
import calc

class TestCalc(unittest.TestCase):
	
```

El contenido de nuestro caso de pruebas incluye una clase llamada TestCalc que hereda de la clase TestCase. Dentro de esta clase escribiremos las diversas pruebas a nuestro programa calculadora.

Escribamos un primer caso para verificar la función suma.

```python 
import unittest
import calc

class TestCalc(unittest.TestCase):
	def test_suma(self):
		result = calc.suma(10,5)
		self.assertEqual(result, 15)
```
Para correr nuestras pruebas llamamos a unittest como nuestro modulo principal y pasamos nuestro test case con el siguiente comando:

```
python -m unittest test_calc.py
```

El resultado de este comando será el siguiente:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```
unittest nos indica el número de pruebas y el tiempo que le toma realizar las evaluciones.



Recuerda que las pruebas deben de nombrarse con test_ al inicio. modificquemos el nombre de nuestra prueba a tsuma y corramos la prueba nuevamente para mostrar esta funcionalidad.

al correr el comando 

```
python -m unittest test_calc.py
```
En el resultado de la consola podemos observar como no se han ejecutado pruebas.

```

----------------------------------------------------------------------
Ran 0 tests in 0.000s
```
Por esta razón debemos tener cuidado al nombrar nuestras funciones de prueba. Renombremos nuestro método a test_suma y agreguemos más casos de prueba. En esta ocasión probaremos la suma de números negativos.

```python
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_suma(self):
        result = calc.suma(10,5)
        self.assertEqual(result, 15)
        result = calc.suma(-1,-1)
        self.assertEqual(result,-2)

```
Notarás que si ejecutas esta prueba nos indica que se corrió 1 prueba con estado Ok

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```
Esto es debido que aunque agregamos varios casos solo estamos probando la función prueba. Agreguemos una prueba para la resta.

```python
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_suma(self):
        result = calc.suma(10,5)
        self.assertEqual(result, 15)
        result = calc.suma(-1,-1)
        self.assertEqual(result,-2)

    def test_resta(self):
        result = calc.resta(10,5)
        self.assertEqual(result, 5)
        result = calc.resta(-1,-1)
        self.assertEqual(result,0)

```
El resultado de nuestro prueba indica que se han ejecutado dos pruebas de forma exitosa.

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```





