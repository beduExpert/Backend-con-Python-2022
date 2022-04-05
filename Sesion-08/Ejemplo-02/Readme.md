[`Backend con Python`](../../Readme.md) > [`Sesión 08`](../Readme.md) > Ejemplo-02
## Ejemplo 02: Unittest - excepciones

### Objetivos
- Analizar la estructura de exepciones en unittest
- Implementar funciones para identificar valores de error


### Desarrollo

Una excepción es un evento disruptor del flujo normal de un programa. Por lo general, las excepciones ocurren cuando python encuentra una situación que no puede procesar.

En unitest cuando corremos una prueba que no cumple con lo establecido dentro de nuestra función assert. Obtenemos lo siguiente:

```
self.assertEqual(result,10)
AssertionError: 1.0 != 10
```
Python nos indica que el valor que resultó de probar la función generó una excepción. En este caso un AssertionError.

unittest nos proveé con métodos para identificar si es nuestras pruebas están ocurriendo excepciones.
El método `assertRaises()` nos permite identificar si una excepción está ocurriendo durante nuestras pruebas.

Tomemos como ejemplo la función de división divide. Implementos un mensaje para indicar que las divisiones entre 0 no son válidas.


```python
def divide(x,y):
    if y == 0:
        raise ValueError('No es posible dividir entre 0')
    return x/y
```

Modificando nuestro script de pruebas.

```python

    def test_divide(self):
        result = calc.divide(10,5)
        self.assertEqual(result, 2)
        result = calc.divide(-1,-1)
        self.assertEqual(result,10)
        self.assertRaises(ValueError, calc.divide, 10,0)

```

Si corremos nuestro script de prueba obtendremos el siguiente resultado:

```python
F...
======================================================================
FAIL: test_divide (test_calc.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
In line 30, in test_divide       
    self.assertRaises(ValueError,calc.divide,10,1)
AssertionError: ValueError not raised by divide

----------------------------------------------------------------------
Ran 4 tests in 0.001s
```
Indicandonos que se esperaba una excepción y que no se ha encontrado.

asserRaises no es el único método que se nos provee para menjar las excepciones. Podemos implementar excepciones utilizando Context Manager de la siguiente forma: 


```python
    def test_divide(self):
        result = calc.divide(10,5)
        self.assertEqual(result, 2)
        result = calc.divide(-1,-1)
        self.assertEqual(result,1)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
```

Al correr el código anterior todas nuestras pruebas se corren con éxito.

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

Esta forma de implementar excepciones puede resultar más comoda de escribir en algunos cosos. Utiliza la que más te convenga.
