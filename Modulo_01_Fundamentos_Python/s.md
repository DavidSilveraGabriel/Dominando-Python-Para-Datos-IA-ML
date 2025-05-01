# Módulo 1: Sintaxis Básica, Comentarios y Sangría

¡Bienvenido/a al Módulo 1! Aquí empezamos a escribir código Python real. Cubriremos los elementos más fundamentales de la sintaxis del lenguaje.

## Ejecutando Código Python

Hay varias formas de ejecutar código Python:

1.  **Modo Interactivo (REPL):**
    *   Abre tu terminal (o Anaconda Prompt).
    *   Escribe `python` y presiona Enter.
    *   Verás un prompt como `>>>`. Aquí puedes escribir código Python línea por línea y ver el resultado inmediatamente.
    *   Es útil para pruebas rápidas y experimentar.
    *   Para salir, escribe `exit()` o presiona `Ctrl+Z` (Windows) / `Ctrl+D` (macOS/Linux) y Enter.

    ```python
    >>> print("¡Hola, Python interactivo!")
    ¡Hola, Python interactivo!
    >>> 2 + 3
    5
    >>> exit()
    ```

2.  **Scripts (`.py`):**
    *   Escribe tu código en un archivo de texto con la extensión `.py` (ej. `mi_script.py`) usando un editor como VS Code.
    *   Guarda el archivo.
    *   Abre tu terminal, navega hasta el directorio donde guardaste el archivo usando `cd`.
    *   Ejecuta el script escribiendo: `python mi_script.py`

    ```python
    # Contenido de mi_script.py
    mensaje = "¡Hola desde un script!"
    print(mensaje)
    numero = 10 + 5
    print(f"El resultado es: {numero}")
    ```
    *   En la terminal: `python mi_script.py`

3.  **Jupyter Notebooks/Lab:**
    *   Como vimos en el Módulo 0, puedes escribir y ejecutar código en celdas dentro de un entorno interactivo basado en web. Ideal para análisis de datos.

## La Función `print()`

La función `print()` es una de las más usadas. Sirve para mostrar mensajes o los valores de las variables en la consola o en la salida de la celda de Jupyter.

```python
print("Este es un mensaje.")
nombre = "Ana"
edad = 30
print("Nombre:", nombre, "Edad:", edad)
print(f"Forma moderna (f-string): Mi nombre es {nombre} y tengo {edad} años.") # f-strings son muy útiles!
```

## Comentarios

Los comentarios son líneas en tu código que Python ignora al ejecutarse. Sirven para explicar qué hace el código, dejar notas o deshabilitar temporalmente alguna línea.

*   **Comentario de una línea:** Empieza con el símbolo `#`. Todo lo que sigue en esa línea es un comentario.
*   **Comentario multilínea (Docstring - uso específico):** Se usan tres comillas dobles `"""` o simples `'''` al inicio y al final. Aunque técnicamente son strings, se usan comúnmente al inicio de funciones, clases o módulos para documentar su propósito (lo veremos más adelante).

```python
# Esto es un comentario de una sola línea. Explica la siguiente línea.
velocidad = 90 # km/h - También puedes poner comentarios al final de una línea de código.

# print("Esta línea no se ejecutará porque está comentada")

"""
Esto es un string multilínea,
a menudo usado como 'docstring' para documentar.
Python no lo ejecuta como código, pero no es un comentario
en el mismo sentido que #. Lo veremos en funciones.
"""
```

## Sangría (Indentation) - ¡CRÍTICO EN PYTHON!

A diferencia de muchos otros lenguajes que usan llaves `{}` o palabras clave como `begin`/`end` para definir bloques de código (como el cuerpo de un `if`, un bucle `for` o una función), **Python usa la sangría**.

*   **¿Qué es?** Son los espacios en blanco al inicio de una línea.
*   **¿Por qué es importante?** ¡Define la estructura del programa! Las líneas de código que pertenecen al mismo bloque *deben* tener el mismo nivel de sangría.
*   **Estándar:** La convención (definida en PEP 8) es usar **4 espacios** por cada nivel de sangría. **No mezcles tabulaciones y espacios.** Configura tu editor (VS Code) para que inserte 4 espacios cuando presiones la tecla `Tab`.
*   **Errores:** Una sangría incorrecta (`IndentationError`) es uno de los errores más comunes al empezar con Python.

```python
# Ejemplo CORRECTO
puntaje = 75

if puntaje > 50:
    print("¡Aprobado!") # Este print pertenece al bloque del if (tiene 4 espacios de sangría)
    print("Felicidades.") # Esta línea también pertenece al if
print("Fin de la evaluación.") # Esta línea está fuera del if (sin sangría)

# Ejemplo INCORRECTO (causará IndentationError)
# if puntaje > 50:
# print("Error de sangría") # Falta la sangría

# Ejemplo INCORRECTO (causará IndentationError)
# if puntaje > 50:
#     print("Nivel 1")
#        print("Nivel 2 incorrecto") # Sangría inconsistente
```

**¡La sangría es obligatoria y fundamental en Python!** Acostúmbrate a ser consistente con ella desde el principio.

Con estos conceptos básicos de sintaxis, comentarios y la crucial sangría, estás listo/a para aprender sobre variables y tipos de datos.


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


# Módulo 1: Operadores (Aritméticos, Comparación, Lógicos)

Los operadores nos permiten realizar diferentes tipos de operaciones con nuestras variables y valores. Son símbolos especiales que le dicen a Python qué hacer.

## Operadores Aritméticos

Se utilizan para realizar operaciones matemáticas comunes.

