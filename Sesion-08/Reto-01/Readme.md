[`Backend con Python`](../../Readme.md) > [`Sesión 08`](../Readme.md) > Reto-01
## Reto 01: Pruebas unitarias usando unittest

### Objetivos
- Utilizar unittest para hacer pruebas unitarias.
- Emplear las clases TestCase para crear un caso de pruebas
- Emplear métodos de prueba para probar una aplicación en python.

### Desarrollo

En el ejemplo 1 demostramos como utilizar el paquete unittest para probar la función suma y resta de nuestra aplicación calculadora (calc.py). Utilizando el código de la aplicación calculadora y unittest escribe pruebas para las funciones restantes.

Código de calc.py

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

Para escribir tus casos de prueba considera lo siguiente. Recuerda generar un nuevo archivo .py con el  prefijo test_ de lo contrario unittest no podrá encontrarlo.

- Escribe pruebas para el método multiplica
    - utiliza el método assertEqual.
    - considera los casos calc.multiplica(10,5), calc.multiplica(-1,-1)
    - De momento no es necesario incluir otros casos de prueba
- Escribe pruebas para el método divide
    - utiliza el método assertEqual.
    - considera los casos calc.divide(10,5), calc.divide(-1,-1)
    - De momento no es necesario incluir otros casos de prueba

<details>
<summary>
Solución
</summary>
El código de test_calc.py que corresponde a las pruebas para los métodos multiplica y divide. 

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


    def test_multiplica(self):
        result = calc.multiplica(10,5)
        self.assertEqual(result, 50)
        result = calc.multiplica(-1,-1)
        self.assertEqual(result,1)

    def test_divide(self):
        result = calc.divide(10,5)
        self.assertEqual(result, 2)
        result = calc.divide(-1,-1)
        self.assertEqual(result,1)

```
El resultado de ejecutar las pruebas es el siguiente:

```console
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
</details>