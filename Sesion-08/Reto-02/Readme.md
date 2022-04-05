[`Backend con Python`](../../Readme.md) > [`Sesión 08`](../Readme.md) > Reto-02
## Reto 02: Pruebas a clases usando unittest

### Objetivos
- Utilizar unittest para hacer pruebas a clases
- Emplear las clases TestCase para crear un caso de pruebas
- Emplear los métodos setUp y TearDown para preparar los datos de prueba.

### Desarrollo
Hemos aprendido a implementar pruebas unitarias a funciones y clases. Utilizando la clase empleado implementa el resto de las pruebas para probar `empleado.nombre_completo()`. Utiliza el método `SetUp` para crear empleados de prueba y agrega una sentencia `print()` al método `tearDown` para visualizar el proceso de creación y destrucción de los datos de prueba.


```python
class Empleado:

    cantidad_aumento = 1.05

    def __init__(self, first, last, pay):
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

El resultado esperado para la impresión del nombre completo de un empleado es 'first last' ejemplo:  'Beto Smith'. Escribe tus pruebas considerando esto y realiza las modificaciones necesarias a la clase Empleado en caso de encontrar algún error.




<details>
<summary>
Solución
</summary>
El código de test_empleado.py que corresponde a las pruebas para el resto de los métodos.

```python
import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Empleado('Corey', 'Schafer', 50000)
        self.emp_2 = Empleado('Beto', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

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

    def test_nombre_completo(self):
        print('Nombre Test')
        self.assertEqual(self.emp_1.nombre_completo, 'Corey Schafer')
        self.assertEqual(self.emp_2.nombre_completo, 'Beto Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.nombre_completo, 'John Schafer')
        self.assertEqual(self.emp_2.nombre_completo, 'Jane Smith')


```
El resultado de ejecutar las pruebas es el siguiente:

Una primera prueba con un error en la prueba Nombre.

```python
setUp
Aumento Test
tearDown    

.setUp      
Email Test  
tearDown    

.setUp      
Nombre Test 
tearDown    

F
======================================================================
FAIL: test_nombre_completo (test_empleado.TestEmpleado)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\hesgarci\Documents\Python\Sesion 8 - Testing\test_empleado.py", line 37, in test_nombre_completo
    self.assertEqual(self.emp_1.nombre_completo, 'Corey Schafer')
AssertionError: 'Corey.Schafer' != 'Corey Schafer'
- Corey.Schafer
?      ^
+ Corey Schafer
?      ^


----------------------------------------------------------------------
Ran 3 tests in 0.004s

FAILED (failures=1)

```

Realizando las correciones a empleado.nombre_completo




```python
@property
    def nombre_completo(self):
        return '{} {}'.format(self.first, self.last)
```

```python
setUp
Aumento Test
tearDown    

.setUp      
Email Test  
tearDown

.setUp
Nombre Test
tearDown

.
----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK

```


</details>