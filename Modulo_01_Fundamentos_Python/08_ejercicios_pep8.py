# Ejercicios: Módulo 1 - Buenas Prácticas Iniciales y PEP 8

# Instrucciones: Revisa el siguiente código. Contiene varias violaciones de las
# convenciones de estilo PEP 8. Identifica las violaciones y reescribe el código
# debajo de cada sección para que cumpla con PEP 8.

# --- Sección 1: Sangría y Espacios ---

print("--- Sección 1: Sangría y Espacios (Original) ---")
def miFuncion( parametro1, parametro2 ):
    resultado=parametro1+parametro2
    if resultado>10 :
     print( 'El resultado es mayor que 10' )
    else:
      print('El resultado es 10 o menor')
    return resultado

variable_a= 5
variable_b =10
suma = miFuncion( variable_a,variable_b)
mi_lista =[1,2, 3,4]
print(suma,mi_lista [0] )

print("\n--- Sección 1: Sangría y Espacios (Corregido) ---")
# Escribe tu código corregido aquí
def mi_funcion(parametro1, parametro2):
    """Suma dos parámetros y compara el resultado con 10."""
    resultado = parametro1 + parametro2
    if resultado > 10:
        print('El resultado es mayor que 10')
    else:
        print('El resultado es 10 o menor')
    return resultado

variable_a = 5
variable_b = 10
suma = mi_funcion(variable_a, variable_b)
mi_lista = [1, 2, 3, 4]
print(suma, mi_lista[0])


# --- Sección 2: Nombres y Longitud de Línea ---

print("\n--- Sección 2: Nombres y Longitud de Línea (Original) ---")
# Constante global (mal nombrada)
FACTORCONVERSION = 1.60934

def KilometrosAMillas(kilometros):
    # Variable local (mal nombrada)
    ResultadoEnMillas = kilometros / FACTORCONVERSION
    print(f"{kilometros} kilómetros equivalen a {ResultadoEnMillas} millas. Este es un mensaje bastante largo para demostrar cómo una línea puede exceder fácilmente el límite recomendado de caracteres si no tenemos cuidado al escribir código o comentarios extensos.")
    return ResultadoEnMillas

distanciaKm = 100
distancia_millas = KilometrosAMillas(distanciaKm)

print("\n--- Sección 2: Nombres y Longitud de Línea (Corregido) ---")
# Escribe tu código corregido aquí
# Constante global (nombre corregido)
FACTOR_CONVERSION_KM_MILLAS = 1.60934

def kilometros_a_millas(kilometros):
    """Convierte una distancia de kilómetros a millas."""
    # Variable local (nombre corregido)
    resultado_en_millas = kilometros / FACTOR_CONVERSION_KM_MILLAS
    # Línea larga dividida para cumplir PEP 8
    print(f"{kilometros} kilómetros equivalen a {resultado_en_millas:.2f} millas. "
          "Este es un mensaje dividido para cumplir el límite.")
    return resultado_en_millas

distancia_km = 100
distancia_millas = kilometros_a_millas(distancia_km)


# --- Sección 3: Importaciones y Líneas en Blanco ---

print("\n--- Sección 3: Importaciones y Líneas en Blanco (Original) ---")
import sys, os # Mal: dos importaciones en una línea
def funcion_a():
    print("Función A")
    # Sin línea en blanco antes
def funcion_b():
    print("Función B")
variable_global = 100 # Sin líneas en blanco suficientes después de imports
class MiClase:
    def metodo_uno(self):
        print("Método 1")
    # Sin línea en blanco entre métodos
    def metodo_dos(self):
        print("Método 2")

print("\n--- Sección 3: Importaciones y Líneas en Blanco (Corregido) ---")
# Escribe tu código corregido aquí
import sys # Bien: una importación por línea
import os

# Dos líneas en blanco antes de la definición de función/clase de nivel superior
variable_global = 100


def funcion_a():
    """Imprime un mensaje para la función A."""
    print("Función A")


# Dos líneas en blanco antes de la siguiente definición
def funcion_b():
    """Imprime un mensaje para la función B."""
    print("Función B")


# Dos líneas en blanco antes de la definición de clase
class MiClase:
    """Una clase de ejemplo con dos métodos."""
    def metodo_uno(self):
        """Imprime un mensaje para el método uno."""
        print("Método 1")

    # Una línea en blanco entre métodos de la clase
    def metodo_dos(self):
        """Imprime un mensaje para el método dos."""
        print("Método 2")


# --- Fin de los ejercicios ---
# ¡Revisa la guía PEP 8 para más detalles!
# Puedes usar herramientas como linters (Flake8, Pylint) en tu editor
# para que te ayuden a identificar estos problemas automáticamente.
