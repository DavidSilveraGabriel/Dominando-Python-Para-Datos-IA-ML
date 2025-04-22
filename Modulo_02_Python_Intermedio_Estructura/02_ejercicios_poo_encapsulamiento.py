# Ejercicios: Módulo 2 - POO - Encapsulamiento

# --- Ejercicio 1: Atributos "Protegidos" (Convención) ---
# Instrucciones:
# 1. Define una clase `Empleado`.
# 2. En el `__init__`, acepta `nombre` (público) y `salario` (privado por convención).
#    Guarda `nombre` como `self.nombre` y `salario` como `self._salario`.
# 3. Crea un método público `obtener_salario` que devuelva el valor de `self._salario`.
# 4. Crea un método público `establecer_salario` que acepte un `nuevo_salario`.
#    Dentro de este método, verifica si `nuevo_salario` es positivo. Si lo es, actualiza
#    `self._salario`; si no, imprime un mensaje de error.
# 5. Crea una instancia de `Empleado`.
# 6. Intenta acceder directamente a `_salario` desde fuera (imprímelo, pero añade un comentario
#    indicando que es mala práctica).
# 7. Usa `obtener_salario` para imprimir el salario.
# 8. Usa `establecer_salario` para cambiar el salario a un valor válido e imprime el nuevo salario usando `obtener_salario`.
# 9. Intenta usar `establecer_salario` con un valor negativo y observa el mensaje de error.

print("--- Ejercicio 1: Atributos 'Protegidos' ---")

class Empleado:
    """Representa un empleado con nombre y salario 'protegido'."""
    def __init__(self, nombre, salario):
        self.nombre = nombre # Público
        self._salario = max(0, salario) # "Protegido", aseguramos no negativo al inicio

    def obtener_salario(self):
        """Devuelve el salario 'protegido'."""
        return self._salario

    def establecer_salario(self, nuevo_salario):
        """Establece un nuevo salario si es válido."""
        if nuevo_salario >= 0:
            self._salario = nuevo_salario
            print(f"Salario de {self.nombre} actualizado a {self._salario}")
        else:
            print("Error: El salario no puede ser negativo.")

# Creación y uso
emp1 = Empleado("Ana López", 30000)
print(f"Empleado: {emp1.nombre}")

# Acceso directo (mala práctica)
# print(f"Acceso directo al salario (mala práctica): {emp1._salario}")

# Acceso mediante métodos
print(f"Salario obtenido con método: {emp1.obtener_salario()}")

emp1.establecer_salario(32000)
print(f"Nuevo salario obtenido: {emp1.obtener_salario()}")

emp1.establecer_salario(-500) # Intento inválido


# --- Ejercicio 2: Atributos "Privados" (Name Mangling) ---
# Instrucciones:
# 1. Define una clase `Circulo`.
# 2. En el `__init__`, acepta `radio`. Guarda el radio como un atributo "privado" `__radio`.
# 3. Crea un método público `calcular_area` que use `self.__radio` para calcular el área (pi * radio^2).
#    Puedes usar `import math` y `math.pi`.
# 4. Crea un método público `obtener_radio` que devuelva `self.__radio`.
# 5. Crea una instancia de `Circulo`.
# 6. Llama a `calcular_area` e imprime el resultado.
# 7. Intenta acceder directamente a `__radio` desde fuera (observa el `AttributeError`). Comenta la línea.
# 8. Accede al radio usando `obtener_radio`.
# 9. (Opcional) Intenta acceder al radio usando el nombre modificado (`_Circulo__radio`) y observa que funciona (pero es mala práctica).

print("\n--- Ejercicio 2: Atributos 'Privados' ---")
import math

class Circulo:
    """Representa un círculo con radio 'privado'."""
    def __init__(self, radio):
        if radio >= 0:
            self.__radio = radio # Atributo "privado"
        else:
            self.__radio = 0
            print("Advertencia: El radio no puede ser negativo, se estableció a 0.")

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * (self.__radio ** 2)

    def obtener_radio(self):
        """Devuelve el valor del radio 'privado'."""
        return self.__radio

# Creación y uso
c1 = Circulo(5)
print(f"Área del círculo con radio {c1.obtener_radio()}: {c1.calcular_area():.2f}")

# Intento de acceso directo (AttributeError)
# print(c1.__radio)

# Acceso mediante método público
print(f"Radio obtenido con método: {c1.obtener_radio()}")

# (Opcional) Acceso con nombre modificado (mala práctica)
# print(f"Acceso con nombre modificado (mala práctica): {c1._Circulo__radio}")

c2 = Circulo(-3) # Prueba con radio negativo
print(f"Radio del segundo círculo: {c2.obtener_radio()}")


# --- Ejercicio 3: Propiedades (`@property`) ---
# Instrucciones:
# 1. Define una clase `Libro`.
# 2. En el `__init__`, acepta `titulo` (público) y `numero_paginas` (privado por convención `_numero_paginas`).
#    Asegúrate de que `numero_paginas` no sea negativo al inicializar.
# 3. Usa el decorador `@property` para crear un getter para `numero_paginas`.
#    Este getter simplemente devolverá `self._numero_paginas`.
# 4. Usa el decorador `@numero_paginas.setter` para crear un setter para `numero_paginas`.
#    Este setter debe aceptar `nuevo_valor`. Dentro, verifica si `nuevo_valor` es positivo.
#    Si lo es, actualiza `self._numero_paginas`; si no, imprime un error.
# 5. Crea una instancia de `Libro`.
# 6. Accede al número de páginas usando la property (como si fuera un atributo público) e imprímelo.
# 7. Establece un nuevo número de páginas válido usando la property (asignación directa).
#    Imprime el nuevo valor accediendo de nuevo a la property.
# 8. Intenta establecer un número de páginas negativo usando la property y observa el error.

print("\n--- Ejercicio 3: Propiedades (`@property`) ---")

class Libro:
    """Representa un libro con título y número de páginas controlado por property."""
    def __init__(self, titulo, numero_paginas):
        self.titulo = titulo
        # Usamos el setter indirectamente en el init para validar
        self.numero_paginas = numero_paginas # Esto llamará al @numero_paginas.setter

    @property
    def numero_paginas(self):
        """Getter para el número de páginas."""
        # print("(Accediendo a _numero_paginas vía getter)") # Descomentar para depurar
        return self._numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, nuevo_valor):
        """Setter para el número de páginas con validación."""
        # print(f"(Intentando establecer _numero_paginas a {nuevo_valor} vía setter)") # Descomentar para depurar
        if isinstance(nuevo_valor, int) and nuevo_valor >= 0:
            self._numero_paginas = nuevo_valor
        else:
            print("Error: El número de páginas debe ser un entero no negativo.")

# Creación y uso
libro1 = Libro("El Hobbit", 310)
print(f"Libro: {libro1.titulo}")

# Acceso vía property (getter)
print(f"Número de páginas inicial: {libro1.numero_paginas}")

# Establecimiento vía property (setter)
libro1.numero_paginas = 320
print(f"Número de páginas actualizado: {libro1.numero_paginas}")

# Intento de establecimiento inválido
libro1.numero_paginas = -50
print(f"Número de páginas tras intento inválido: {libro1.numero_paginas}")

libro2 = Libro("Otro Libro", -100) # Prueba de validación en __init__
print(f"Páginas de libro2: {libro2.numero_paginas}")


# --- Fin de los ejercicios ---
