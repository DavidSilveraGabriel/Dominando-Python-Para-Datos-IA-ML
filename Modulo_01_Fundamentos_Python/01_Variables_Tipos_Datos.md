# Módulo 1: Variables y Tipos de Datos Primitivos

Las **variables** son como contenedores o etiquetas que usamos para almacenar datos en la memoria del computador. Podemos asignarles un nombre y guardar diferentes tipos de información en ellas para usarla más tarde en nuestro programa.

## Asignación de Variables

En Python, asignamos un valor a una variable usando el operador de asignación, que es el signo igual (`=`).

```python
# Sintaxis: nombre_variable = valor

mensaje = "Hola, mundo!"  # Asigna el texto "Hola, mundo!" a la variable 'mensaje'
numero_entero = 42         # Asigna el número 42 a la variable 'numero_entero'
numero_decimal = 3.14159   # Asigna el número decimal 3.14159 a 'numero_decimal'
es_valido = True           # Asigna el valor booleano True a 'es_valido'

# Podemos imprimir el valor almacenado en una variable
print(mensaje)
print(numero_entero)
print(es_valido)

# El valor de una variable puede cambiar (son 'mutables' en este sentido)
numero_entero = 100
print(numero_entero) # Ahora imprime 100
```

## Nombres de Variables (Convenciones PEP 8)

Elegir buenos nombres para las variables hace tu código mucho más legible. Sigue estas convenciones (recomendadas por PEP 8):

*   **Usa nombres descriptivos:** `edad_usuario` es mejor que `e` o `x`.
*   **Estilo `snake_case`:** Usa letras minúsculas y separa las palabras con guiones bajos (`_`). Ejemplo: `tasa_interes`, `nombre_completo`.
*   **No uses palabras reservadas:** No puedes nombrar una variable con palabras que Python usa para su sintaxis, como `if`, `else`, `for`, `while`, `class`, `def`, `True`, `False`, `None`, etc.
*   **No empieces con números:** Un nombre de variable no puede empezar con un número (ej. `1variable` es inválido), pero puede contener números después de la primera letra (ej. `variable1` es válido).
*   **Distinción entre mayúsculas y minúsculas:** `miVariable` y `mivariable` son dos variables diferentes. Sin embargo, por convención, se prefiere `snake_case`.
*   **Evita caracteres especiales:** Aparte del guion bajo, evita usar otros símbolos como `!`, `@`, `#`, `$`, `%`, etc.

```python
# Buenos nombres
contador_visitas = 0
precio_total = 99.95
usuario_activo = False

# Malos nombres (evitar)
# x = 0           # No descriptivo
# total$ = 99.95  # Caracter inválido
# class = "Python" # Palabra reservada
# 2do_nombre = "Perez" # Empieza con número
```

## Tipos de Datos Primitivos

Python tiene varios tipos de datos incorporados para representar diferentes clases de información. Los más básicos (primitivos) son:

1.  **Enteros (`int`):** Números enteros, positivos o negativos, sin parte decimal.
    ```python
    edad = 35
    cantidad = -10
    año = 2024
    ```

2.  **Flotantes (`float`):** Números con parte decimal. Se usa el punto (`.`) como separador decimal.
    ```python
    precio = 19.99
    temperatura = -5.5
    pi = 3.14159
    altura = 1.75
    ```

3.  **Booleanos (`bool`):** Representan valores de verdad: `True` (verdadero) o `False` (falso). Son fundamentales para la toma de decisiones (condicionales). ¡Ojo! Se escriben con la primera letra en mayúscula.
    ```python
    es_mayor_de_edad = True
    tiene_descuento = False
    sistema_activo = True
    ```

4.  **Cadenas de Texto (`str` - Strings):** Secuencias de caracteres (letras, números, símbolos) encerradas entre comillas simples (`'...'`) o dobles (`"..."`).
    ```python
    nombre = "Alice"
    saludo = '¡Bienvenido!'
    direccion = "Calle Falsa 123"
    mensaje_largo = """Este es un string
    que ocupa varias
    líneas.""" # También se pueden usar comillas triples para strings multilínea
    ```

## Verificando el Tipo de Dato (`type()`)

Puedes usar la función incorporada `type()` para saber de qué tipo es una variable o un valor.

```python
numero = 10
texto = "Python"
decimal = 9.8
logico = False

print(type(numero))    # Salida: <class 'int'>
print(type(texto))     # Salida: <class 'str'>
print(type(decimal))   # Salida: <class 'float'>
print(type(logico))    # Salida: <class 'bool'>
print(type(99))        # Salida: <class 'int'>
print(type("Hola"))    # Salida: <class 'str'>
```

Python es un lenguaje de **tipado dinámico**, lo que significa que no necesitas declarar explícitamente el tipo de una variable. Python lo infiere automáticamente cuando le asignas un valor. Además, una misma variable puede contener diferentes tipos de datos en diferentes momentos (aunque no siempre es una buena práctica cambiar el tipo drásticamente).

```python
mi_variable = 10
print(type(mi_variable)) # <class 'int'>

mi_variable = "Ahora soy un string"
print(type(mi_variable)) # <class 'str'>
```

Entender las variables y los tipos de datos es el primer paso esencial para poder manipular información en tus programas Python. ¡A practicar!
