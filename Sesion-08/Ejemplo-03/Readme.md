[`Backend con Python`](../../Readme.md) > [`Sesión 08`](../Readme.md) > Ejemplo-03
## Ejemplo 03: Unittest - pruebas a clases

### Objetivos
- Realizar pruebas a clases utilizando unitest
- Gestionar las instancias de prueba de una clase utilizando script de pruebas

### Desarrollo

En este ejemplo vamos a implementar unittest para realizar pruebas un poco más complejas que las anteriores. Para realizar esto vamos a crear la siguiente clase:


```python
class Empleado:

    cantidad_aumento = 1.05

    def __init__(self, fisrt, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def nombre_completo(self):
        return '{}.{}'.format(self.first, self.last)

    def aplicar_aumento(self):
        self.pay = int(self.pay * self.cantidad_aumento)
```

Vamos a implentar pruebas a esta clase, utilizando la calse de prueba TestCase y el método assert. La primera función que nos interesa probar email, probará la lógica que genera el email del empleado su primer nombre y segundo nombre ( first , last) @email.com

Comenzemos escribiendo la primera prueba. Email Test.

```python 
import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):
    
    def test_email(self):
        print('Email Test')

        self.emp_1 = Empleado('Corey', 'Schafer', 24000)
        self.emp_2 = Empleado('Beto', 'Smith', 60000)

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Beto.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Juan'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Juan.Smith@email.com')
```

Al correr nuestra prueba podemos implementar sentencias print() que nos permitan dan más información sobre el código que se está ejecutando. El resultado de la prueba es el siguiente: 

```python
Email Test
.
----------------------------------------------------------------------
Ran 1 test in 0.001s
```

Supongamos que nos intersa agregar una segunda prueba.Una prueba para aplicar aumento a nuestros empleados. 

```
    def test_aumento(self):
        print('Aumento Test')
        self.emp_1.aplicar_aumento()
        self.emp_2.aplicar_aumento()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
```
Al intentar correr este fragmento de código. Nos toparemos con el problema de que debido al scope nuestra variable no es posible realizar la prueba pues no existen empleados.

Una solución es generar los empleados en cada prueba. Recuerda que el aumento se definió como un 5% sobre el salario base.

```python
    def test_aumento(self):
        print('Aumento Test')
        self.emp_1 = Empleado('Corey', 'Schafer',50000)
        self.emp_2 = Empleado('Beto', 'Smith', 60000)

        self.emp_1.aplicar_aumento()
        self.emp_2.aplicar_aumento()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
```

Al ejecutar la prueba obtenemos el resultado esperado. Las dos pruebas se ejecutan con éxito.

```python
Aumento Test
.Email Test
.
----------------------------------------------------------------------
Ran 2 tests in 0.002s
```

Sin embargo, generar empleados para cada prueba no resulta conveniente. Debido a esto unittest nos ofrece un método para manejar todos los datos de prueba que utilizaremos durante el caso de prueba.

```python
    def setUp(self):
        self.emp_1 = Empleado('Corey', 'Schafer', 50000)
        self.emp_2 = Empleado('Beto', 'Smith', 60000)
```
El métdodo setUp nos permite inicializar todos los aspectos necesarios para realizar nuestras pruebas. Adaptando el código de forma acorde tenemos lo siguiente:

```python
import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Empleado('Corey', 'Schafer', 50000)
        self.emp_2 = Empleado('Beto', 'Smith', 60000)

    def test_email(self):
        print('Email Test')

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Beto.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Juan'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Juan.Smith@email.com')

    def test_aumento(self):
        print('Aumento Test')

        self.emp_1.aplicar_aumento()
        self.emp_2.aplicar_aumento()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
```
Hemos agregado una sentencia print en el método setUp(), está tiene el único fin de ejemplificar como se va a generar un empleado previo al inicio de cada prueba.

Ejecutar el código anterior resulta en el siguiente resultado:

 ```Python
setUp
Aumento Test
.setUp
Email Test
.
----------------------------------------------------------------------
Ran 2 tests in 0.002s
```
Debido a los mensajes print podemos ver como se genera de forma correcta el empleado de prueba. el método setUp no es el único método que provee unittest para gestionar los datos de prueba. También contamos con el método tearDown que destruye los empleados que hemos generado posterior a cada prueba.

```
   def tearDown(self):
        print('tearDown\n')
```
La implementación de este método será parte del reto que deberás resolver :).