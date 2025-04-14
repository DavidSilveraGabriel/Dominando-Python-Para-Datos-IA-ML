# Módulo 1: Funciones (Definición, Parámetros, Retorno, Scope)

A medida que tus programas crecen, notarás que repites ciertas secuencias de código. Las **funciones** son la solución a esto. Una función es un bloque de código con nombre que realiza una tarea específica. Puedes "llamar" a la función por su nombre cada vez que necesites ejecutar ese bloque de código.

**Beneficios de usar Funciones:**

*   **Reutilización:** Escribes el código una vez y lo llamas múltiples veces.
*   **Organización:** Dividen programas grandes en partes más pequeñas y manejables.
*   **Legibilidad:** Dan nombres descriptivos a bloques de código, haciendo el programa más fácil de entender.
*   **Mantenimiento:** Si necesitas cambiar la lógica, solo la modificas en un lugar (la definición de la función).

## Definición de una Función (`def`)

Usamos la palabra clave `def` para definir una función.

**Sintaxis:**

```python
def nombre_de_la_funcion(parametro1, parametro2, ...):
    """
    Docstring opcional: Explica brevemente qué hace la función.
    Se escribe entre triples comillas.
    """
    # Bloque de código de la función (indentado)
    # Puede realizar cálculos, imprimir, llamar a otras funciones, etc.
    # ...
    # Opcionalmente, puede devolver un valor usando 'return'
    return valor_a_devolver # Opcional
```

*   `def`: Palabra clave que indica el inicio de la definición de una función.
*   `nombre_de_la_funcion`: Nombre que le das a la función (sigue las mismas convenciones que los nombres de variables: `snake_case`).
*   `()`: Paréntesis obligatorios. Dentro de ellos van los **parámetros** (variables que la función recibe), separados por comas. Si la función no recibe parámetros, los paréntesis van vacíos: `def mi_funcion():`.
*   `: `: Dos puntos obligatorios al final de la línea `def`.
*   `"""Docstring"""`: (Opcional pero muy recomendado) Una cadena de texto multilínea que documenta la función. Explica qué hace, qué parámetros recibe y qué devuelve.
*   **Bloque de código:** Las líneas de código indentadas que forman el cuerpo de la función.
*   `return valor_a_devolver`: (Opcional) Palabra clave que especifica el valor que la función enviará de vuelta a donde fue llamada. Si no hay `return`, la función devuelve implícitamente `None`.

## Llamada a una Función

Una vez definida, puedes ejecutar una función "llamándola" por su nombre seguido de paréntesis `()`. Si la función espera parámetros, debes proporcionar los **argumentos** (los valores concretos para esos parámetros) dentro de los paréntesis.

```python
# Definición de una función simple
def saludar():
    """Imprime un saludo simple."""
    print("¡Hola! Bienvenido/a.")

# Llamada a la función
saludar() # Salida: ¡Hola! Bienvenido/a.
saludar() # Puedes llamarla cuantas veces quieras

# Definición de una función con un parámetro
def saludar_a(nombre):
    """Imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}! ¿Cómo estás?")

# Llamada con un argumento
saludar_a("Ana")     # Salida: ¡Hola, Ana! ¿Cómo estás?
saludar_a("Pedro")   # Salida: ¡Hola, Pedro! ¿Cómo estás?

# Definición de una función con dos parámetros y retorno
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    resultado = a + b
    return resultado

# Llamada y almacenamiento del valor devuelto
total = sumar(5, 3)
print(f"El resultado de la suma es: {total}") # Salida: El resultado de la suma es: 8
print(sumar(10, -2)) # Salida: 8 (puedes imprimir directamente el valor devuelto)
```

## Parámetros y Argumentos

*   **Parámetros:** Son las variables listadas dentro de los paréntesis en la *definición* de la función. Actúan como placeholders para los valores que la función recibirá.
*   **Argumentos:** Son los valores reales que pasas a la función cuando la *llamas*.

**Tipos de Argumentos:**