| Operador | Descripción          | Ejemplo (`a=10`, `b=3`) | Resultado |
| :------- | :------------------- | :---------------------- | :-------- |
| `+`      | Suma                 | `a + b`                 | `13`      |
| `-`      | Resta                | `a - b`                 | `7`       |
| `*`      | Multiplicación       | `a * b`                 | `30`      |
| `/`      | División             | `a / b`                 | `3.333...`|
| `//`     | División Entera      | `a // b`                | `3`       |
| `%`      | Módulo (Resto)       | `a % b`                 | `1`       |
| `**`     | Exponenciación       | `a ** b`                | `1000`    |

```python
num1 = 15
num2 = 4

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2          # División real (siempre devuelve float)
division_entera = num1 // num2  # Descarta la parte decimal
modulo = num1 % num2            # Resto de la división entera
potencia = num2 ** 3            # 4 elevado a 3

print(f"Suma: {suma}")                 # Salida: Suma: 19
print(f"Resta: {resta}")               # Salida: Resta: 11
print(f"Multiplicación: {multiplicacion}") # Salida: Multiplicación: 60
print(f"División: {division}")         # Salida: División: 3.75
print(f"División Entera: {division_entera}") # Salida: División Entera: 3
print(f"Módulo: {modulo}")             # Salida: Módulo: 3
print(f"Potencia: {potencia}")         # Salida: Potencia: 64

# Orden de operaciones (PEMDAS/BODMAS) se respeta
resultado = 5 + 2 * 3  # Primero 2*3, luego + 5
print(f"Resultado (orden op): {resultado}") # Salida: Resultado (orden op): 11
```

## Operadores de Comparación

Se utilizan para comparar dos valores. El resultado de una comparación es siempre un valor booleano (`True` o `False`).

| Operador | Descripción              | Ejemplo (`x=5`, `y=8`) | Resultado |
| :------- | :----------------------- | :---------------------- | :-------- |
| `==`     | Igual a                  | `x == y`                | `False`   |
| `!=`     | No igual a (Diferente)   | `x != y`                | `True`    |
| `>`      | Mayor que                | `x > y`                 | `False`   |
| `<`      | Menor que                | `x < y`                 | `True`    |
| `>=`     | Mayor o igual que        | `x >= 5`                | `True`    |
| `<=`     | Menor o igual que        | `y <= 8`                | `True`    |

```python
edad_juan = 25
edad_maria = 30
altura_minima = 1.60
altura_persona = 1.75

print(f"¿Juan y María tienen la misma edad? {edad_juan == edad_maria}") # False
print(f"¿Juan es mayor que María? {edad_juan > edad_maria}")          # False
print(f"¿María tiene 30 años o menos? {edad_maria <= 30}")           # True
print(f"¿La persona cumple la altura mínima? {altura_persona >= altura_minima}") # True
print(f"¿Las edades son diferentes? {edad_juan != edad_maria}")       # True
```

Estos operadores son cruciales para las estructuras de control como `if`, `elif`, `else` y los bucles `while`.

## Operadores Lógicos

Se utilizan para combinar expresiones booleanas (`True`/`False`).

| Operador | Descripción                                     | Ejemplo (`a=True`, `b=False`) | Resultado |
| :------- | :---------------------------------------------- | :---------------------------- | :-------- |
| `and`    | Devuelve `True` si **ambas** expresiones son `True` | `a and b`                     | `False`   |
| `or`     | Devuelve `True` si **al menos una** expresión es `True` | `a or b`                      | `True`    |
| `not`    | Invierte el valor booleano                      | `not a`                       | `False`   |

```python
usuario_registrado = True
tiene_pago_al_dia = False
es_admin = False

# ¿Puede acceder al contenido premium? (registrado Y pago al día)
acceso_premium = usuario_registrado and tiene_pago_al_dia
print(f"Acceso Premium: {acceso_premium}") # Salida: Acceso Premium: False

# ¿Puede acceder al panel de control? (registrado Y (pago al día O es admin))
acceso_panel = usuario_registrado and (tiene_pago_al_dia or es_admin)
print(f"Acceso Panel: {acceso_panel}") # Salida: Acceso Panel: False (porque es_admin es False)

es_admin = True # Cambiamos el valor de es_admin
acceso_panel = usuario_registrado and (tiene_pago_al_dia or es_admin)
print(f"Acceso Panel (ahora admin): {acceso_panel}") # Salida: Acceso Panel (ahora admin): True

# Invertir un valor
no_esta_registrado = not usuario_registrado
print(f"No está registrado: {no_esta_registrado}") # Salida: No está registrado: False
```

**Cortocircuito (Short-circuiting):**

*   En una expresión `a and b`, si `a` es `False`, Python no necesita evaluar `b`, porque el resultado ya será `False`.
*   En una expresión `a or b`, si `a` es `True`, Python no necesita evaluar `b`, porque el resultado ya será `True`.
    Esto puede ser útil para evitar errores si la segunda parte depende de la primera.

## Operadores de Asignación

Además del `=` básico, existen operadores combinados que realizan una operación aritmética y asignan el resultado a la variable original.

| Operador | Equivalente a | Ejemplo (`c=10`) | Resultado en `c` |
| :------- | :------------ | :--------------- | :--------------- |
| `+=`     | `c = c + 5`   | `c += 5`         | `15`             |
| `-=`     | `c = c - 2`   | `c -= 2`         | `8`              |
| `*=`     | `c = c * 3`   | `c *= 3`         | `30`             |
| `/=`     | `c = c / 2`   | `c /= 2`         | `5.0`            |
| `//=`    | `c = c // 3`  | `c //= 3`        | `3`              |
| `%=`     | `c = c % 4`   | `c %= 4`         | `2`              |
| `**=`    | `c = c ** 2`  | `c **= 2`        | `100`            |

```python
contador = 0
contador += 1  # Incrementa en 1 (muy común)
print(f"Contador: {contador}") # Salida: Contador: 1

total = 100
total -= 10 # Decrementa en 10
print(f"Total: {total}")   # Salida: Total: 90
```

Estos operadores son una forma concisa de modificar el valor de una variable basándose en su valor actual.

