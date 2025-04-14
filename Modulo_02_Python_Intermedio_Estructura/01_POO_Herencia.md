# Módulo 2: Programación Orientada a Objetos - Herencia

La **Herencia** es uno de los conceptos centrales de la POO. Permite crear una nueva clase (llamada **clase hija**, **subclase** o **clase derivada**) que hereda las propiedades (atributos) y comportamientos (métodos) de una clase existente (llamada **clase padre**, **superclase** o **clase base**).

**¿Por qué usar Herencia?**

*   **Reutilización de Código:** Evita tener que reescribir el mismo código en múltiples clases. La clase hija obtiene automáticamente la funcionalidad de la clase padre.
*   **Establecer Relaciones "Es un/a":** Modela relaciones jerárquicas del mundo real. Por ejemplo, un `Perro` *es un* `Animal`, un `Gato` *es un* `Animal`. Un `Coche` *es un* `Vehiculo`.
*   **Extensibilidad:** Puedes añadir nueva funcionalidad específica en la clase hija sin modificar la clase padre.
*   **Polimorfismo (lo veremos más adelante):** La herencia es fundamental para el polimorfismo, que permite tratar objetos de diferentes clases hijas de manera uniforme a través de la interfaz de la clase padre.

## Sintaxis de la Herencia

Para indicar que una clase hereda de otra, se especifica el nombre de la clase padre entre paréntesis después del nombre de la clase hija en la definición.

```python
class ClasePadre:
    """Clase base de la que se hereda."""
    def __init__(self, atributo_padre):
        print("Inicializador de ClasePadre")
        self.atributo_padre = atributo_padre

    def metodo_padre(self):
        print("Ejecutando método de ClasePadre")

# ClaseHija hereda de ClasePadre
class ClaseHija(ClasePadre):
    """Clase que hereda de ClasePadre."""
    def __init__(self, atributo_padre, atributo_hija):
        print("Inicializador de ClaseHija")
        # --- Llamando al constructor del padre ---
        # Forma 1: Usando super() (Recomendado en Python 3+)
        super().__init__(atributo_padre)
        # Forma 2: Llamando explícitamente al __init__ del padre
        # ClasePadre.__init__(self, atributo_padre) # Menos común hoy en día

        # Atributo propio de la clase hija
        self.atributo_hija = atributo_hija

    def metodo_hija(self):
        print("Ejecutando método de ClaseHija")

    # --- Sobrescribiendo un método del padre ---
    def metodo_padre(self):
        print("Ejecutando método_padre SOBRESCRITO en ClaseHija")
        # Opcionalmente, puedes llamar a la versión original del padre si la necesitas
        # super().metodo_padre()
```

**Puntos Clave:**

*   `class ClaseHija(ClasePadre):`: Así se declara la herencia.
*   **Acceso a Miembros Heredados:** Un objeto de `ClaseHija` tiene acceso a `atributo_padre` y puede llamar a `metodo_padre()` (a menos que se sobrescriba).
*   **Llamar al Constructor del Padre (`super().__init__(...)`):**
    *   Es **muy importante** que si la clase hija define su propio `__init__`, llame explícitamente al `__init__` de la clase padre usando `super().__init__(...)`.
    *   Esto asegura que la inicialización definida en la clase padre también se realice para el objeto hijo. `super()` devuelve un objeto temporal de la superclase que permite llamar a sus métodos.
*   **Sobrescritura de Métodos (Method Overriding):**
    *   Si una clase hija define un método con el **mismo nombre** que un método de la clase padre, la versión de la hija **sobrescribe** (reemplaza) a la del padre para los objetos de la clase hija.
    *   Dentro del método sobrescrito, aún puedes llamar a la versión original del padre usando `super().nombre_metodo_padre()`.

## Ejemplo Práctico: Animales

```python
class Animal:
    """Clase base para todos los animales."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Animal '{self.nombre}' creado.")

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido genérico.")

# Perro hereda de Animal
class Perro(Animal):
    """Representa un perro, que es un tipo de Animal."""
    def __init__(self, nombre, edad, raza):
        # Llamamos al __init__ de Animal para inicializar nombre y edad
        super().__init__(nombre, edad)
        self.raza = raza # Atributo específico de Perro
        print(f"Perro de raza '{self.raza}' creado.")

    # Método específico de Perro
    def perseguir_cola(self):
        print(f"{self.nombre} está persiguiendo su cola.")

    # Sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Gato hereda de Animal
class Gato(Animal):
    """Representa un gato, que es un tipo de Animal."""
    def __init__(self, nombre, edad, color_pelaje):
        super().__init__(nombre, edad)
        self.color_pelaje = color_pelaje
        print(f"Gato de color '{self.color_pelaje}' creado.")

    # Método específico de Gato
    def amasar(self):
        print(f"{self.nombre} está amasando con sus patitas.")

    # Sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# --- Creando instancias ---
mi_perro = Perro("Bobby", 4, "Golden Retriever")
mi_gato = Gato("Mishi", 2, "Naranja")
animal_generico = Animal("Criatura", 1)

print("\n--- Comportamientos ---")

# Métodos heredados de Animal
mi_perro.comer()
mi_gato.dormir()
animal_generico.comer()

# Métodos específicos de cada subclase
mi_perro.perseguir_cola()
mi_gato.amasar()
# animal_generico.amasar() # Esto daría un error, Animal no tiene ese método

# Métodos sobrescritos
mi_perro.hacer_sonido()
mi_gato.hacer_sonido()
animal_generico.hacer_sonido()
```

**Salida del Ejemplo:**

```
Animal 'Bobby' creado.
Perro de raza 'Golden Retriever' creado.
Animal 'Mishi' creado.
Gato de color 'Naranja' creado.
Animal 'Criatura' creado.

--- Comportamientos ---
Bobby está comiendo.
Mishi está durmiendo.
Criatura está comiendo.
Bobby está persiguiendo su cola.
Mishi está amasando con sus patitas.
Bobby dice: ¡Guau!
Mishi dice: ¡Miau!
Criatura hace un sonido genérico.
```

La herencia es una herramienta poderosa para modelar relaciones y reutilizar código. Permite construir jerarquías de clases complejas de manera organizada. El siguiente concepto importante es el encapsulamiento, que se refiere a cómo protegemos los datos internos de un objeto.