1.  **Argumentos Posicionales:** Se asignan a los parámetros según su orden. El primer argumento va al primer parámetro, el segundo al segundo, etc.
    ```python
    def describir_mascota(tipo_animal, nombre_mascota):
        print(f"Tengo un {tipo_animal} llamado {nombre_mascota}.")

    describir_mascota("perro", "Fido") # "perro" va a tipo_animal, "Fido" a nombre_mascota
    ```

2.  **Argumentos de Palabra Clave (Keyword Arguments):** Especificas explícitamente a qué parámetro corresponde cada argumento usando `nombre_parametro=valor`. El orden no importa si usas argumentos de palabra clave.
    ```python
    describir_mascota(nombre_mascota="Mishi", tipo_animal="gato") # Funciona igual
    ```
    Puedes mezclar posicionales y de palabra clave, pero los posicionales deben ir *antes* que los de palabra clave.

## Parámetros con Valores por Defecto

Puedes asignar un valor por defecto a un parámetro en la definición de la función. Si al llamar la función no proporcionas un argumento para ese parámetro, usará el valor por defecto.

```python
def potencia(base, exponente=2): # exponente tiene valor por defecto 2
    """Calcula la base elevada al exponente."""
    return base ** exponente

print(potencia(5))      # Usa exponente=2 por defecto. Salida: 25
print(potencia(5, 3))   # Proporcionamos exponente=3. Salida: 125
print(potencia(base=3)) # Usa exponente=2 por defecto. Salida: 9
```
Los parámetros con valores por defecto deben ir *después* de los parámetros sin valor por defecto en la definición.

## La Declaración `return`

*   Se usa para enviar un valor de vuelta desde la función al lugar donde fue llamada.
*   Una función puede tener múltiples declaraciones `return` (por ejemplo, dentro de `if/else`), pero en cuanto se ejecuta una, la función termina inmediatamente.
*   Si una función no tiene una declaración `return`, o llega al final sin ejecutar una, devuelve `None` implícitamente.

```python
def dividir(a, b):
    """Divide a entre b. Devuelve el resultado o None si b es 0."""
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None # Devolvemos None explícitamente en caso de error
    else:
        return a / b

resultado1 = dividir(10, 2)
resultado2 = dividir(5, 0)

print(f"Resultado 1: {resultado1}") # Salida: Resultado 1: 5.0
print(f"Resultado 2: {resultado2}") # Salida: Resultado 2: None
```

## Alcance de las Variables (Scope)

*   **Variables Locales:** Las variables definidas *dentro* de una función (incluidos los parámetros) son **locales** a esa función. Solo existen mientras la función se está ejecutando y no pueden ser accedidas desde fuera de la función.
*   **Variables Globales:** Las variables definidas *fuera* de cualquier función son **globales**. Pueden ser accedidas (leídas) desde dentro de una función, pero si quieres *modificar* una variable global dentro de una función, necesitas usar la palabra clave `global` (aunque esto generalmente se considera una mala práctica y debe evitarse si es posible).

```python
variable_global = "Soy global"

def mi_funcion_scope():
    variable_local = "Soy local"
    print(f"Dentro de la función, puedo ver la local: {variable_local}")
    print(f"Dentro de la función, puedo ver la global: {variable_global}")

mi_funcion_scope()
# Salida:
# Dentro de la función, puedo ver la local: Soy local
# Dentro de la función, puedo ver la global: Soy global

print(f"Fuera de la función, puedo ver la global: {variable_global}")
# Salida: Fuera de la función, puedo ver la global: Soy global

# Esto daría un error (NameError) porque variable_local no existe fuera de la función:
# print(variable_local)

# Ejemplo (no recomendado) de modificar global
contador_global = 0
def incrementar_global():
    global contador_global # Indica que queremos modificar la global
    contador_global += 1
    print(f"Dentro de incrementar: {contador_global}")

incrementar_global() # Salida: Dentro de incrementar: 1
incrementar_global() # Salida: Dentro de incrementar: 2
print(f"Fuera, contador_global es: {contador_global}") # Salida: Fuera, contador_global es: 2
```

Las funciones son bloques de construcción fundamentales en Python. Dominarlas te permitirá escribir código más modular, organizado y fácil de mantener.
