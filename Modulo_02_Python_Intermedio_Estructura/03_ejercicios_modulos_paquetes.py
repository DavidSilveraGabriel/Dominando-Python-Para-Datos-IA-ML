# Ejercicios: Módulo 2 - Módulos y Paquetes

# --- Prerrequisito ---
# Asegúrate de que el archivo 'matematicas_basicas.py' (creado en el paso anterior)
# se encuentre en el MISMO directorio que este archivo de ejercicios.

# --- Ejercicio 1: Importación Completa de Módulo ---
# Instrucciones:
# 1. Importa el módulo completo `matematicas_basicas`.
# 2. Llama a la función `sumar` del módulo para sumar 15 y 7. Imprime el resultado.
# 3. Llama a la función `multiplicar` del módulo para multiplicar 6 por 8. Imprime el resultado.
# 4. Accede a la constante `PI` del módulo e imprímela.

print("--- Ejercicio 1: Importación Completa ---")
# Escribe tu código aquí
import matematicas_basicas

resultado_suma = matematicas_basicas.sumar(15, 7)
print(f"Suma (15+7) usando módulo completo: {resultado_suma}")

resultado_multi = matematicas_basicas.multiplicar(6, 8)
print(f"Multiplicación (6*8) usando módulo completo: {resultado_multi}")

print(f"Valor de PI desde el módulo: {matematicas_basicas.PI}")


# --- Ejercicio 2: Importación Selectiva (`from ... import`) ---
# Instrucciones:
# 1. Importa específicamente la función `restar` y la constante `PI` del módulo `matematicas_basicas`.
# 2. Llama directamente a la función `restar` para restar 5 de 20. Imprime el resultado.
# 3. Imprime directamente el valor de `PI`.
# 4. Intenta llamar a la función `sumar` (sin usar el prefijo del módulo). ¿Qué sucede? (Comenta la línea).

print("\n--- Ejercicio 2: Importación Selectiva ---")
# Escribe tu código aquí
from matematicas_basicas import restar, PI

resultado_resta = restar(20, 5) # Llamada directa
print(f"Resta (20-5) usando 'from...import': {resultado_resta}")

print(f"Valor de PI importado directamente: {PI}")

# Intentar llamar a sumar directamente dará NameError porque no se importó así
# resultado_suma_directa = sumar(10, 2)
# print(resultado_suma_directa)


# --- Ejercicio 3: Importación con Alias (`as`) ---
# Instrucciones:
# 1. Importa el módulo completo `matematicas_basicas` usando el alias `mb`.
# 2. Importa la función `multiplicar` del módulo `matematicas_basicas` usando el alias `mult`.
# 3. Llama a la función `sumar` usando el alias del módulo (`mb.sumar`). Suma 100 y 50. Imprime el resultado.
# 4. Llama a la función `multiplicar` usando su alias (`mult`). Multiplica 9 por 9. Imprime el resultado.

print("\n--- Ejercicio 3: Importación con Alias ---")
# Escribe tu código aquí
import matematicas_basicas as mb
from matematicas_basicas import multiplicar as mult

resultado_suma_alias = mb.sumar(100, 50)
print(f"Suma (100+50) usando alias de módulo: {resultado_suma_alias}")

resultado_multi_alias = mult(9, 9)
print(f"Multiplicación (9*9) usando alias de función: {resultado_multi_alias}")


# --- Ejercicio 4: Creación y Uso de un Paquete (Requiere crear archivos/carpetas) ---
# Instrucciones:
# 1. **MANUALMENTE (fuera de este script):**
#    a. En el mismo directorio donde está este script (`Modulo_02_Python_Intermedio_Estructura`),
#       crea una NUEVA CARPETA llamada `mi_paquete_ejercicios`.
#    b. Dentro de `mi_paquete_ejercicios`, crea un ARCHIVO VACÍO llamado `__init__.py`.
#    c. Dentro de `mi_paquete_ejercicios`, crea un ARCHIVO llamado `utilidades.py` con el siguiente contenido:
#       ```python
#       # mi_paquete_ejercicios/utilidades.py
#       def formatear_texto(texto):
#           return texto.strip().capitalize()
#       ```
#    d. Dentro de `mi_paquete_ejercicios`, crea otro ARCHIVO llamado `calculos.py` con el siguiente contenido:
#       ```python
#       # mi_paquete_ejercicios/calculos.py
#       IVA = 0.21
#       def calcular_iva(monto):
#           return monto * IVA
#       ```
# 2. **EN ESTE SCRIPT (abajo):**
#    a. Importa la función `formatear_texto` desde `mi_paquete_ejercicios.utilidades`.
#    b. Importa la función `calcular_iva` y la variable `IVA` desde `mi_paquete_ejercicios.calculos`.
#    c. Llama a `formatear_texto` con una cadena como "  texto de prueba  " e imprime el resultado.
#    d. Llama a `calcular_iva` con un monto de 100 e imprime el resultado junto con el valor de `IVA`.

print("\n--- Ejercicio 4: Uso de Paquete ---")
print("(Asegúrate de haber creado la carpeta 'mi_paquete_ejercicios' y sus archivos)")

# Escribe tu código aquí (después de crear la estructura de carpetas/archivos)
try:
    from mi_paquete_ejercicios.utilidades import formatear_texto
    from mi_paquete_ejercicios.calculos import calcular_iva, IVA

    texto_original = "  texto de prueba  "
    texto_formateado = formatear_texto(texto_original)
    print(f"Texto original: '{texto_original}'")
    print(f"Texto formateado: '{texto_formateado}'")

    monto_base = 100
    iva_calculado = calcular_iva(monto_base)
    print(f"El IVA ({IVA*100}%) para ${monto_base} es: ${iva_calculado:.2f}")

except ImportError:
    print("\nERROR: No se pudo importar desde 'mi_paquete_ejercicios'.")
    print("Por favor, verifica que la carpeta y los archivos .py (incluyendo __init__.py) fueron creados correctamente.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# --- Fin de los ejercicios ---
