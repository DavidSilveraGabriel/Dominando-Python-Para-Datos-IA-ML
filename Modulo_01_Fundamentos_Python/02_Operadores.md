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
