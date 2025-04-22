# Ejercicios: Módulo 2 - POO - Herencia

# --- Ejercicio 1: Clase Base y Clase Derivada Simple ---
# Instrucciones:
# 1. Define una clase base llamada `Vehiculo` con un método `__init__` que acepte `marca` y `modelo`.
#    Guarda estos como atributos de instancia.
# 2. Añade un método `mostrar_info` a `Vehiculo` que imprima la marca y el modelo.
# 3. Define una clase derivada llamada `Coche` que herede de `Vehiculo`.
# 4. En el `__init__` de `Coche`, acepta `marca`, `modelo` y `numero_puertas`.
#    Llama al `__init__` de la clase padre (`Vehiculo`) usando `super()` para inicializar `marca` y `modelo`.
#    Guarda `numero_puertas` como un atributo específico de `Coche`.
# 5. Crea una instancia de `Vehiculo` y llama a `mostrar_info`.
# 6. Crea una instancia de `Coche` y llama a `mostrar_info` (heredado de `Vehiculo`).
# 7. Accede e imprime el atributo `numero_puertas` del objeto `Coche`.

print("--- Ejercicio 1: Clase Base y Derivada Simple ---")

# Escribe tu código aquí
class Vehiculo:
    """Clase base para vehículos."""
    def __init__(self, marca, modelo):
        print(f"Inicializando Vehiculo ({marca} {modelo})")
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        """Muestra la marca y modelo del vehículo."""
        print(f"Vehículo: {self.marca} {self.modelo}")

class Coche(Vehiculo):
    """Clase derivada que representa un coche."""
    def __init__(self, marca, modelo, numero_puertas):
        print(f"Inicializando Coche ({marca} {modelo})")
        # Llamamos al constructor de la clase padre (Vehiculo)
        super().__init__(marca, modelo)
        # Atributo específico de Coche
        self.numero_puertas = numero_puertas

# Creación de instancias
vehiculo_generico = Vehiculo("Yamaha", "XTZ 125")
mi_coche = Coche("Ford", "Focus", 4)

# Llamadas a métodos y acceso a atributos
print("\nInformación:")
vehiculo_generico.mostrar_info()
mi_coche.mostrar_info() # Método heredado
print(f"El coche {mi_coche.marca} {mi_coche.modelo} tiene {mi_coche.numero_puertas} puertas.")


# --- Ejercicio 2: Sobrescritura de Métodos ---
# Instrucciones:
# 1. Añade un método `arrancar` a la clase `Vehiculo` que imprima "Arrancando el vehículo...".
# 2. Sobrescribe el método `arrancar` en la clase `Coche`. La nueva versión debe imprimir
#    "Arrancando el coche [marca] [modelo]... ¡Brum, brum!".
# 3. Añade un método `mostrar_info` específico a la clase `Coche` que sobrescriba al del padre.
#    Este nuevo método debe imprimir la marca, modelo y el número de puertas.
#    (Opcional: puedes llamar a `super().mostrar_info()` dentro de este método si quieres
#    reutilizar parte de la lógica del padre).
# 4. Crea una instancia de `Vehiculo` y llama a `arrancar` y `mostrar_info`.
# 5. Crea una instancia de `Coche` y llama a `arrancar` y `mostrar_info` (las versiones sobrescritas).

print("\n--- Ejercicio 2: Sobrescritura de Métodos ---")