Dominar los operadores es esencial para realizar cálculos, tomar decisiones y controlar el flujo de tus programas.
# Módulo 1: Estructuras de Datos (Listas, Tuplas, Diccionarios, Conjuntos)

Además de los tipos de datos primitivos (int, float, bool, str), Python ofrece estructuras de datos incorporadas muy potentes para agrupar y organizar información. Las más importantes son:

## 1. Listas (`list`)

*   **¿Qué son?** Colecciones **ordenadas** y **mutables** (modificables) de elementos. Pueden contener elementos de diferentes tipos.
*   **Sintaxis:** Se definen usando corchetes `[]`, con los elementos separados por comas.
*   **Características Clave:**
    *   **Ordenadas:** Los elementos mantienen el orden en que se añadieron.
    *   **Mutables:** Puedes añadir, eliminar o modificar elementos después de crear la lista.
    *   **Indexadas:** Puedes acceder a los elementos por su posición (índice), empezando desde 0.
    *   **Permiten Duplicados:** Una lista puede contener el mismo elemento varias veces.

```python
# Crear listas
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza"]
mixta = [10, "hola", True, 3.14]
vacia = []

print(numeros)   # Salida: [1, 2, 3, 4, 5]
print(frutas)    # Salida: ['manzana', 'banana', 'cereza']
print(mixta)     # Salida: [10, 'hola', True, 3.14]

# Acceder a elementos por índice (base 0)
print(frutas[0])  # Salida: manzana
print(frutas[1])  # Salida: banana
print(numeros[-1]) # Índice negativo: empieza desde el final (-1 es el último) -> Salida: 5

# Modificar elementos (mutabilidad)
frutas[1] = "pera"
print(frutas)     # Salida: ['manzana', 'pera', 'cereza']

# Añadir elementos
frutas.append("naranja") # Añade al final
print(frutas)     # Salida: ['manzana', 'pera', 'cereza', 'naranja']
frutas.insert(1, "kiwi") # Inserta en una posición específica
print(frutas)     # Salida: ['manzana', 'kiwi', 'pera', 'cereza', 'naranja']

# Eliminar elementos
frutas.remove("pera") # Elimina la primera ocurrencia del valor
print(frutas)     # Salida: ['manzana', 'kiwi', 'cereza', 'naranja']
elemento_eliminado = frutas.pop(2) # Elimina por índice y devuelve el elemento
print(frutas)     # Salida: ['manzana', 'kiwi', 'naranja']
print(f"Elemento eliminado: {elemento_eliminado}") # Salida: Elemento eliminado: cereza
del frutas[0]     # Elimina por índice usando 'del'
print(frutas)     # Salida: ['kiwi', 'naranja']

# Longitud de la lista
print(len(frutas)) # Salida: 2

# Verificar si un elemento está en la lista
print("kiwi" in frutas) # Salida: True
print("uva" not in frutas) # Salida: True
```

## 2. Tuplas (`tuple`)

*   **¿Qué son?** Colecciones **ordenadas** e **inmutables** (no modificables) de elementos.
*   **Sintaxis:** Se definen usando paréntesis `()`, con los elementos separados por comas. (Los paréntesis son opcionales en algunos casos, pero recomendados por claridad).
*   **Características Clave:**
    *   **Ordenadas:** Mantienen el orden.
    *   **Inmutables:** Una vez creadas, no puedes añadir, eliminar ni modificar sus elementos.
    *   **Indexadas:** Puedes acceder a los elementos por su índice (base 0).
    *   **Permiten Duplicados:** Pueden contener elementos repetidos.
    *   **Más eficientes (en memoria y velocidad) que las listas para datos fijos.**

```python
# Crear tuplas
coordenadas = (10.5, -3.2)
colores_rgb = (255, 0, 128)
un_elemento = (5,) # ¡Ojo! Coma final necesaria para tupla de un solo elemento
mixta_tupla = (1, "dos", False)
vacia_tupla = ()

print(coordenadas)    # Salida: (10.5, -3.2)
print(colores_rgb)    # Salida: (255, 0, 128)
print(un_elemento)    # Salida: (5,)

# Acceder a elementos por índice
print(coordenadas[0]) # Salida: 10.5
print(colores_rgb[-1])# Salida: 128

# Intentar modificar una tupla dará error (TypeError)
# coordenadas[0] = 5.0 # Esto generaría un error

# Longitud de la tupla
print(len(colores_rgb)) # Salida: 3

# Verificar pertenencia
print(255 in colores_rgb) # Salida: True

# Usos comunes: coordenadas, registros de bases de datos, claves de diccionario compuestas (lo veremos).
```

## 3. Diccionarios (`dict`)

*   **¿Qué son?** Colecciones **desordenadas** (en versiones de Python < 3.7, ordenadas por inserción en >= 3.7) y **mutables** de pares **clave-valor**.
*   **Sintaxis:** Se definen usando llaves `{}`, con pares `clave: valor` separados por comas.
*   **Características Clave:**
    *   **Clave-Valor:** Cada elemento tiene una clave única que se usa para acceder a su valor asociado.
    *   **Claves Únicas e Inmutables:** Las claves deben ser únicas dentro del diccionario y deben ser de un tipo inmutable (strings, números, tuplas son comunes).
    *   **Mutables:** Puedes añadir, eliminar o modificar pares clave-valor.
    *   **Acceso por Clave:** No se accede por índice numérico, sino por la clave.
    *   **Optimizados para Búsqueda:** Muy eficientes para buscar un valor si conoces su clave.

