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
