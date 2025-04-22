# Ejercicios: Módulo 2 - Introducción a las Pruebas Unitarias

# --- Prerrequisitos ---
# 1. Asegúrate de que el archivo 'utilidades_texto.py' se encuentre en el
#    MISMO directorio que este archivo de ejercicios.
# 2. Si quieres ejecutar las pruebas de pytest, necesitas instalarlo:
#    En tu terminal, con el entorno virtual activado, ejecuta:
#    pip install pytest
#    o
#    conda install pytest

import unittest
import pytest # Necesario para pytest.raises y para ejecutar con pytest

# Importamos las funciones del módulo que queremos probar
from utilidades_texto import a_mayusculas, contar_vocales, invertir_texto

print("--- Ejercicios de Pruebas Unitarias ---")
print("Este script define pruebas, pero la ejecución se hace desde la terminal.")

# --- Ejercicio 1: Pruebas con `unittest` ---
# Instrucciones:
# 1. Define una clase `TestUtilidadesTextoUnittest` que herede de `unittest.TestCase`.
# 2. Dentro de la clase, crea métodos de prueba (que empiecen con `test_`) para
#    cada función en `utilidades_texto.py`.
# 3. Usa los métodos de aserción de `unittest.TestCase` (como `assertEqual`,
#    `assertRaises`) para verificar el comportamiento esperado.
#    - Prueba `a_mayusculas` con un string simple.
#    - Prueba `contar_vocales` con diferentes strings (con/sin vocales, mayúsculas/minúsculas).
#    - Prueba `invertir_texto` con un string.
#    - Prueba que `a_mayusculas` lance un `TypeError` si se le pasa un número
#      (usa `assertRaises` dentro de un `with` statement).
# 4. (Opcional) Añade el bloque `if __name__ == '__main__': unittest.main()` al final
#    para poder ejecutar las pruebas de unittest directamente desde este archivo.
# 5. **Ejecución (desde la terminal):**
#    `python -m unittest 09_ejercicios_pruebas_unitarias.py`
#    o si añadiste el if __name__...: `python 09_ejercicios_pruebas_unitarias.py`

print("\n--- Definiendo Pruebas con unittest ---")

class TestUtilidadesTextoUnittest(unittest.TestCase):

    def test_a_mayusculas_simple(self):
        """Prueba conversión a mayúsculas simple."""
        self.assertEqual(a_mayusculas("hola"), "HOLA")

    def test_a_mayusculas_vacio(self):
        """Prueba conversión a mayúsculas con string vacío."""
        self.assertEqual(a_mayusculas(""), "")

    def test_a_mayusculas_lanza_error_con_numero(self):
        """Prueba que a_mayusculas lanza TypeError con un número."""
        with self.assertRaises(TypeError):
            a_mayusculas(123)
        # Alternativa (menos común):
        # self.assertRaises(TypeError, a_mayusculas, 123)

    def test_contar_vocales_normal(self):
        """Prueba contar vocales en un caso normal."""
        self.assertEqual(contar_vocales("Murcielago"), 5)

    def test_contar_vocales_mayusculas(self):
        """Prueba contar vocales ignorando mayúsculas."""
        self.assertEqual(contar_vocales("AEIOU"), 5)

    def test_contar_vocales_sin_vocales(self):
        """Prueba contar vocales cuando no hay."""
        self.assertEqual(contar_vocales("Rhythm"), 0)

    def test_contar_vocales_vacio(self):
        """Prueba contar vocales en string vacío."""
        self.assertEqual(contar_vocales(""), 0)

    def test_invertir_texto_simple(self):
        """Prueba invertir un texto simple."""
        self.assertEqual(invertir_texto("python"), "nohtyp")

    def test_invertir_texto_palindromo(self):
        """Prueba invertir un palíndromo."""
        self.assertEqual(invertir_texto("reconocer"), "reconocer")

    def test_invertir_texto_vacio(self):
        """Prueba invertir un string vacío."""
        self.assertEqual(invertir_texto(""), "")

# Bloque opcional para ejecución directa con unittest
# if __name__ == '__main__':
#     print("\nEjecutando pruebas de unittest directamente...")
#     unittest.main(argv=['first-arg-is-ignored'], exit=False) # exit=False para que el script continúe


# --- Ejercicio 2: Pruebas con `pytest` ---
# Instrucciones:
# 1. Define funciones de prueba simples (que empiecen con `test_`). No necesitas clases
#    (aunque pytest también las soporta).
# 2. Usa la palabra clave `assert` directamente para verificar los resultados.
# 3. Replica las mismas pruebas que hiciste para `unittest`:
#    - Prueba `a_mayusculas` con un string simple y vacío.
#    - Prueba `contar_vocales` con diferentes casos.
#    - Prueba `invertir_texto` con diferentes casos.
#    - Prueba que `a_mayusculas` lance `TypeError` usando `pytest.raises()`.
# 4. **Ejecución (desde la terminal):**
#    Simplemente ejecuta `pytest` en la terminal, en el directorio que contiene
#    este archivo y `utilidades_texto.py`. Pytest descubrirá y ejecutará
#    automáticamente todas las funciones `test_` y clases `Test...`.

print("\n--- Definiendo Pruebas para pytest ---")

def test_pytest_a_mayusculas_simple():
    """Prueba pytest: conversión a mayúsculas simple."""
    assert a_mayusculas("hola") == "HOLA"

def test_pytest_a_mayusculas_vacio():
    """Prueba pytest: conversión a mayúsculas con string vacío."""
    assert a_mayusculas("") == ""

def test_pytest_a_mayusculas_lanza_error_con_numero():
    """Prueba pytest: a_mayusculas lanza TypeError con un número."""
    with pytest.raises(TypeError):
        a_mayusculas(123)

def test_pytest_contar_vocales_normal():
    """Prueba pytest: contar vocales en un caso normal."""
    assert contar_vocales("Murcielago") == 5

def test_pytest_contar_vocales_mayusculas():
    """Prueba pytest: contar vocales ignorando mayúsculas."""
    assert contar_vocales("AEIOU") == 5

def test_pytest_contar_vocales_sin_vocales():
    """Prueba pytest: contar vocales cuando no hay."""
    assert contar_vocales("Rhythm") == 0

def test_pytest_contar_vocales_vacio():
    """Prueba pytest: contar vocales en string vacío."""
    assert contar_vocales("") == 0

def test_pytest_invertir_texto_simple():
    """Prueba pytest: invertir un texto simple."""
    assert invertir_texto("python") == "nohtyp"

def test_pytest_invertir_texto_palindromo():
    """Prueba pytest: invertir un palíndromo."""
    assert invertir_texto("reconocer") == "reconocer"

def test_pytest_invertir_texto_vacio():
    """Prueba pytest: invertir un string vacío."""
    assert invertir_texto("") == ""


# --- Indicaciones Finales ---
print("\n--- Instrucciones de Ejecución ---")
print("1. Guarda este archivo como '09_ejercicios_pruebas_unitarias.py'.")
print("2. Asegúrate de que 'utilidades_texto.py' está en el mismo directorio.")
print("3. Abre tu terminal en este directorio.")
print("4. Para ejecutar con unittest: python -m unittest 09_ejercicios_pruebas_unitarias.py")
print("5. Para ejecutar con pytest (requiere 'pip install pytest'): pytest")

# --- Fin de los ejercicios ---
