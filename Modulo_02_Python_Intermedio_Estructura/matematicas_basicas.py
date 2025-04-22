# Modulo_02_Python_Intermedio_Estructura/matematicas_basicas.py
"""
Módulo simple con funciones matemáticas básicas para usar en ejercicios.
"""

print("Importando el módulo matematicas_basicas...")

PI = 3.14159

def sumar(a, b):
  """Devuelve la suma de a y b."""
  return a + b

def restar(a, b):
  """Devuelve la resta de b a a."""
  return a - b

def multiplicar(a, b):
  """Devuelve la multiplicación de a y b."""
  return a * b

# Código de prueba que solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    print("\nEjecutando matematicas_basicas.py directamente (para pruebas):")
    print(f"Suma 5 + 3 = {sumar(5, 3)}")
    print(f"Resta 10 - 4 = {restar(10, 4)}")
    print(f"Multiplicación 6 * 7 = {multiplicar(6, 7)}")
    print(f"Valor de PI: {PI}")
