# Módulo 8: Manejo Avanzado de Excepciones

Ya introdujimos el manejo básico de errores con `try`, `except`, `else`, y `finally` en el Módulo 1. Ahora profundizaremos en algunos aspectos más avanzados para un control de errores más robusto y específico.

## Jerarquía de Excepciones

Python tiene una jerarquía incorporada de excepciones. Todas las excepciones heredan de la clase base `BaseException`, y la mayoría de las excepciones comunes que encontraremos heredan de `Exception`.

Algunas excepciones comunes y su relación (simplificada):

```
BaseException
 +-- SystemExit        # Lanzada por sys.exit()
 +-- KeyboardInterrupt # Lanzada cuando el usuario presiona Ctrl+C
 +-- Exception         # Clase base para errores no relacionados con la salida del sistema
      +-- StopIteration     # Lanzada por next() cuando el iterador se agota
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      |    +-- OverflowError
      |    +-- FloatingPointError
      +-- AssertionError    # Lanzada por la declaración assert
      +-- AttributeError    # Atributo o método no encontrado
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError    # Índice de secuencia fuera de rango
      |    +-- KeyError      # Clave de diccionario no encontrada
      +-- MemoryError
      +-- NameError         # Variable local o global no encontrada
      +-- OSError           # Error del sistema operativo (ej. archivo no encontrado)
      |    +-- FileNotFoundError
      |    +-- PermissionError
      |    +-- ConnectionError
      +-- RuntimeError      # Errores que no caen en otras categorías
      |    +-- NotImplementedError
      +-- SyntaxError       # Error de sintaxis (hereda de Exception pero se maneja diferente)
      +-- IndentationError  # Error de sangría (subclase de SyntaxError)
      +-- TypeError         # Operación o función aplicada a un objeto de tipo inapropiado
      +-- ValueError        # Operación o función recibe argumento con tipo correcto pero valor inapropiado
           +-- UnicodeError
```

**¿Por qué es útil la jerarquía?**

Un bloque `except` puede capturar no solo la excepción específica mencionada, sino también **cualquier excepción que herede de ella**.

```python
try:
    # x = 1 / 0 # ZeroDivisionError
    # lista = []
    # print(lista[1]) # IndexError
    d = {}
    print(d['clave_no_existe']) # KeyError
except LookupError as e:
    # Esto captura IndexError y KeyError (y otras LookupError si las hubiera)
    print(f"Error de búsqueda capturado (LookupError): {type(e).__name__}: {e}")
except ZeroDivisionError as e:
    print(f"Error aritmético capturado: {type(e).__name__}: {e}")
except Exception as e:
    # Captura cualquier otra excepción que herede de Exception
    print(f"Otra excepción capturada: {type(e).__name__}: {e}")

```

*   **Buenas Prácticas:**
    *   Sé **específico** en los bloques `except`. Captura los errores que *esperas* y sabes cómo manejar.
    *   Evita `except:` sin tipo o `except Exception:` genéricos a menos que sea realmente necesario (ej. para logging de último recurso), ya que pueden ocultar errores inesperados o de programación.
    *   Ordena los bloques `except` del más específico al más general. Python usará el primer bloque que coincida.

## Lanzando Excepciones (`raise`)

A veces, quieres señalar explícitamente que ha ocurrido una condición de error en tu propio código. Puedes **lanzar** (o relanzar) excepciones usando la palabra clave `raise`.

```python
def calcular_raiz_cuadrada(numero):
    """Calcula la raíz cuadrada, lanza ValueError si el número es negativo."""
    if numero < 0:
        # Lanzamos una excepción específica con un mensaje descriptivo
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return numero ** 0.5

try:
    print(calcular_raiz_cuadrada(25))
    print(calcular_raiz_cuadrada(-4)) # Esto lanzará la excepción
except ValueError as e:
    print(f"Error al calcular raíz: {e}")

# Relanzar una excepción (útil dentro de un except para añadir info o dejar que un nivel superior la maneje)
def funcion_intermedia(valor):
    try:
        resultado = calcular_raiz_cuadrada(valor)
        print("Cálculo intermedio exitoso.")
        return resultado
    except ValueError as e:
        print(f"Error en funcion_intermedia: {e}. Relanzando...")
        # Podrías añadir más contexto aquí antes de relanzar
        raise # Relanza la misma excepción 'e' que fue capturada

print("\nProbando relanzamiento:")
try:
    funcion_intermedia(-10)
except ValueError as e:
    print(f"Excepción capturada en el nivel superior después de relanzar: {e}")
```