```python
# Crear diccionarios
estudiante = {
    "nombre": "Carlos",
    "edad": 22,
    "curso": "Ingeniería",
    "activo": True
}
capitales = {"España": "Madrid", "Francia": "París", "Italia": "Roma"}
vacio_dict = {}

print(estudiante)
print(capitales)

# Acceder a valores por clave
print(estudiante["nombre"])  # Salida: Carlos
print(capitales["Francia"]) # Salida: París
# print(estudiante["apellido"]) # Daría KeyError si la clave no existe

# Acceso seguro con .get() (devuelve None si no existe, o un valor por defecto)
print(estudiante.get("edad"))      # Salida: 22
print(estudiante.get("apellido"))  # Salida: None
print(estudiante.get("apellido", "No especificado")) # Salida: No especificado

# Modificar valores
estudiante["edad"] = 23
print(estudiante)

# Añadir nuevos pares clave-valor
estudiante["universidad"] = "Universidad XYZ"
capitales["Alemania"] = "Berlín"
print(estudiante)
print(capitales)

# Eliminar pares clave-valor
del estudiante["activo"]
print(estudiante)
valor_eliminado = capitales.pop("Italia")
print(capitales)
print(f"Capital eliminada: {valor_eliminado}") # Salida: Capital eliminada: Roma

# Obtener claves, valores o pares (clave, valor)
print(list(estudiante.keys()))   # Salida: ['nombre', 'edad', 'curso', 'universidad'] (convertido a lista)
print(list(estudiante.values())) # Salida: ['Carlos', 23, 'Ingeniería', 'Universidad XYZ']
print(list(estudiante.items()))  # Salida: [('nombre', 'Carlos'), ('edad', 23), ('curso', 'Ingeniería'), ('universidad', 'Universidad XYZ')]

# Longitud (número de pares)
print(len(estudiante)) # Salida: 4

# Verificar si una clave existe
print("nombre" in estudiante) # Salida: True
print("Paris" in capitales)  # Salida: False (busca en claves, no valores)
```

## 4. Conjuntos (`set`)

*   **¿Qué son?** Colecciones **desordenadas** y **mutables** de elementos **únicos**.
*   **Sintaxis:** Se definen usando llaves `{}` o la función `set()`, con elementos separados por comas. ¡Ojo! `{}` crea un diccionario vacío, para un conjunto vacío usa `set()`.
*   **Características Clave:**
    *   **Desordenados:** No garantizan ningún orden específico de los elementos.
    *   **Elementos Únicos:** No permiten elementos duplicados. Si intentas añadir un elemento que ya existe, simplemente se ignora.
    *   **Mutables:** Puedes añadir o eliminar elementos.
    *   **No Indexados:** No puedes acceder a elementos por índice.
    *   **Optimizados para Pertenencia:** Muy eficientes para comprobar si un elemento está presente en el conjunto.
    *   **Operaciones de Conjuntos:** Soportan operaciones matemáticas como unión, intersección, diferencia.

```python
# Crear conjuntos
numeros_set = {1, 2, 3, 4, 5, 5, 5} # Los duplicados se eliminan
letras = set("hola mundo") # Crea un conjunto con las letras únicas
vacio_set = set() # Conjunto vacío

print(numeros_set) # Salida: {1, 2, 3, 4, 5} (el orden puede variar)
print(letras)      # Salida: {'o', 'u', 'd', 'l', 'h', ' ', 'n', 'm'} (el orden puede variar)
print(vacio_set)   # Salida: set()

# Añadir elementos
numeros_set.add(6)
numeros_set.add(3) # No hace nada porque 3 ya está
print(numeros_set) # Salida: {1, 2, 3, 4, 5, 6}

# Eliminar elementos
numeros_set.remove(4) # Elimina el elemento. Da KeyError si no existe.
print(numeros_set) # Salida: {1, 2, 3, 5, 6}
numeros_set.discard(2) # Elimina si existe, no da error si no existe.
numeros_set.discard(10) # No hace nada, no da error.
print(numeros_set) # Salida: {1, 3, 5, 6}
elemento_pop = numeros_set.pop() # Elimina y devuelve un elemento arbitrario
print(f"Elemento eliminado con pop: {elemento_pop}")
print(numeros_set)

# Longitud
print(len(letras))

# Verificar pertenencia (muy rápido)
print('a' in letras) # Salida: True
print('z' in letras) # Salida: False

# Operaciones de conjuntos
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a.union(set_b) # o set_a | set_b
print(f"Unión: {union}") # Salida: Unión: {1, 2, 3, 4, 5, 6}

interseccion = set_a.intersection(set_b) # o set_a & set_b
print(f"Intersección: {interseccion}") # Salida: Intersección: {3, 4}

diferencia = set_a.difference(set_b) # o set_a - set_b (elementos en A pero no en B)
print(f"Diferencia (A-B): {diferencia}") # Salida: Diferencia (A-B): {1, 2}

diferencia_simetrica = set_a.symmetric_difference(set_b) # o set_a ^ set_b (elementos en A o B, pero no en ambos)
print(f"Diferencia Simétrica: {diferencia_simetrica}") # Salida: Diferencia Simétrica: {1, 2, 5, 6}
```

Elegir la estructura de datos correcta (lista, tupla, diccionario o conjunto) depende de lo que necesites hacer con tus datos: ¿necesitas orden? ¿modificabilidad? ¿unicidad? ¿acceso rápido por clave? Entender sus diferencias es clave para escribir código Python eficiente y efectivo.
# Módulo 1: Control de Flujo - Condicionales (`if`, `elif`, `else`)

Hasta ahora, nuestro código se ejecuta línea por línea, de arriba abajo. Pero a menudo necesitamos que nuestros programas tomen decisiones y sigan caminos diferentes según ciertas condiciones. Para eso usamos las **estructuras condicionales**.

La estructura condicional fundamental en Python es `if`, `elif` (contracción de "else if"), y `else`.

## La Declaración `if`

La declaración `if` ejecuta un bloque de código **solo si** una condición especificada es `True`.

**Sintaxis:**

