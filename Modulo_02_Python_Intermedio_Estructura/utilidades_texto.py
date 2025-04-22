# Modulo_02_Python_Intermedio_Estructura/utilidades_texto.py
"""
Módulo simple con funciones de utilidad de texto para probar.
"""

def a_mayusculas(texto):
  """Convierte un texto a mayúsculas."""
  if not isinstance(texto, str):
    raise TypeError("El argumento debe ser una cadena de texto.")
  return texto.upper()

def contar_vocales(texto):
  """Cuenta el número de vocales (a, e, i, o, u) en un texto (insensible a mayúsculas)."""
  if not isinstance(texto, str):
    raise TypeError("El argumento debe ser una cadena de texto.")
  vocales = "aeiou"
  contador = 0
  for letra in texto.lower():
    if letra in vocales:
      contador += 1
  return contador

def invertir_texto(texto):
  """Invierte una cadena de texto."""
  if not isinstance(texto, str):
    raise TypeError("El argumento debe ser una cadena de texto.")
  return texto[::-1]

if __name__ == "__main__":
    print("Ejecutando utilidades_texto.py directamente (para pruebas manuales):")
    print(f"'Hola' a mayúsculas: {a_mayusculas('Hola')}")
    print(f"Vocales en 'Murcielago': {contar_vocales('Murcielago')}")
    print(f"Invertir 'Python': {invertir_texto('Python')}")
    try:
        a_mayusculas(123)
    except TypeError as e:
        print(f"Error esperado al pasar número a a_mayusculas: {e}")