## Creando Excepciones Personalizadas

Para errores específicos de tu aplicación o biblioteca, puedes crear tus propias clases de excepción heredando de `Exception` (o de una excepción más específica). Esto hace tu manejo de errores más claro y semántico.

```python
# Definir una excepción personalizada
class ErrorDeValidacion(ValueError): # Hereda de ValueError (o Exception)
    """Excepción lanzada por errores de validación específicos de la aplicación."""
    pass # No necesita cuerpo adicional, hereda todo

class ValorDemasiadoAltoError(ErrorDeValidacion): # Puede tener sub-excepciones
    """Error específico si un valor supera un límite."""
    def __init__(self, valor, limite):
        mensaje = f"El valor {valor} supera el límite permitido de {limite}."
        super().__init__(mensaje) # Llama al __init__ de la clase padre (ValueError)
        self.valor = valor
        self.limite = limite

def procesar_nivel(nivel):
    if not isinstance(nivel, int):
        raise TypeError("El nivel debe ser un entero.")
    if nivel < 0:
        # Usamos nuestra excepción personalizada
        raise ErrorDeValidacion("El nivel no puede ser negativo.")
    if nivel > 100:
        raise ValorDemasiadoAltoError(valor=nivel, limite=100)
    print(f"Procesando nivel {nivel}... OK.")

# Manejando excepciones personalizadas
print("\nProbando excepciones personalizadas:")
for n in [50, -5, 150, "abc"]:
    try:
        procesar_nivel(n)
    except ValorDemasiadoAltoError as e: # Captura el error más específico primero
        print(f"Error específico capturado: {e} (Valor={e.valor}, Límite={e.limite})")
    except ErrorDeValidacion as e: # Captura otros errores de validación
        print(f"Error de validación capturado: {e}")
    except TypeError as e: # Captura errores de tipo
        print(f"Error de tipo capturado: {e}")
    except Exception as e: # Captura cualquier otro error inesperado
        print(f"Error inesperado: {type(e).__name__}: {e}")

```

## Encadenamiento de Excepciones (`raise ... from ...`)

Cuando capturas una excepción y lanzas otra diferente como resultado (ej. un error de bajo nivel causa un error de más alto nivel en tu lógica), puedes usar `raise NuevaExcepcion from excepcion_original` para preservar la información sobre la causa raíz. Esto mejora la depuración al mostrar ambas excepciones en el traceback.

```python
class ErrorProcesamientoArchivo(Exception):
    pass

def procesar_archivo(ruta):
    try:
        with open(ruta, 'r') as f:
            # ... procesar contenido ...
            if "ERROR_DATA" in f.read(): # Simular error en datos
                 raise ValueError("Formato de datos inválido en el archivo.")
            print(f"Archivo '{ruta}' procesado OK.")
    except FileNotFoundError as e:
        # Lanzamos nuestra excepción, indicando la causa original
        raise ErrorProcesamientoArchivo(f"No se pudo encontrar el archivo: {ruta}") from e
    except ValueError as e:
        raise ErrorProcesamientoArchivo(f"Error en el contenido del archivo: {ruta}") from e
    except OSError as e:
        raise ErrorProcesamientoArchivo(f"Error de OS al leer archivo: {ruta}") from e

print("\nProbando encadenamiento de excepciones:")
try:
    # procesar_archivo("archivo_que_no_existe.txt")
    # Crear un archivo con "ERROR_DATA" para probar el otro caso
    with open("archivo_con_error.txt", "w") as f: f.write("ERROR_DATA")
    procesar_archivo("archivo_con_error.txt")
except ErrorProcesamientoArchivo as e:
    print(f"Error principal: {e}")
    # El traceback mostrará ambas excepciones (ErrorProcesamientoArchivo y la causa original)
    # print("\nCausa original:")
    # print(e.__cause__) # Acceder a la excepción original
```

Un manejo de excepciones avanzado y bien estructurado, utilizando la jerarquía, excepciones personalizadas y encadenamiento, hace que tus programas sean mucho más robustos, fáciles de depurar y mantener.
