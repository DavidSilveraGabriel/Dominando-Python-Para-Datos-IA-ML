# Módulo 2: Introducción a las Pruebas Unitarias (`unittest` / `pytest`)

Escribir código que funcione es solo una parte del desarrollo de software. ¿Cómo te aseguras de que tu código sigue funcionando correctamente a medida que añades nuevas características o modificas las existentes (refactorización)? La respuesta es **escribir pruebas automatizadas**.

Las **Pruebas Unitarias (Unit Tests)** son el tipo más básico de prueba automatizada. Se centran en verificar que las **unidades individuales** de código (generalmente funciones o métodos de una clase) funcionan como se espera de forma aislada.

**¿Por qué escribir Pruebas Unitarias?**

*   **Detectar Errores Temprano:** Atrapan bugs durante el desarrollo, cuando son más fáciles y baratos de corregir.
*   **Confianza en la Refactorización:** Te permiten modificar o reestructurar tu código con la seguridad de que si las pruebas pasan, no has roto la funcionalidad existente.
*   **Documentación Viva:** Las pruebas sirven como ejemplos ejecutables de cómo se supone que debe usarse tu código.
*   **Mejor Diseño:** Pensar en cómo probar una función a menudo te lleva a diseñarla de manera más modular y desacoplada.
*   **Regresión:** Evitan que errores ya corregidos vuelvan a aparecer accidentalmente en el futuro.

## Frameworks de Pruebas en Python

Python tiene varias herramientas para escribir y ejecutar pruebas unitarias. Dos de las más importantes son:

1.  **`unittest`:**
    *   Es el framework de pruebas **incorporado** en la biblioteca estándar de Python.
    *   Está inspirado en los frameworks xUnit (como JUnit para Java).
    *   Utiliza un enfoque basado en clases: escribes clases que heredan de `unittest.TestCase` y defines métodos de prueba dentro de ellas (que suelen empezar con `test_`).
    *   Proporciona métodos de aserción (assertions) como `assertEqual()`, `assertTrue()`, `assertRaises()`, etc., para verificar los resultados.

2.  **`pytest`:**
    *   Es un framework de pruebas de **terceros** (necesita instalarse: `pip install pytest` o `conda install pytest`).
    *   Es **extremadamente popular** en la comunidad Python por su sintaxis más simple y concisa, su potente sistema de fixtures (para configuración de pruebas) y su extensibilidad.
    *   Permite escribir pruebas como funciones simples (que suelen empezar con `test_`) usando la palabra clave `assert` de Python directamente para las verificaciones.
    *   Tiene un excelente sistema de descubrimiento de pruebas.

**Recomendación:** Aunque `unittest` está incorporado, **`pytest` es generalmente preferido** por su facilidad de uso y características avanzadas. Aprenderemos lo básico de ambos.

## Ejemplo Básico con `unittest`

1.  **Crea tu código a probar:** Guarda esto como `calculadora_simple.py`.

    ```python
    # calculadora_simple.py
    def sumar(a, b):
        """Suma dos números."""
        return a + b

    def restar(a, b):
        """Resta b de a."""
        return a - b
    ```

2.  **Crea el archivo de prueba:** Guarda esto como `test_calculadora_unittest.py` en el mismo directorio o en un subdirectorio `tests/`.

    ```python
    # test_calculadora_unittest.py
    import unittest
    from calculadora_simple import sumar, restar # Importa las funciones a probar

    class TestCalculadoraSimple(unittest.TestCase): # Hereda de unittest.TestCase

        # Un método de prueba (debe empezar con 'test_')
        def test_sumar_positivos(self):
            """Prueba la suma de dos números positivos."""
            resultado = sumar(5, 3)
            self.assertEqual(resultado, 8) # Afirma que resultado es igual a 8

        def test_sumar_negativos(self):
            """Prueba la suma de dos números negativos."""
            self.assertEqual(sumar(-5, -3), -8)

        def test_sumar_cero(self):
            """Prueba la suma con cero."""
            self.assertEqual(sumar(10, 0), 10)
            self.assertEqual(sumar(0, 7), 7)

        def test_restar_basico(self):
            """Prueba la resta básica."""
            self.assertEqual(restar(10, 4), 6)

        def test_restar_resultando_negativo(self):
            """Prueba la resta que da un resultado negativo."""
            self.assertEqual(restar(5, 10), -5)

    # Esto permite ejecutar las pruebas directamente desde este archivo
    if __name__ == '__main__':
        unittest.main()
    ```

3.  **Ejecuta las pruebas:** Abre tu terminal en el directorio del proyecto y ejecuta:
    *   `python -m unittest test_calculadora_unittest.py`
    *   O si añadiste el `if __name__ == '__main__': unittest.main()`, puedes ejecutar: `python test_calculadora_unittest.py`

    Verás una salida indicando cuántas pruebas se ejecutaron y si pasaron (`OK`) o fallaron (`FAIL` o `ERROR`).

## Ejemplo Básico con `pytest`

1.  **Usa el mismo `calculadora_simple.py`** de antes.
2.  **Crea el archivo de prueba:** Guarda esto como `test_calculadora_pytest.py`. `pytest` descubre automáticamente archivos que empiezan con `test_` o terminan con `_test.py`, y funciones dentro de ellos que empiezan con `test_`.

    ```python
    # test_calculadora_pytest.py
    from calculadora_simple import sumar, restar # Importa las funciones

    # Simples funciones de prueba (empiezan con 'test_')
    def test_sumar_positivos():
        """Prueba la suma de dos números positivos."""
        resultado = sumar(5, 3)
        assert resultado == 8 # Usa 'assert' directamente

    def test_sumar_negativos():
        """Prueba la suma de dos números negativos."""
        assert sumar(-5, -3) == -8

    def test_sumar_cero():
        """Prueba la suma con cero."""
        assert sumar(10, 0) == 10
        assert sumar(0, 7) == 7

    def test_restar_basico():
        """Prueba la resta básica."""
        assert restar(10, 4) == 6

    def test_restar_resultando_negativo():
        """Prueba la resta que da un resultado negativo."""
        assert restar(5, 10) == -5

    # Pytest también puede probar métodos dentro de clases (si la clase NO hereda de unittest.TestCase)
    class TestRestaAdicional:
         def test_restar_cero(self):
             assert restar(5, 0) == 5
             assert restar(0, 5) == -5
    ```

3.  **Ejecuta las pruebas:** Abre tu terminal en el directorio del proyecto y simplemente ejecuta:
    *   `pytest`

    `pytest` buscará automáticamente todos los archivos y funciones de prueba en el directorio actual y subdirectorios y los ejecutará. La salida es a menudo más informativa y concisa que la de `unittest`.

**Buenas Prácticas Iniciales:**

*   **Nombra tus archivos de prueba** de forma clara (ej. `test_mi_modulo.py`).
*   **Nombra tus funciones/métodos de prueba** empezando con `test_`.
*   **Cada prueba debe ser independiente:** No debe depender del resultado de otra prueba.
*   **Prueba una sola cosa** en cada función/método de prueba.
*   **Usa nombres descriptivos** para tus pruebas para entender qué están verificando.
*   **Escribe pruebas para casos límite y erróneos**, no solo para el "camino feliz". (Ej. ¿qué pasa si `sumar` recibe texto en lugar de números? Podrías probar que lance un `TypeError` usando `assertRaises()` en `unittest` o `pytest.raises()` en `pytest`).

Las pruebas unitarias son una inversión que da sus frutos a largo plazo, especialmente en proyectos complejos o colaborativos. Empezar a escribirlas desde el principio es una excelente práctica de ingeniería de software.