```python
if condicion:
    # Bloque de código a ejecutar si la condicion es True
    # ¡Recuerda la sangría (4 espacios)!
    print("La condición es verdadera.")
# El código fuera del bloque if (sin sangría) se ejecuta siempre
print("Esto se ejecuta después del if, independientemente de la condición.")
```

*   `condicion`: Es una expresión que evalúa a un valor booleano (`True` o `False`). Usualmente involucra operadores de comparación (`==`, `!=`, `>`, `<`, `>=`, `<=`) y/o lógicos (`and`, `or`, `not`).
*   Los dos puntos (`:`) al final de la línea `if` son obligatorios.
*   El bloque de código indentado debajo del `if` solo se ejecuta si la `condicion` es `True`.

**Ejemplo:**

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad.") # Esta línea se ejecuta

temperatura = 15

if temperatura < 20:
    print("Hace un poco de frío.") # Esta línea se ejecuta
```

## La Declaración `else`

La declaración `else` se puede añadir opcionalmente después de un `if`. Ejecuta un bloque de código **solo si** la condición del `if` es `False`.

**Sintaxis:**

```python
if condicion:
    # Bloque si la condicion es True
    print("Condición verdadera.")
else:
    # Bloque si la condicion es False
    # ¡También requiere sangría!
    print("Condición falsa.")
print("Fin del bloque if-else.")
```

*   El `else` no lleva condición propia, simplemente captura el caso en que la condición del `if` no se cumplió.
*   Debe estar al mismo nivel de sangría que el `if` al que pertenece.

**Ejemplo:**

```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.") # Esta línea se ejecuta

nota = 75

if nota >= 60:
    print("Aprobado.") # Esta línea se ejecuta
else:
    print("Reprobado.")
```

## La Declaración `elif` (Else If)

A veces necesitas comprobar múltiples condiciones en secuencia. Si la primera condición del `if` es falsa, puedes usar `elif` para comprobar otra condición. Puedes tener tantos `elif` como necesites.

**Sintaxis:**

```python
if condicion1:
    # Bloque si condicion1 es True
    print("Se cumple la condición 1.")
elif condicion2:
    # Bloque si condicion1 es False Y condicion2 es True
    print("Se cumple la condición 2.")
elif condicion3:
    # Bloque si condicion1 y condicion2 son False Y condicion3 es True
    print("Se cumple la condición 3.")
# ... puedes tener más elif ...
else:
    # Bloque si NINGUNA de las condiciones anteriores es True
    print("No se cumple ninguna condición anterior.")
print("Fin del bloque if-elif-else.")
```

*   Python evalúa las condiciones en orden (`if`, luego el primer `elif`, luego el segundo `elif`, etc.).
*   En cuanto encuentra una condición que es `True`, ejecuta su bloque de código asociado y **sale** de toda la estructura `if-elif-else`. No evalúa las condiciones restantes.
*   El `else` final es opcional y se ejecuta solo si ninguna de las condiciones anteriores (`if` y todos los `elif`) fue `True`.

**Ejemplo:**

```python
nota = 78

if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C") # Esta condición es True, se ejecuta este bloque y termina.
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# Otro ejemplo
dia = "Martes"

if dia == "Lunes":
    print("Inicio de semana laboral.")
elif dia == "Viernes":
    print("¡Casi fin de semana!")
elif dia == "Sábado" or dia == "Domingo":
    print("¡Fin de semana!")
else:
    print("Día normal entre semana.") # Se ejecuta para "Martes"
```

## Condiciones Anidadas

Puedes poner estructuras `if-elif-else` dentro de otras estructuras `if-elif-else`. Esto se llama anidamiento. ¡Cuidado con la sangría para mantener la claridad!

```python
edad = 25
tiene_licencia = True

if edad >= 18:
    print("Es mayor de edad.")
    if tiene_licencia:
        print("Puede conducir.") # Bloque anidado
    else:
        print("No puede conducir (necesita licencia).") # Bloque anidado
else:
    print("Es menor de edad, no puede conducir.")
```

Las estructuras condicionales son la base para que tus programas tomen decisiones lógicas y respondan de manera diferente a distintas situaciones o entradas de datos. ¡Son esenciales en casi cualquier programa!
# Módulo 1: Control de Flujo - Bucles (`for`, `while`, `break`, `continue`)

Los bucles son estructuras de control que nos permiten ejecutar un bloque de código múltiples veces. Son fundamentales para procesar colecciones de datos o realizar tareas repetitivas sin tener que escribir el mismo código una y otra vez.

Python tiene dos tipos principales de bucles: `for` y `while`.

## Bucle `for`

El bucle `for` se utiliza para **iterar sobre una secuencia** (como una lista, tupla, diccionario, conjunto o cadena de texto) u otros objetos iterables. Ejecuta el bloque de código una vez por cada elemento en la secuencia.

**Sintaxis:**

```python
for variable_temporal in secuencia_o_iterable:
    # Bloque de código a ejecutar para cada elemento
    # La variable_temporal tomará el valor de cada elemento en cada iteración
    print(variable_temporal)
print("Fin del bucle for.")
```

*   `variable_temporal`: Es una variable que creas en el momento. En cada pasada (iteración) del bucle, tomará el valor del siguiente elemento de la `secuencia_o_iterable`. Puedes nombrarla como quieras (ej. `elemento`, `numero`, `fruta`, `letra`).
*   `secuencia_o_iterable`: Es la colección sobre la que quieres iterar.
*   El bloque de código indentado se ejecuta para cada elemento.

**Ejemplos:**

```python
# Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
print("Iterando sobre lista de frutas:")
for fruta in frutas:
    print(f"- {fruta}")

# Iterar sobre una cadena de texto (string)
mensaje = "Hola"
print("\nIterando sobre un string:")
for letra in mensaje:
    print(letra)