# Reescribimos las clases con los nuevos métodos y sobrescrituras
class Vehiculo:
    """Clase base para vehículos."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        """Muestra la marca y modelo del vehículo."""
        print(f"Vehículo: {self.marca} {self.modelo}")

    def arrancar(self):
        """Método para arrancar el vehículo."""
        print("Arrancando el vehículo...")

class Coche(Vehiculo):
    """Clase derivada que representa un coche."""
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    # Sobrescribimos arrancar
    def arrancar(self):
        """Método sobrescrito para arrancar el coche."""
        print(f"Arrancando el coche {self.marca} {self.modelo}... ¡Brum, brum!")

    # Sobrescribimos mostrar_info
    def mostrar_info(self):
        """Muestra información específica del coche."""
        # Opcional: Llamar al método del padre primero
        # super().mostrar_info()
        print(f"Coche: {self.marca} {self.modelo}, Puertas: {self.numero_puertas}")

# Creación de instancias
vehiculo_generico = Vehiculo("Honda", "CB190R")
mi_coche = Coche("Renault", "Clio", 5)

# Llamadas a métodos
print("\nComportamiento Vehículo Genérico:")
vehiculo_generico.mostrar_info()
vehiculo_generico.arrancar()

print("\nComportamiento Coche Específico:")
mi_coche.mostrar_info() # Llama a la versión sobrescrita en Coche
mi_coche.arrancar()     # Llama a la versión sobrescrita en Coche


# --- Ejercicio 3: Jerarquía de Clases ---
# Instrucciones:
# 1. Define una clase `FiguraGeometrica` con un `__init__` que acepte `color` y un método
#    `describir` que imprima "Soy una figura geométrica de color [color]".
# 2. Define una clase `Rectangulo` que herede de `FiguraGeometrica`. Su `__init__` debe
#    aceptar `color`, `base` y `altura`. Llama al `__init__` del padre y guarda `base` y `altura`.
# 3. Añade un método `calcular_area` a `Rectangulo` que devuelva `base * altura`.
# 4. Sobrescribe el método `describir` en `Rectangulo` para que imprima
#    "Soy un rectángulo de color [color] con base [base] y altura [altura]".
# 5. Define una clase `Cuadrado` que herede de `Rectangulo`. Su `__init__` debe aceptar
#    `color` y `lado`. Llama al `__init__` del padre (`Rectangulo`) pasando `lado`
#    tanto para `base` como para `altura`.
# 6. Sobrescribe el método `describir` en `Cuadrado` para que imprima
#    "Soy un cuadrado de color [color] con lado [lado]".
# 7. Crea instancias de `Rectangulo` y `Cuadrado`.
# 8. Llama a `describir` y `calcular_area` (si aplica) para cada instancia.

print("\n--- Ejercicio 3: Jerarquía de Clases ---")

# Escribe tu código aquí
class FiguraGeometrica:
    """Clase base para figuras geométricas."""
    def __init__(self, color):
        self.color = color

    def describir(self):
        """Describe la figura genérica."""
        print(f"Soy una figura geométrica de color {self.color}")

class Rectangulo(FiguraGeometrica):
    """Representa un rectángulo."""
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    # Sobrescribe describir
    def describir(self):
        """Describe el rectángulo."""
        print(f"Soy un rectángulo de color {self.color} con base {self.base} y altura {self.altura}")

class Cuadrado(Rectangulo):
    """Representa un cuadrado, que es un tipo de Rectangulo."""
    def __init__(self, color, lado):
        # Llamamos al __init__ de Rectangulo pasando lado como base y altura
        super().__init__(color, lado, lado)
        # Guardamos lado también para la descripción específica
        self.lado = lado

    # Sobrescribe describir
    def describir(self):
        """Describe el cuadrado."""
        # Podríamos llamar a super().describir() pero la descripción es muy diferente
        print(f"Soy un cuadrado de color {self.color} con lado {self.lado}")
        # Nota: calcular_area() se hereda directamente de Rectangulo y funciona correctamente

# Creación de instancias
mi_rectangulo = Rectangulo("Azul", 10, 5)
mi_cuadrado = Cuadrado("Rojo", 7)

# Uso de los objetos
print("\nDescripción y Área del Rectángulo:")
mi_rectangulo.describir()
print(f"Área: {mi_rectangulo.calcular_area()}")

print("\nDescripción y Área del Cuadrado:")
mi_cuadrado.describir()
print(f"Área: {mi_cuadrado.calcular_area()}") # Método heredado de Rectangulo


# --- Fin de los ejercicios ---
