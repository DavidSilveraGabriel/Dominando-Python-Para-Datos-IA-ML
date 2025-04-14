# Módulo 2: Programación Orientada a Objetos (Clases y Objetos)

Hasta ahora, hemos trabajado principalmente con funciones y datos de forma separada (programación procedural). La **Programación Orientada a Objetos (POO)** es un paradigma diferente que nos permite estructurar nuestro código de una manera que a menudo se asemeja más al mundo real, modelando entidades como "objetos".

**Conceptos Clave de POO:**

*   **Clase (`class`):** Es como un **plano** o una **plantilla** para crear objetos. Define las propiedades (atributos) y comportamientos (métodos) que tendrán todos los objetos creados a partir de ella.
*   **Objeto (`object`):** Es una **instancia** específica de una clase. Es la entidad concreta creada a partir del plano (la clase). Puedes tener muchos objetos (instancias) de la misma clase, cada uno con sus propios valores para los atributos.
*   **Atributo (`attribute`):** Son las **variables** asociadas a una clase o a un objeto. Representan las características o el estado del objeto (ej. el `nombre`, `edad`, `color` de un objeto `Perro`).
*   **Método (`method`):** Son las **funciones** asociadas a una clase. Definen los comportamientos o acciones que un objeto puede realizar (ej. un objeto `Perro` podría tener métodos como `ladrar()`, `comer()`, `sentarse()`).

## Definiendo una Clase (`class`)

Usamos la palabra clave `class` para definir una nueva clase. Por convención (PEP 8), los nombres de las clases usan `CapWords` o `PascalCase`.

**Sintaxis Básica:**

```python
class NombreDeLaClase:
    """Docstring opcional que describe la clase."""

    # Atributo de clase (compartido por todas las instancias) - Opcional
    atributo_de_clase = "Valor compartido"

    # Método constructor (__init__) - Se ejecuta al crear un objeto
    def __init__(self, parametro1, parametro2, ...):
        """Inicializa los atributos del objeto."""
        # Atributos de instancia (propios de cada objeto)
        self.parametro1 = parametro1 # 'self.nombre_atributo = valor'
        self.parametro2 = parametro2
        self.nuevo_atributo = "Valor inicial" # Puedes definir otros atributos aquí

    # Otros métodos (comportamientos del objeto)
    def nombre_del_metodo(self, arg1, arg2, ...):
        """Describe lo que hace el método."""
        # El código del método usa 'self' para acceder a los atributos
        # y otros métodos del objeto.
        print(f"Ejecutando método con {self.parametro1} y {arg1}")
        # ... hacer algo ...
        return # Opcional
```

**Componentes Importantes:**

*   **`class NombreDeLaClase:`**: Define la clase.
*   **`__init__(self, ...)` (El Constructor):**
    *   Es un método **especial** (llamado "dunder method" por los dobles guiones bajos) que se ejecuta **automáticamente** cada vez que creas un nuevo objeto (instancia) de la clase.
    *   Su propósito principal es **inicializar** los atributos del objeto.
    *   El primer parámetro de `__init__` (y de cualquier método de instancia) **siempre** debe ser `self`.
*   **`self`:**
    *   Es una **referencia al propio objeto** (a la instancia que se está creando o sobre la que se está llamando el método).
    *   Se usa *dentro* de la clase para acceder a los atributos y métodos de esa instancia específica. Ej: `self.nombre`, `self.mi_metodo()`.
    *   **No** necesitas pasar `self` explícitamente cuando llamas a un método desde fuera del objeto; Python lo hace automáticamente.
*   **Atributos de Instancia:** Son los atributos definidos dentro de `__init__` usando `self.nombre_atributo = valor`. Cada objeto de la clase tendrá su propia copia de estos atributos con sus propios valores.
*   **Métodos de Instancia:** Son las funciones definidas dentro de la clase que toman `self` como primer parámetro. Operan sobre los datos (atributos) del objeto específico.

## Creando Objetos (Instanciación)

Para crear un objeto (una instancia) de una clase, llamas a la clase como si fuera una función, pasando los argumentos requeridos por el método `__init__` (sin incluir `self`).

```python
# Definición de la clase Perro
class Perro:
    """Representa un perro."""
    # Atributo de clase
    especie = "Canis lupus familiaris"

    def __init__(self, nombre, raza, edad):
        """Inicializa un nuevo perro."""
        self.nombre = nombre # Atributo de instancia
        self.raza = raza     # Atributo de instancia
        self.edad = edad     # Atributo de instancia
        self.esta_durmiendo = False # Otro atributo con valor inicial

    def ladrar(self):
        """El perro ladra."""
        if not self.esta_durmiendo:
            print(f"{self.nombre} dice: ¡Guau! ¡Guau!")
        else:
            print(f"{self.nombre} está durmiendo... Zzz...")

    def dormir(self):
        """Pone al perro a dormir."""
        self.esta_durmiendo = True
        print(f"{self.nombre} se fue a dormir.")

    def despertar(self):
        """Despierta al perro."""
        self.esta_durmiendo = False
        print(f"{self.nombre} se despertó.")

    def cumplir_anios(self):
        """Incrementa la edad del perro."""
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.edad}, {self.nombre}!")

# --- Creación de Objetos (Instancias) ---

# Creamos el primer objeto Perro
mi_perro = Perro(nombre="Fido", raza="Labrador", edad=3)

# Creamos otro objeto Perro
otro_perro = Perro(nombre="Luna", raza="Chihuahua", edad=5)

# --- Accediendo a Atributos ---
# Usamos la notación de punto: objeto.atributo
print(f"{mi_perro.nombre} es un {mi_perro.raza} de {mi_perro.edad} años.")
# Salida: Fido es un Labrador de 3 años.
print(f"{otro_perro.nombre} tiene {otro_perro.edad} años.")
# Salida: Luna tiene 5 años.

# Accediendo al atributo de clase (se puede acceder desde la clase o la instancia)
print(f"Especie (desde clase): {Perro.especie}")
# Salida: Especie (desde clase): Canis lupus familiaris
print(f"Especie (desde objeto): {mi_perro.especie}")
# Salida: Especie (desde objeto): Canis lupus familiaris

# Modificando un atributo de instancia
mi_perro.edad = 4
print(f"La edad de {mi_perro.nombre} ahora es {mi_perro.edad}.")
# Salida: La edad de Fido ahora es 4.

# --- Llamando a Métodos ---
# Usamos la notación de punto: objeto.metodo(argumentos)
mi_perro.ladrar()    # Salida: Fido dice: ¡Guau! ¡Guau!
otro_perro.ladrar()  # Salida: Luna dice: ¡Guau! ¡Guau!

mi_perro.dormir()    # Salida: Fido se fue a dormir.
mi_perro.ladrar()    # Salida: Fido está durmiendo... Zzz...
mi_perro.despertar() # Salida: Fido se despertó.

otro_perro.cumplir_anios() # Salida: ¡Feliz cumpleaños 6, Luna!
print(f"La nueva edad de {otro_perro.nombre} es {otro_perro.edad}.") # Salida: La nueva edad de Luna es 6.
```

Las clases y objetos son la base de la POO. Permiten encapsular datos (atributos) y comportamientos (métodos) relacionados en unidades lógicas, lo que conduce a un código más organizado, reutilizable y fácil de escalar. En las siguientes secciones exploraremos otros pilares de la POO como la herencia y el encapsulamiento.