# Iterar sobre una secuencia de números usando range()
# range(n): genera números desde 0 hasta n-1
# range(inicio, fin): genera números desde inicio hasta fin-1
# range(inicio, fin, paso): genera números desde inicio hasta fin-1, con un incremento de 'paso'
print("\nIterando con range(5):")
for i in range(5): # Genera 0, 1, 2, 3, 4
    print(i)

print("\nIterando con range(2, 7):")
for num in range(2, 7): # Genera 2, 3, 4, 5, 6
    print(num)

print("\nIterando con range(0, 10, 2):")
for par in range(0, 10, 2): # Genera 0, 2, 4, 6, 8
    print(par)

# Iterar sobre las claves de un diccionario
estudiante = {"nombre": "Ana", "edad": 21, "curso": "Biología"}
print("\nIterando sobre claves de diccionario:")
for clave in estudiante: # Por defecto itera sobre las claves
    print(f"Clave: {clave}, Valor: {estudiante[clave]}")

# Iterar sobre los valores de un diccionario
print("\nIterando sobre valores de diccionario:")
for valor in estudiante.values():
    print(valor)

# Iterar sobre los pares clave-valor de un diccionario
print("\nIterando sobre items (clave-valor) de diccionario:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
```

## Bucle `while`

El bucle `while` ejecuta un bloque de código **mientras** una condición especificada sea `True`.

**Sintaxis:**

```python
while condicion:
    # Bloque de código a ejecutar mientras la condicion sea True
    # ¡Importante! Dentro del bucle, algo debe eventualmente
    # hacer que la condicion se vuelva False, o tendrás un bucle infinito.
    print("La condición sigue siendo verdadera.")
    # ...hacer algo que afecte la condición...
print("Fin del bucle while (la condición se volvió falsa).")
```

*   `condicion`: Expresión booleana. El bucle se ejecuta repetidamente mientras esta condición sea `True`.
*   El bloque indentado se ejecuta en cada iteración.
*   **¡Peligro de Bucle Infinito!** Si la condición nunca se vuelve `False`, el bucle se ejecutará para siempre (o hasta que interrumpas el programa manualmente). Asegúrate de que algo dentro del bucle modifique las variables involucradas en la condición.

**Ejemplos:**

```python
# Contar hasta 5
contador = 0
print("Bucle while contando hasta 4:")
while contador < 5:
    print(f"Contador es: {contador}")
    contador += 1 # ¡Fundamental! Modificamos la variable de la condición
print("Fin del conteo.")

# Esperar una entrada específica del usuario
entrada = ""
print("\nBucle while esperando 'salir':")
while entrada.lower() != "salir":
    entrada = input("Escribe 'salir' para terminar: ")
    print(f"Escribiste: {entrada}")
print("¡Saliste del bucle!")
```

## `break` y `continue`

Estas dos declaraciones permiten controlar el flujo dentro de los bucles:

1.  **`break`:**
    *   Termina **inmediatamente** el bucle actual (tanto `for` como `while`), incluso si la condición del `while` sigue siendo `True` o si quedan elementos por iterar en el `for`.
    *   La ejecución continúa en la primera línea *después* del bucle.

2.  **`continue`:**
    *   Salta **el resto de la iteración actual** del bucle.
    *   La ejecución pasa directamente al **inicio de la siguiente iteración**.
    *   En un `while`, se vuelve a evaluar la condición.
    *   En un `for`, se pasa al siguiente elemento de la secuencia.

**Ejemplos:**

```python
# Ejemplo con break: encontrar el primer número divisible por 7
numeros = [12, 15, 21, 25, 30, 35, 40]
print("\nBuscando el primer divisible por 7 (con break):")
numero_encontrado = None
for num in numeros:
    print(f"Probando {num}...")
    if num % 7 == 0:
        numero_encontrado = num
        print(f"¡Encontrado! {num} es divisible por 7.")
        break # Salimos del bucle for inmediatamente
print(f"El primer número divisible por 7 es: {numero_encontrado}")

# Ejemplo con continue: imprimir solo números impares
print("\nImprimiendo solo impares (con continue):")
for i in range(10): # Números del 0 al 9
    if i % 2 == 0: # Si es par...
        continue   # ...saltamos al siguiente número, no ejecutamos el print
    print(f"Impar: {i}")

# Ejemplo while con break
print("\nBucle while con break:")
contador_infinito = 0
while True: # Bucle potencialmente infinito
    print(f"Iteración {contador_infinito}")
    contador_infinito += 1
    if contador_infinito >= 5:
        print("Alcanzado el límite, saliendo con break.")
        break
```

Los bucles `for` y `while`, junto con `break` y `continue`, te dan un control muy preciso sobre cómo y cuántas veces se repite una porción de tu código. Son herramientas esenciales para la automatización y el procesamiento de datos.
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
# Módulo 1: Manejo de Errores Básicos (`try`, `except`)

Cuando ejecutas tu código Python, a veces ocurren errores. Estos pueden ser:

*   **Errores de Sintaxis (`SyntaxError`):** Ocurren cuando escribes código que no sigue las reglas gramaticales de Python (ej. falta de dos puntos, sangría incorrecta, palabra clave mal escrita). Estos errores impiden que el programa se ejecute siquiera. Debes corregirlos antes de poder ejecutar.
*   **Excepciones (Errores en Tiempo de Ejecución):** Ocurren *mientras* el programa se está ejecutando porque sucede algo inesperado (ej. intentar dividir por cero, intentar acceder a un índice de lista que no existe, intentar abrir un archivo que no se encuentra, intentar convertir a número un texto que no es numérico). Si no se manejan, las excepciones detienen abruptamente la ejecución del programa y muestran un mensaje de error (traceback).

El **manejo de excepciones** nos permite "atrapar" estos errores en tiempo de ejecución y ejecutar un código alternativo para manejar la situación, evitando que el programa se detenga por completo.

## La Estructura `try...except`

La forma básica de manejar excepciones en Python es usando un bloque `try...except`.

**Sintaxis:**

```python
try:
    # Bloque de código donde PUEDE ocurrir una excepción
    # Se intenta ejecutar este código normalmente.
    print("Intentando ejecutar código propenso a errores...")
    resultado = 10 / 0 # Esto causará una ZeroDivisionError
    print("Esta línea no se ejecutará si ocurre un error antes.")

except NombreDelErrorEspecifico:
    # Bloque de código que se ejecuta SI Y SOLO SI
    # ocurre la excepción 'NombreDelErrorEspecifico' en el bloque 'try'.
    print("¡Oops! Ocurrió un error específico.")

except OtroErrorEspecifico:
    # Puedes tener múltiples bloques 'except' para diferentes tipos de error.
    print("¡Oops! Ocurrió otro tipo de error.")

except:
    # Un 'except' sin especificar el tipo de error atrapará CUALQUIER excepción.
    # (Generalmente no es la mejor práctica ser tan genérico, es mejor
    # capturar errores específicos que esperas).
    print("¡Oops! Ocurrió algún error inesperado.")

print("El programa continúa después del try-except.")
```

**Flujo de Ejecución:**

1.  Python ejecuta el código dentro del bloque `try`.
2.  **Si no ocurre ninguna excepción** en el bloque `try`, el bloque (o bloques) `except` se omiten por completo, y la ejecución continúa después de toda la estructura `try...except`.
3.  **Si ocurre una excepción** en el bloque `try`:
    *   Python detiene inmediatamente la ejecución del resto del código dentro del `try`.
    *   Busca un bloque `except` que coincida con el tipo de excepción ocurrida.
    *   Si encuentra un `except` que coincide, ejecuta el código dentro de ese bloque `except`. Después de ejecutar el bloque `except`, la ejecución continúa *después* de la estructura `try...except` (el programa no se detiene).
    *   Si no encuentra ningún `except` que coincida (y no hay un `except:` genérico), la excepción no se maneja, y el programa se detiene mostrando el error (traceback), como si no hubiéramos usado `try...except`.

**Ejemplos:**

```python
# Ejemplo 1: División por cero (ZeroDivisionError)
try:
    numerador = 10
    denominador = int(input("Introduce el denominador (intenta 0): "))
    division = numerador / denominador
    print(f"El resultado es: {division}")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
except ValueError:
    print("Error: Debes introducir un número entero.")

print("--- Fin del Ejemplo 1 ---")

# Ejemplo 2: Acceso a índice inválido (IndexError)
mi_lista = [10, 20, 30]
try:
    indice = int(input(f"Introduce un índice (0 a {len(mi_lista)-1}): "))
    print(f"El elemento en el índice {indice} es: {mi_lista[indice]}")
except IndexError:
    print(f"Error: El índice {indice} está fuera de rango.")
except ValueError:
    print("Error: Debes introducir un número entero como índice.")

print("--- Fin del Ejemplo 2 ---")
```

## Capturando la Información del Error

Puedes capturar el objeto de la excepción para obtener más detalles sobre el error usando `as nombre_variable` en el `except`.

```python
try:
    x = int("hola") # Esto causará un ValueError
except ValueError as e: # Capturamos la excepción en la variable 'e'
    print(f"Ocurrió un error de valor: {e}")
    print(f"Tipo de error: {type(e)}")
```
**Salida:**
```
Ocurrió un error de valor: invalid literal for int() with base 10: 'hola'
Tipo de error: <class 'ValueError'>
```

## Bloques `else` y `finally` (Opcionales)

La estructura `try...except` puede extenderse con bloques `else` y `finally`:

*   **`else`:** El bloque `else` se ejecuta **solo si no ocurrió ninguna excepción** en el bloque `try`. Es útil para poner código que debe ejecutarse solo si el `try` fue exitoso.
*   **`finally`:** El bloque `finally` se ejecuta **siempre**, haya ocurrido una excepción o no, e incluso si se usó `return`, `break` o `continue` dentro del `try` o `except`. Se usa típicamente para tareas de "limpieza" que deben realizarse sí o sí (como cerrar un archivo o una conexión de red).

**Sintaxis Completa:**

```python
try:
    # Código propenso a errores
    print("Intentando...")
    # ...
except MiErrorEspecifico as e:
    # Manejar MiErrorEspecifico
    print(f"Manejando error: {e}")
    # ...
else:
    # Código a ejecutar si NO hubo excepciones en el try
    print("El bloque try se completó sin errores.")
    # ...
finally:
    # Código que se ejecuta SIEMPRE (limpieza)
    print("Este bloque finally siempre se ejecuta.")
    # ...
```

**Ejemplo con `else` y `finally`:**

```python
archivo = None # Inicializamos la variable fuera del try
try:
    nombre_archivo = "mi_archivo_inexistente.txt"
    print(f"Intentando abrir '{nombre_archivo}'...")
    archivo = open(nombre_archivo, "r") # Esto dará FileNotFoundError
    contenido = archivo.read()
    print("Archivo leído exitosamente.")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
except Exception as e: # Captura otros posibles errores
    print(f"Ocurrió un error inesperado: {e}")
else:
    # Esto solo se ejecutaría si el archivo se abre y lee sin problemas
    print("Contenido del archivo:")
    print(contenido)
finally:
    # Esto se ejecuta siempre, para asegurarnos de cerrar el archivo si se abrió
    if archivo: # Verificamos si el archivo se llegó a abrir
        print("Cerrando el archivo (en finally).")
        archivo.close()
    else:
        print("El archivo no se abrió (en finally).")

print("--- Fin del programa ---")
```

El manejo básico de errores con `try` y `except` es crucial para escribir programas robustos que puedan recuperarse de situaciones inesperadas sin detenerse por completo.
# Módulo 1: Buenas Prácticas Iniciales y PEP 8

¡Felicidades por llegar hasta aquí! Ya conoces los bloques de construcción fundamentales de Python. Ahora, hablemos de cómo escribir código no solo funcional, sino también **limpio, legible y mantenible**. Esto es crucial para tu propio entendimiento futuro y para colaborar con otros.

La comunidad Python valora mucho la legibilidad del código. Existe una guía de estilo oficial llamada **PEP 8** (Python Enhancement Proposal 8) que describe las convenciones recomendadas para escribir código Python. Seguir PEP 8 hace que el código sea más consistente y fácil de leer para cualquier programador Python.

Puedes encontrar la guía completa aquí: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

No necesitas memorizarla toda de golpe, pero es importante conocer y aplicar los puntos clave desde el principio. Herramientas como los linters (que veremos más adelante) pueden ayudarte a verificar si tu código cumple con PEP 8.

## Puntos Clave de PEP 8 para Empezar:

1.  **Sangría (Indentation):**
    *   Usa **4 espacios** por nivel de sangría. ¡No uses tabulaciones ni mezcles tabulaciones y espacios! Configura tu editor para que inserte espacios al presionar Tab. Ya vimos lo crucial que es la sangría para la estructura del código.

2.  **Longitud Máxima de Línea:**
    *   Limita todas las líneas a un máximo de **79 caracteres**.
    *   Para líneas largas, puedes dividirlas usando paréntesis `()`, corchetes `[]`, llaves `{}` o la barra invertida `\` (esta última con menos frecuencia). La sangría de continuación ayuda a la legibilidad.
    ```python
    # Ejemplo de línea larga dividida
    def funcion_con_muchos_parametros(param1, param2, param3, param4,
                                      param5, param6):
        print("Llamada con muchos parámetros")

    resultado_largo = (variable1 + variable2 + variable3
                       - variable4 * variable5)
    ```

3.  **Líneas en Blanco:**
    *   Usa líneas en blanco para separar bloques lógicos de código y mejorar la legibilidad.
    *   Separa las definiciones de funciones y clases de nivel superior con **dos** líneas en blanco.
    *   Separa las definiciones de métodos dentro de una clase con **una** línea en blanco.
    *   Usa líneas en blanco con moderación dentro de las funciones para separar pasos lógicos.

4.  **Importaciones (`import`):**
    *   Las importaciones deben ir siempre al **principio del archivo**, justo después de los comentarios del módulo y docstrings, y antes de las variables globales y definiciones.
    *   Importa **un módulo por línea**.
        ```python
        # Correcto:
        import os
        import sys

        # Incorrecto:
        # import os, sys
        ```
    *   Agrupa las importaciones en este orden, separadas por una línea en blanco:
        1.  Importaciones de la biblioteca estándar (ej. `os`, `sys`, `math`).
        2.  Importaciones de terceros relacionados (ej. `numpy`, `pandas`, `flask`).
        3.  Importaciones de tu propia aplicación/biblioteca local.

5.  **Espacios en Blanco en Expresiones y Declaraciones:**
    *   **Evita espacios innecesarios:** justo dentro de paréntesis/corchetes/llaves, antes de una coma.
    *   **Usa espacios alrededor de operadores:** asignación (`=`), comparación (`==`, `!=`, `>`, `<`), aritméticos (`+`, `-`, `*`, `/`), lógicos (`and`, `or`), etc. (Excepto alrededor de `**`).
        ```python
        # Correcto:
        x = 5
        y = x + 2
        if x > y and x != 0:
            mi_lista[1] = z * 3

        # Incorrecto:
        # x=5
        # y = x+2
        # if x>y and x!=0 :
        #     mi_lista [ 1 ] = z*3
        ```
    *   Usa un espacio después de la coma (`,`) en listas, tuplas, diccionarios, argumentos de funciones.

6.  **Nombres (Naming Conventions):** (Ya lo mencionamos, pero reforzamos)
    *   `snake_case`: Para variables, funciones y métodos (minúsculas con guion bajo). Ej: `mi_variable`, `calcular_total()`.
    *   `CapWords` o `PascalCase`: Para clases. Ej: `MiClase`, `CalculadoraDeImpuestos`.
    *   `UPPERCASE_SNAKE_CASE`: Para constantes. Ej: `PI = 3.14159`, `TASA_MAXIMA`.
    *   Nombres descriptivos y evitar abreviaturas ambiguas.

7.  **Comentarios:**
    *   Escribe comentarios claros y concisos que expliquen el *por qué* o el *cómo* de un código complejo, no el *qué* (si el código es legible, el qué debería ser obvio).
    *   Mantén los comentarios actualizados si cambias el código.
    *   Usa comentarios de bloque (`#`) para explicar secciones y comentarios en línea (`#`) con moderación para aclarar líneas específicas.
    *   Usa **Docstrings** (`"""Docstring"""`) para documentar funciones, clases y módulos (explicar su propósito, parámetros, etc.).

**¿Por qué seguir estas prácticas?**

*   **Legibilidad:** Otros (¡y tu yo futuro!) podrán entender tu código más fácilmente.
*   **Mantenibilidad:** Es más fácil encontrar errores y modificar código bien formateado.
*   **Colaboración:** Permite que los equipos trabajen juntos de manera más eficiente usando un estilo consistente.
*   **Profesionalismo:** Demuestra atención al detalle y buenas prácticas de ingeniería de software.

**Conclusión del Módulo 1:**

Has aprendido los fundamentos esenciales de Python: sintaxis, variables, tipos de datos, operadores, estructuras de datos básicas, control de flujo (condicionales y bucles), funciones, manejo básico de errores y la importancia de escribir código limpio siguiendo PEP 8.

¡Estás listo/a para pasar al siguiente nivel en el Módulo 2, donde exploraremos conceptos más intermedios como la Programación Orientada a Objetos!
