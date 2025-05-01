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
# Módulo 2: Programación Orientada a Objetos - Encapsulamiento

El **Encapsulamiento** es otro pilar fundamental de la POO. Se refiere a dos ideas relacionadas pero distintas:

1.  **Agrupación:** Bundling (agrupar) los datos (atributos) y los métodos (comportamientos) que operan sobre esos datos dentro de una única unidad lógica: la clase. Ya hemos estado haciendo esto al definir clases como `Perro` o `Animal`.
2.  **Ocultación de Información (Data Hiding):** Restringir el acceso directo al estado interno (atributos) de un objeto desde el exterior. El objetivo es proteger los datos de modificaciones accidentales o inválidas y permitir que la clase controle cómo se accede y se cambia su estado interno, generalmente a través de métodos públicos (getters/setters o propiedades).

**¿Por qué es importante el Encapsulamiento?**

*   **Protección de Datos:** Evita que el estado interno del objeto sea corrompido por acceso externo no controlado.
*   **Abstracción:** Oculta los detalles complejos de implementación interna. El usuario de la clase solo necesita saber *qué* hace el objeto (a través de su interfaz pública de métodos), no *cómo* lo hace internamente.
*   **Flexibilidad y Mantenimiento:** Permite cambiar la implementación interna de una clase (cómo se almacenan los datos o cómo funcionan los métodos) sin afectar el código externo que la utiliza, siempre que la interfaz pública (los métodos que se llaman desde fuera) se mantenga igual.
*   **Control:** La clase puede validar los datos antes de modificar sus atributos (ej. asegurarse de que una edad no sea negativa).

## Encapsulamiento en Python: Convenciones de Nomenclatura

Python no tiene palabras clave estrictas como `private` o `protected`. En su lugar, utiliza **convenciones de nomenclatura** basadas en guiones bajos (`_`) al principio de los nombres de atributos y métodos para indicar el nivel de acceso deseado:

1.  **Atributo/Método Público:**
    *   Sin guion bajo inicial (ej. `nombre`, `edad`, `ladrar()`).
    *   Son accesibles libremente desde fuera de la clase. Son parte de la interfaz pública de la clase.
    *   **Este es el comportamiento por defecto.**

2.  **Atributo/Método "Protegido" (Convención):**
    *   Un solo guion bajo inicial (ej. `_saldo`, `_calcular_impuesto()`).
    *   **Convención:** Indica que el atributo o método está destinado **solo para uso interno** dentro de la clase o sus subclases (herencia).
    *   **Técnicamente:** Python *no impide* el acceso desde fuera (`objeto._saldo`), pero se considera una **mala práctica** hacerlo. Es una señal para otros desarrolladores: "No toques esto directamente desde fuera a menos que sepas lo que haces".

3.  **Atributo/Método "Privado" (Name Mangling):**
    *   Doble guion bajo inicial (ej. `__clave_secreta`, `__metodo_muy_interno()`).
    *   **Name Mangling (Modificación de Nombre):** Python **modifica automáticamente** el nombre de estos atributos/métodos internamente para hacer más difícil el acceso accidental desde fuera o la sobrescritura accidental en subclases. Lo renombra a `_NombreClase__nombreAtributo`.
    *   **No es verdadera privacidad:** Aún se puede acceder si conoces el nombre modificado (`objeto._NombreClase__clave_secreta`), pero su propósito es evitar colisiones de nombres y accesos accidentales. Se usa con menos frecuencia que el guion bajo simple.

**Ejemplo:**

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular # Atributo público
        self._saldo = saldo_inicial # Atributo "protegido" por convención
        self.__tipo_cuenta = "Ahorro" # Atributo "privado" (name mangling)

    # Método público para depositar
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self._saldo}")
            self.__registrar_transaccion("deposito", cantidad) # Llama a método "privado"
        else:
            print("Error: La cantidad a depositar debe ser positiva.")

    # Método público para retirar
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self._saldo}")
            self.__registrar_transaccion("retiro", cantidad)
        elif cantidad > self._saldo:
            print("Error: Saldo insuficiente.")
        else:
            print("Error: La cantidad a retirar debe ser positiva.")

    # Método público para obtener saldo (Getter)
    def obtener_saldo(self):
        """Devuelve el saldo actual."""
        return self._saldo

    # Método "privado" para uso interno
    def __registrar_transaccion(self, tipo, monto):
        # En un caso real, esto escribiría en una base de datos o log
        print(f"-- Registrando transacción interna: {tipo} de {monto} --")

# --- Uso de la clase ---
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

# Acceso a atributo público (OK)
print(f"Titular: {mi_cuenta.titular}")

# Acceso a método público (OK)
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
saldo_actual = mi_cuenta.obtener_saldo()
print(f"Saldo obtenido con método: {saldo_actual}")

# Acceso a atributo "protegido" (Técnicamente posible, pero NO recomendado)
# print(f"Accediendo directamente al saldo: {mi_cuenta._saldo}") # ¡Mala práctica!

# Intento de acceso a atributo "privado" (NameError - nombre modificado)
# print(mi_cuenta.__tipo_cuenta) # Esto dará AttributeError

# Acceso al atributo "privado" usando el nombre modificado (Posible, pero MUY mala práctica)
# print(f"Accediendo al tipo de cuenta 'privado': {mi_cuenta._CuentaBancaria__tipo_cuenta}")

# Intento de llamada a método "privado" (AttributeError)
# mi_cuenta.__registrar_transaccion("intento", 10) # Esto dará AttributeError
```

## Getters, Setters y Propiedades (`@property`)

En lugar de acceder directamente a atributos (incluso los públicos o "protegidos"), a menudo es mejor usar métodos para obtener (`getters`) y establecer (`setters`) sus valores. Esto da más control a la clase.

Python ofrece una forma más elegante y "Pythonica" de hacer esto usando el decorador `@property`.

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre # Público
        self._precio = max(0, precio) # "Protegido", aseguramos que no sea negativo al inicio

    # --- Usando @property para controlar el acceso a _precio ---

    @property
    def precio(self):
        """Getter para el precio. Se accede como un atributo: producto.precio"""
        print("(Obteniendo precio a través de property)")
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        """Setter para el precio. Se usa como asignación: producto.precio = valor"""
        print("(Estableciendo precio a través de setter)")
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")

    @precio.deleter
    def precio(self):
        """Deleter para el precio (menos común). Se usa con: del producto.precio"""
        print("(Eliminando precio a través de deleter)")
        # Podrías ponerlo a None, 0, o lanzar un error si no se permite borrar
        del self._precio


# --- Uso ---
tv = Producto("Televisor HD", 500)

# Accediendo al precio (llama al getter @property)
precio_tv = tv.precio # No se usan paréntesis ()
print(f"Precio de la TV: {precio_tv}")

# Estableciendo el precio (llama al setter @precio.setter)
tv.precio = 550 # Asignación normal
print(f"Nuevo precio: {tv.precio}")

# Intentando establecer un precio inválido
tv.precio = -50
print(f"Precio después de intento inválido: {tv.precio}")

# Eliminando el atributo (llama al deleter @precio.deleter)
# del tv.precio
# print(tv.precio) # Daría AttributeError si se eliminó _precio
```

**Ventajas de `@property`:**

*   Permite acceder y modificar atributos como si fueran públicos (`objeto.atributo`), pero ejecutando código (getters/setters) por detrás.
*   Mantiene una interfaz limpia y simple para el usuario de la clase.
*   Permite añadir lógica de validación o cálculo al acceder o modificar un atributo.

El encapsulamiento, ya sea mediante convenciones de nomenclatura o propiedades, es clave para diseñar clases robustas, flexibles y fáciles de mantener en Python.
# Módulo 2: Módulos y Paquetes

A medida que tus programas se vuelven más complejos, no es práctico mantener todo el código en un solo archivo `.py`. Los **Módulos** y **Paquetes** son la forma en que Python organiza el código en unidades lógicas y reutilizables.

## Módulos

*   **¿Qué es?** Un módulo es simplemente un archivo de Python (`.py`) que contiene definiciones y declaraciones de Python (variables, funciones, clases).
*   **Propósito:** Permite agrupar código relacionado lógicamente y reutilizarlo en otros archivos o programas.
*   **Ejemplo:** La biblioteca estándar de Python está compuesta por muchos módulos (`math`, `os`, `sys`, `datetime`, `random`, etc.). También las librerías que instalamos (como `numpy` o `pandas`) son módulos o paquetes de módulos.

**Creando un Módulo Simple:**

1.  Crea un archivo llamado, por ejemplo, `mi_modulo.py`.
2.  Escribe algunas funciones o variables dentro de él:

    ```python
    # Contenido de mi_modulo.py
    print("Módulo 'mi_modulo' importado o ejecutado.")

    PI = 3.14159

    def saludar(nombre):
        """Saluda a la persona."""
        print(f"Hola, {nombre} desde mi_modulo!")

    def calcular_area_circulo(radio):
        """Calcula el área de un círculo."""
        return PI * (radio ** 2)

    class MiClaseModulo:
        def __init__(self, valor):
            self.valor = valor
        def mostrar(self):
            print(f"Valor en MiClaseModulo: {self.valor}")

    # Código que se ejecuta solo si el módulo se ejecuta directamente
    if __name__ == "__main__":
        print("Este código solo se ve si ejecutas mi_modulo.py directamente.")
        saludar("Mundo")
        area = calcular_area_circulo(10)
        print(f"Área de prueba: {area}")
    ```

**Importando un Módulo (`import`):**

Para usar las funciones, clases o variables definidas en otro módulo (`.py`), necesitas importarlo en tu archivo actual.

1.  Crea otro archivo, por ejemplo, `programa_principal.py`, **en el mismo directorio** que `mi_modulo.py`.
2.  Usa la declaración `import` seguida del nombre del archivo del módulo (sin la extensión `.py`).

    ```python
    # Contenido de programa_principal.py
    import mi_modulo # Importa todo el módulo

    print("--- Usando mi_modulo ---")

    # Para acceder a los miembros del módulo, usa la notación de punto:
    # nombre_modulo.nombre_miembro
    print(f"Valor de PI: {mi_modulo.PI}")

    mi_modulo.saludar("Alice")

    radio_circulo = 5
    area = mi_modulo.calcular_area_circulo(radio_circulo)
    print(f"El área de un círculo con radio {radio_circulo} es {area}")

    objeto_modulo = mi_modulo.MiClaseModulo(100)
    objeto_modulo.mostrar()
    ```

*   Cuando importas un módulo (`import mi_modulo`), Python ejecuta el código del archivo `mi_modulo.py` de arriba abajo la primera vez que se importa. Por eso vemos el mensaje "Módulo 'mi_modulo' importado o ejecutado." al correr `programa_principal.py`.
*   El código dentro del bloque `if __name__ == "__main__":` en `mi_modulo.py` **no** se ejecuta cuando el módulo es *importado*, solo cuando `mi_modulo.py` se ejecuta *directamente* como script principal. Esto es útil para poner código de prueba o ejemplos dentro del propio módulo.

**Otras Formas de Importar:**

*   **`from ... import ...`:** Importa miembros específicos de un módulo directamente al espacio de nombres actual. No necesitas usar el prefijo `nombre_modulo.`.

    ```python
    # programa_principal_v2.py
    from mi_modulo import saludar, calcular_area_circulo, MiClaseModulo

    print("--- Usando from...import ---")

    # Ahora puedes llamar directamente
    saludar("Bob")
    area = calcular_area_circulo(7)
    print(f"Área calculada: {area}")
    obj = MiClaseModulo(200)
    obj.mostrar()

    # PI no fue importado directamente, esto daría NameError:
    # print(PI)
    ```
    *   **Precaución:** Si importas algo con el mismo nombre que ya existe en tu archivo actual, lo sobrescribirás.

*   **`from ... import *`:** Importa *todos* los nombres públicos de un módulo al espacio de nombres actual. **¡Generalmente considerado una mala práctica!** Hace difícil saber de dónde viene cada nombre y puede causar colisiones de nombres inesperadas. Evítalo si es posible.

    ```python
    # programa_principal_v3.py (NO RECOMENDADO)
    # from mi_modulo import *
    # saludar("Charlie")
    # print(PI)
    ```

*   **`import ... as ...`:** Importa un módulo (o un miembro) y le da un alias (un nombre más corto o diferente) en tu archivo actual. Muy útil para módulos con nombres largos o para evitar colisiones.

    ```python
    # programa_principal_v4.py
    import mi_modulo as mm # Alias 'mm' para mi_modulo
    from mi_modulo import calcular_area_circulo as area_circ

    print("--- Usando alias (as) ---")

    print(f"PI desde alias: {mm.PI}")
    mm.saludar("David")
    a = area_circ(3)
    print(f"Área con alias de función: {a}")
    ```
    *   Es muy común ver alias como `import numpy as np`, `import pandas as pd`, `import matplotlib.pyplot as plt`.

## Paquetes

*   **¿Qué es?** Un paquete es una forma de estructurar el espacio de nombres de los módulos de Python utilizando la "notación de puntos". Esencialmente, un paquete es una **carpeta** que contiene:
    *   Otros módulos (`.py`).
    *   Otras subcarpetas (que a su vez son sub-paquetes).
    *   Un archivo especial (opcional en Python 3.3+, pero aún recomendado por compatibilidad y para inicialización) llamado `__init__.py`. La presencia de este archivo (incluso si está vacío) le indica a Python que el directorio debe ser tratado como un paquete.
*   **Propósito:** Permite organizar módulos relacionados jerárquicamente, evitando conflictos de nombres entre módulos de diferentes paquetes y facilitando la distribución de colecciones grandes de módulos (bibliotecas).

**Creando un Paquete Simple:**

1.  Crea una carpeta principal para tu paquete, por ejemplo, `mi_paquete`.
2.  Dentro de `mi_paquete`, crea un archivo (puede estar vacío) llamado `__init__.py`.
3.  Dentro de `mi_paquete`, crea algunos módulos, por ejemplo, `modulo_a.py` y `modulo_b.py`.
4.  (Opcional) Dentro de `mi_paquete`, crea una subcarpeta, por ejemplo, `sub_paquete`.
5.  Dentro de `sub_paquete`, crea otro `__init__.py` (vacío) y otro módulo, por ejemplo, `modulo_c.py`.

**Estructura de ejemplo:**

```
proyecto_principal/
├── programa_main.py
└── mi_paquete/
    ├── __init__.py
    ├── modulo_a.py
    ├── modulo_b.py
    └── sub_paquete/
        ├── __init__.py
        └── modulo_c.py
```

**Contenido de los módulos (ejemplos):**

```python
# mi_paquete/modulo_a.py
def funcion_a():
    print("Función A desde modulo_a en mi_paquete")

# mi_paquete/modulo_b.py
VARIABLE_B = "Soy B"

# mi_paquete/sub_paquete/modulo_c.py
def funcion_c():
    print("Función C desde modulo_c en sub_paquete")
```

**Importando desde un Paquete:**

Desde `programa_main.py` (que está fuera de `mi_paquete`), puedes importar usando la notación de puntos:

```python
# programa_main.py

# Importar un módulo completo del paquete
import mi_paquete.modulo_a
mi_paquete.modulo_a.funcion_a()

# Importar un miembro específico usando from
from mi_paquete.modulo_b import VARIABLE_B
print(f"Variable de modulo_b: {VARIABLE_B}")

# Importar un módulo de un sub-paquete
import mi_paquete.sub_paquete.modulo_c as mod_c # Usando alias
mod_c.funcion_c()

# Importar un miembro específico de un sub-paquete
from mi_paquete.sub_paquete.modulo_c import funcion_c
funcion_c() # Llamada directa
```

**El archivo `__init__.py`:**

*   Se ejecuta automáticamente cuando se importa el paquete (o un módulo dentro de él) por primera vez.
*   Puede estar vacío (solo para marcar el directorio como paquete).
*   Puede contener código de inicialización para el paquete.
*   Puede definir qué se importa cuando se hace `from mi_paquete import *` (usando la variable `__all__`).
*   Puede importar miembros de sus propios módulos para hacerlos accesibles directamente desde el paquete (ej. `import mi_paquete` y luego `mi_paquete.funcion_a()` en lugar de `mi_paquete.modulo_a.funcion_a()`). Esto se hace editando `mi_paquete/__init__.py`:
    ```python
    # mi_paquete/__init__.py
    print("Inicializando mi_paquete...")
    from .modulo_a import funcion_a # Importa funcion_a al nivel del paquete
    from .modulo_b import VARIABLE_B

    # Opcional: Define qué se importa con 'from mi_paquete import *'
    __all__ = ["funcion_a", "VARIABLE_B"]
    ```
    *   El `.` antes de `modulo_a` indica una importación relativa (dentro del mismo paquete).

Los módulos y paquetes son esenciales para escribir código Python organizado, reutilizable y escalable, especialmente en proyectos grandes o al crear bibliotecas para compartir.
# Módulo 2: Manejo de Ficheros (Lectura y Escritura)

Interactuar con archivos (ficheros) en el disco duro es una necesidad común en programación. Python proporciona funciones incorporadas para abrir, leer, escribir y cerrar archivos de texto y binarios.

## Abriendo un Archivo (`open()`)

La función principal para trabajar con archivos es `open()`. Devuelve un objeto archivo que luego puedes usar para leer o escribir.

**Sintaxis:**

```python
objeto_archivo = open("ruta/al/archivo.txt", "modo")
# ... operaciones de lectura/escritura ...
objeto_archivo.close() # ¡Importante cerrar el archivo!
```

*   **`ruta/al/archivo.txt`**: Es la ruta (path) al archivo que quieres abrir. Puede ser:
    *   **Ruta Relativa:** Relativa al directorio donde se está ejecutando tu script Python (ej. `"datos.txt"`, `"config/settings.ini"`).
    *   **Ruta Absoluta:** La ruta completa desde la raíz del sistema de archivos (ej. `"C:/Usuarios/TuUsuario/Documentos/reporte.txt"` en Windows, `"/home/tuusuario/documentos/reporte.txt"` en Linux/macOS). **Nota:** En Windows, usa barras inclinadas `/` o escapa las barras invertidas `\\` (ej. `"C:\\Usuarios\\..."`).
*   **`modo`**: Es una cadena que especifica cómo quieres abrir el archivo (para leer, escribir, etc.). Los modos más comunes son:
    *   `'r'` (Read - Leer): Modo por defecto. Abre el archivo para **lectura**. Da error si el archivo no existe.
    *   `'w'` (Write - Escribir): Abre el archivo para **escritura**.
        *   **Si el archivo existe, sobrescribe completamente su contenido.**
        *   Si el archivo no existe, lo crea.
    *   `'a'` (Append - Añadir): Abre el archivo para **añadir** contenido al final. Si el archivo no existe, lo crea. No sobrescribe el contenido existente.
    *   `'r+'`: Abre para **lectura y escritura**. El puntero se sitúa al principio.
    *   `'w+'`: Abre para **escritura y lectura**. Sobrescribe el archivo si existe, lo crea si no.
    *   `'a+'`: Abre para **añadir y lectura**. El puntero se sitúa al final para escribir. Si no existe, lo crea.
    *   `'b'` (Binary - Binario): Se puede añadir a cualquier modo (ej. `'rb'`, `'wb'`) para trabajar con archivos binarios (imágenes, ejecutables, etc.) en lugar de archivos de texto.
    *   `'t'` (Text - Texto): Modo por defecto si no se especifica `'b'`. Trabaja con archivos de texto, manejando la codificación de caracteres.

*   **`objeto_archivo.close()`**: Es **crucial** cerrar el archivo después de terminar de trabajar con él. Esto asegura que todos los datos se escriban correctamente en el disco y libera los recursos del sistema asociados al archivo.

## La Declaración `with` (Método Recomendado)

Olvidarse de cerrar un archivo es un error común. La forma **recomendada y más segura** de trabajar con archivos en Python es usando la declaración `with`, que actúa como un **context manager**:

**Sintaxis:**

```python
try:
    with open("ruta/al/archivo.txt", "modo") as alias_objeto_archivo:
        # Bloque de código donde trabajas con el archivo
        # usando 'alias_objeto_archivo'
        contenido = alias_objeto_archivo.read()
        # ... más operaciones ...
    # --- El archivo se cierra AUTOMÁTICAMENTE aquí ---
    # incluso si ocurren errores dentro del bloque 'with'.

except FileNotFoundError:
    print("Error: El archivo no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

print("El bloque 'with' ha terminado (archivo cerrado).")
```

*   `with open(...) as alias_objeto_archivo:`: Abre el archivo y lo asigna al alias que elijas (ej. `f`, `archivo`, `input_file`).
*   El bloque indentado debajo del `with` es donde realizas las operaciones con el archivo.
*   **Ventaja Principal:** Python garantiza que el archivo se cerrará automáticamente (`alias_objeto_archivo.close()` se llama implícitamente) al salir del bloque `with`, sin importar si la salida fue normal o debido a una excepción. **¡Usa `with` siempre que sea posible!**

## Leyendo Archivos de Texto

Una vez abierto en modo lectura (`'r'`, `'r+'`, `'a+'`), puedes leer su contenido:

```python
# Crear un archivo de ejemplo primero
try:
    with open("ejemplo_lectura.txt", "w") as f:
        f.write("Primera línea.\n")
        f.write("Segunda línea con números: 123.\n")
        f.write("Tercera y última línea.\n")
except Exception as e:
    print(f"Error creando archivo de ejemplo: {e}")

# --- Leer el archivo completo ---
print("\n--- Leyendo archivo completo (read()) ---")
try:
    with open("ejemplo_lectura.txt", "r") as f:
        contenido_completo = f.read() # Lee todo el archivo en una sola cadena
        print("Contenido:")
        print(contenido_completo)
except FileNotFoundError:
    print("Error: ejemplo_lectura.txt no encontrado.")

# --- Leer línea por línea (readline()) ---
print("\n--- Leyendo línea por línea (readline()) ---")
try:
    with open("ejemplo_lectura.txt", "r") as f:
        linea1 = f.readline() # Lee la primera línea (incluye el \n al final)
        linea2 = f.readline() # Lee la segunda línea
        print(f"Línea 1: {linea1.strip()}") # .strip() quita espacios/saltos de línea al inicio/final
        print(f"Línea 2: {linea2.strip()}")
        # Puedes seguir llamando a readline() hasta que devuelva una cadena vacía ""
except FileNotFoundError:
    print("Error: ejemplo_lectura.txt no encontrado.")

# --- Leer todas las líneas en una lista (readlines()) ---
print("\n--- Leyendo todas las líneas en lista (readlines()) ---")
try:
    with open("ejemplo_lectura.txt", "r") as f:
        todas_las_lineas = f.readlines() # Devuelve una lista donde cada elemento es una línea (con \n)
        print(todas_las_lineas)
        # Procesando la lista:
        for i, linea in enumerate(todas_las_lineas):
            print(f"Lista - Línea {i}: {linea.strip()}")
except FileNotFoundError:
    print("Error: ejemplo_lectura.txt no encontrado.")

# --- Iterar directamente sobre el objeto archivo (Forma más Pythonica) ---
print("\n--- Iterando directamente sobre el archivo ---")
try:
    with open("ejemplo_lectura.txt", "r") as f:
        # El objeto archivo es iterable, cada iteración devuelve una línea
        for numero_linea, linea_actual in enumerate(f):
            print(f"Iter - Línea {numero_linea}: {linea_actual.strip()}")
except FileNotFoundError:
    print("Error: ejemplo_lectura.txt no encontrado.")

```

## Escribiendo en Archivos de Texto

Para escribir, abre el archivo en modo `'w'` (sobrescribir) o `'a'` (añadir).

```python
# --- Escribir (sobrescribir) en un archivo ('w') ---
print("\n--- Escribiendo (sobrescribiendo) archivo ('w') ---")
try:
    with open("ejemplo_escritura.txt", "w") as f:
        f.write("Este es contenido nuevo.\n") # Escribe una cadena
        f.write("Sobrescribe lo que había antes.\n")
        num = 42
        f.write(f"Puedes escribir variables formateadas: {num}\n")
        # writelines() escribe los elementos de una lista (deben ser strings)
        lineas_a_escribir = ["Lista línea 1\n", "Lista línea 2\n"]
        f.writelines(lineas_a_escribir)
    print("Archivo 'ejemplo_escritura.txt' escrito (modo 'w').")
except Exception as e:
    print(f"Error escribiendo en modo 'w': {e}")

# Verificar el contenido
try:
    with open("ejemplo_escritura.txt", "r") as f:
        print("Contenido después de 'w':")
        print(f.read())
except Exception as e:
    print(f"Error leyendo después de 'w': {e}")


# --- Añadir a un archivo ('a') ---
print("\n--- Añadiendo a archivo ('a') ---")
try:
    with open("ejemplo_escritura.txt", "a") as f:
        f.write("--- Contenido añadido ---\n")
        f.write("Esta línea se añade al final.\n")
    print("Contenido añadido a 'ejemplo_escritura.txt' (modo 'a').")
except Exception as e:
    print(f"Error escribiendo en modo 'a': {e}")

# Verificar el contenido de nuevo
try:
    with open("ejemplo_escritura.txt", "r") as f:
        print("Contenido después de 'a':")
        print(f.read())
except Exception as e:
    print(f"Error leyendo después de 'a': {e}")
```

**Consideraciones:**

*   **Codificación (Encoding):** Al trabajar con texto, especialmente si contiene caracteres no ingleses (acentos, ñ, etc.), es buena práctica especificar la codificación, comúnmente UTF-8: `open("archivo.txt", "r", encoding="utf-8")`. Si no se especifica, Python usa una codificación por defecto del sistema, que puede variar y causar problemas.
*   **Archivos Binarios:** Para archivos no textuales (imágenes, audio, etc.), usa los modos binarios (`'rb'`, `'wb'`, `'ab'`, etc.). Las operaciones de lectura/escritura trabajarán con bytes (`bytes`) en lugar de cadenas (`str`).

El manejo de archivos es una habilidad esencial. Recuerda siempre usar `with` para garantizar que los archivos se cierren correctamente y maneja posibles errores como `FileNotFoundError`.
# Módulo 2: Comprensión de Listas, Diccionarios y Conjuntos

Las **comprensiones** (Comprehensions) son una característica muy "Pythonica" que ofrece una sintaxis concisa y legible para crear nuevas listas, diccionarios o conjuntos a partir de secuencias existentes (u otros iterables). A menudo, pueden reemplazar bucles `for` más largos y explícitos para tareas comunes de creación de colecciones.

## 1. Comprensión de Listas (List Comprehensions)

Permiten crear nuevas listas aplicando una expresión a cada elemento de una secuencia iterable, opcionalmente filtrando elementos con una condición.

**Sintaxis Básica:**

```python
nueva_lista = [expresion for elemento in iterable]
```

**Sintaxis con Condición (`if`):**

```python
nueva_lista = [expresion for elemento in iterable if condicion]
```

**Sintaxis con `if-else` (Expresión Condicional):**

```python
nueva_lista = [expresion_si_true if condicion else expresion_si_false for elemento in iterable]
```

**Equivalencia con Bucle `for`:**

La sintaxis básica `[expresion for elemento in iterable]` es equivalente a:

```python
nueva_lista = []
for elemento in iterable:
    nueva_lista.append(expresion)
```

La sintaxis con `if` `[expresion for elemento in iterable if condicion]` es equivalente a:

```python
nueva_lista = []
for elemento in iterable:
    if condicion:
        nueva_lista.append(expresion)
```

**Ejemplos:**

```python
# Ejemplo 1: Crear una lista con los cuadrados de los números del 0 al 9
# Usando bucle for tradicional
cuadrados_for = []
for x in range(10):
    cuadrados_for.append(x**2)
print(f"Cuadrados (for): {cuadrados_for}")

# Usando list comprehension (más conciso)
cuadrados_comp = [x**2 for x in range(10)]
print(f"Cuadrados (comp): {cuadrados_comp}")

# Ejemplo 2: Crear una lista con los números pares del 0 al 9
# Usando bucle for con if
pares_for = []
for x in range(10):
    if x % 2 == 0:
        pares_for.append(x)
print(f"Pares (for): {pares_for}")

# Usando list comprehension con if
pares_comp = [x for x in range(10) if x % 2 == 0]
print(f"Pares (comp): {pares_comp}")

# Ejemplo 3: Crear una lista de frutas en mayúsculas
frutas = ["manzana", "banana", "cereza"]
mayusculas_comp = [fruta.upper() for fruta in frutas]
print(f"Frutas mayúsculas: {mayusculas_comp}")

# Ejemplo 4: Crear una lista indicando si cada número es par o impar
numeros = [0, 1, 2, 3, 4, 5]
par_impar_comp = ["Par" if num % 2 == 0 else "Impar" for num in numeros]
print(f"Par/Impar: {par_impar_comp}")

# Ejemplo 5: Comprensiones anidadas (crear pares)
pares_anidados = [(x, y) for x in [1, 2] for y in [3, 4]]
# Equivalente a:
# pares_anidados_for = []
# for x in [1, 2]:
#     for y in [3, 4]:
#         pares_anidados_for.append((x, y))
print(f"Pares anidados: {pares_anidados}") # Salida: [(1, 3), (1, 4), (2, 3), (2, 4)]
```

## 2. Comprensión de Diccionarios (Dictionary Comprehensions)

Similar a las listas, pero crean diccionarios. Se usan llaves `{}` y se especifica un par `clave: valor`.

**Sintaxis Básica:**

```python
nuevo_dict = {clave_expresion: valor_expresion for elemento in iterable}
```

**Sintaxis con Condición (`if`):**

```python
nuevo_dict = {clave_expresion: valor_expresion for elemento in iterable if condicion}
```

**Ejemplos:**

```python
# Ejemplo 1: Crear un diccionario con números y sus cuadrados
cuadrados_dict = {x: x**2 for x in range(5)}
print(f"Dict cuadrados: {cuadrados_dict}")
# Salida: Dict cuadrados: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Ejemplo 2: Crear un diccionario a partir de dos listas (nombres y edades)
nombres = ["Ana", "Luis", "Eva"]
edades = [25, 30, 22]
# Usando zip para emparejar las listas
personas_dict = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(f"Dict personas: {personas_dict}")
# Salida: Dict personas: {'Ana': 25, 'Luis': 30, 'Eva': 22}

# Ejemplo 3: Crear un diccionario con palabras y su longitud, solo para palabras largas
texto = "esta es una frase de ejemplo con algunas palabras"
palabras = texto.split() # Divide el string en una lista de palabras
largas_dict = {palabra: len(palabra) for palabra in palabras if len(palabra) > 4}
print(f"Dict palabras largas: {largas_dict}")
# Salida: Dict palabras largas: {'frase': 5, 'ejemplo': 7, 'algunas': 7, 'palabras': 8}

# Ejemplo 4: Invertir un diccionario (claves por valores) - ¡Cuidado si los valores no son únicos!
original_dict = {'a': 1, 'b': 2, 'c': 3}
invertido_dict = {valor: clave for clave, valor in original_dict.items()}
print(f"Dict invertido: {invertido_dict}")
# Salida: Dict invertido: {1: 'a', 2: 'b', 3: 'c'}
```

## 3. Comprensión de Conjuntos (Set Comprehensions)

Crean conjuntos (`set`). La sintaxis es similar a la de listas, pero usando llaves `{}` y sin especificar un par clave-valor (solo la expresión para el elemento). Recuerda que los conjuntos solo almacenan elementos únicos.

**Sintaxis Básica:**

```python
nuevo_set = {expresion for elemento in iterable}
```

**Sintaxis con Condición (`if`):**

```python
nuevo_set = {expresion for elemento in iterable if condicion}
```

**Ejemplos:**

```python
# Ejemplo 1: Crear un conjunto con los cuadrados de números (duplicados se eliminan)
numeros_lista = [1, 2, 2, 3, 3, 3, 4]
cuadrados_set = {x**2 for x in numeros_lista}
print(f"Set cuadrados: {cuadrados_set}")
# Salida: Set cuadrados: {1, 4, 9, 16}

# Ejemplo 2: Crear un conjunto con las iniciales en mayúscula de una lista de nombres
nombres = ["ana", "luis", "eva", "ana"]
iniciales_set = {nombre[0].upper() for nombre in nombres}
print(f"Set iniciales: {iniciales_set}")
# Salida: Set iniciales: {'E', 'A', 'L'}

# Ejemplo 3: Crear un conjunto de números divisibles por 3 del 0 al 15
divisibles_3_set = {n for n in range(16) if n % 3 == 0}
print(f"Set divisibles por 3: {divisibles_3_set}")
# Salida: Set divisibles por 3: {0, 3, 6, 9, 12, 15}
```

**Ventajas de las Comprensiones:**

*   **Concisión:** Código más corto y a menudo más legible que los bucles `for` equivalentes.
*   **Eficiencia:** Suelen ser ligeramente más rápidas que los bucles `for` explícitos para crear colecciones, ya que están optimizadas internamente en CPython.

**Cuándo usarlas:**

Son ideales para crear colecciones basadas en transformaciones o filtrados simples de otras secuencias. Si la lógica para crear cada elemento es muy compleja (múltiples `if/else`, cálculos extensos), un bucle `for` tradicional podría ser más legible.
# Módulo 2: Funciones Lambda, `map` y `filter`

Python ofrece herramientas que facilitan un estilo de programación más funcional, permitiendo operar sobre secuencias de datos de forma concisa. Tres de estas herramientas son las funciones lambda, `map()` y `filter()`.

## Funciones Lambda (Funciones Anónimas)

*   **¿Qué son?** Son funciones pequeñas y **anónimas** (sin nombre definido con `def`) que se definen usando la palabra clave `lambda`.
*   **Sintaxis:** `lambda argumentos: expresion`
*   **Características:**
    *   Pueden tener cualquier número de `argumentos`, pero solo **una única `expresion`**.
    *   La `expresion` se evalúa y su resultado es lo que la función lambda **devuelve implícitamente** (no se usa `return`).
    *   Son útiles cuando necesitas una función simple por un corto período de tiempo, especialmente como argumento para otras funciones de orden superior (como `map`, `filter`, `sorted`).

**Ejemplos:**

```python
# Función normal para sumar 5
def sumar_cinco_def(x):
    return x + 5

# Función lambda equivalente
sumar_cinco_lambda = lambda x: x + 5

print(f"Usando def: {sumar_cinco_def(10)}")    # Salida: Usando def: 15
print(f"Usando lambda: {sumar_cinco_lambda(10)}") # Salida: Usando lambda: 15

# Lambda con múltiples argumentos
multiplicar = lambda a, b: a * b
print(f"Multiplicar (lambda): {multiplicar(6, 7)}") # Salida: Multiplicar (lambda): 42

# Uso común: como argumento para ordenar una lista de tuplas por el segundo elemento
puntos = [(1, 5), (3, 2), (5, 8), (2, 1)]
puntos_ordenados = sorted(puntos, key=lambda punto: punto[1]) # Usa lambda para extraer el 2do elemento como clave de ordenación
print(f"Puntos ordenados por Y: {puntos_ordenados}")
# Salida: Puntos ordenados por Y: [(2, 1), (3, 2), (1, 5), (5, 8)]
```

Aunque puedes asignar una lambda a una variable (como `sumar_cinco_lambda`), PEP 8 generalmente recomienda usar `def` para funciones con nombre, ya que mejora la legibilidad y la depuración. El verdadero poder de lambda reside en su uso directo como argumento.

## La Función `map()`

*   **¿Qué hace?** Aplica una función dada a **cada elemento** de una secuencia iterable (lista, tupla, etc.) y devuelve un **iterador** con los resultados.
*   **Sintaxis:** `map(funcion, iterable1, [iterable2, ...])`
*   **Características:**
    *   `funcion`: La función que se aplicará a cada elemento. Puede ser una función definida con `def` o una `lambda`.
    *   `iterable`: La secuencia cuyos elementos serán procesados. Puedes pasar múltiples iterables si la función toma múltiples argumentos.
    *   **Devuelve un iterador `map`:** No devuelve una lista directamente. Necesitas convertirlo a una lista (u otro tipo) si quieres ver todos los resultados a la vez (ej. `list(map(...))`). Esto lo hace eficiente en memoria para secuencias grandes, ya que procesa los elementos bajo demanda.

**Ejemplos:**

```python
numeros = [1, 2, 3, 4, 5]

# Ejemplo 1: Elevar al cuadrado cada número usando map y una función def
def cuadrado(n):
    return n**2

cuadrados_map_def = map(cuadrado, numeros)
print(f"Objeto map (def): {cuadrados_map_def}") # Salida: Objeto map (def): <map object at 0x...>
print(f"Lista de cuadrados (def): {list(cuadrados_map_def)}") # Salida: Lista de cuadrados (def): [1, 4, 9, 16, 25]

# Ejemplo 2: Elevar al cuadrado usando map y lambda (más conciso)
cuadrados_map_lambda = map(lambda x: x**2, numeros)
print(f"Lista de cuadrados (lambda): {list(cuadrados_map_lambda)}") # Salida: Lista de cuadrados (lambda): [1, 4, 9, 16, 25]

# Ejemplo 3: Convertir lista de strings a mayúsculas
palabras = ["hola", "mundo", "python"]
mayusculas_map = map(str.upper, palabras) # str.upper es un método, se pasa sin ()
print(f"Mayúsculas (map): {list(mayusculas_map)}") # Salida: Mayúsculas (map): ['HOLA', 'MUNDO', 'PYTHON']

# Ejemplo 4: Sumar elementos de dos listas
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
sumas_map = map(lambda x, y: x + y, lista1, lista2)
print(f"Sumas de listas (map): {list(sumas_map)}") # Salida: Sumas de listas (map): [11, 22, 33]

# Comparación con List Comprehension (a menudo más legible para casos simples)
cuadrados_comp = [x**2 for x in numeros]
print(f"Cuadrados (comp): {cuadrados_comp}") # Salida: Cuadrados (comp): [1, 4, 9, 16, 25]
```

## La Función `filter()`

*   **¿Qué hace?** Filtra elementos de una secuencia iterable, manteniendo solo aquellos para los cuales una función dada devuelve `True`. Devuelve un **iterador** con los elementos que pasaron el filtro.
*   **Sintaxis:** `filter(funcion_booleana, iterable)`
*   **Características:**
    *   `funcion_booleana`: Una función que recibe un elemento del iterable y devuelve `True` (para mantener el elemento) o `False` (para descartarlo). Puede ser una función `def` o una `lambda`. Si se pasa `None` como función, `filter` elimina los elementos que son considerados "falsy" en Python (0, "", [], {}, False, None).
    *   `iterable`: La secuencia a filtrar.
    *   **Devuelve un iterador `filter`:** Al igual que `map`, necesitas convertirlo (ej. `list(filter(...))`) para ver los resultados.

**Ejemplos:**

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejemplo 1: Filtrar números pares usando filter y una función def
def es_par(n):
    return n % 2 == 0

pares_filter_def = filter(es_par, numeros)
print(f"Objeto filter (def): {pares_filter_def}") # Salida: Objeto filter (def): <filter object at 0x...>
print(f"Lista de pares (def): {list(pares_filter_def)}") # Salida: Lista de pares (def): [2, 4, 6, 8, 10]

# Ejemplo 2: Filtrar números pares usando filter y lambda
pares_filter_lambda = filter(lambda x: x % 2 == 0, numeros)
print(f"Lista de pares (lambda): {list(pares_filter_lambda)}") # Salida: Lista de pares (lambda): [2, 4, 6, 8, 10]

# Ejemplo 3: Filtrar palabras que empiezan con 'P' (ignorando mayúsculas/minúsculas)
palabras = ["Python", "es", "poderoso", "pero", "practica"]
palabras_p = filter(lambda p: p.lower().startswith('p'), palabras)
print(f"Palabras con P (filter): {list(palabras_p)}") # Salida: Palabras con P (filter): ['Python', 'poderoso', 'pero', 'practica']

# Ejemplo 4: Filtrar elementos "falsy" usando None como función
mezcla = [0, "Hola", "", None, 100, False, True, [], [1,2]]
verdaderos = filter(None, mezcla)
print(f"Elementos 'truthy' (filter None): {list(verdaderos)}")
# Salida: Elementos 'truthy' (filter None): ['Hola', 100, True, [1, 2]]

# Comparación con List Comprehension (a menudo más legible)
pares_comp = [x for x in numeros if x % 2 == 0]
print(f"Pares (comp): {pares_comp}") # Salida: Pares (comp): [2, 4, 6, 8, 10]
```

**`map` vs. `filter` vs. List Comprehension:**

*   `map`: Aplica una función a *todos* los elementos para transformarlos. El número de elementos resultante es el mismo que el original.
*   `filter`: Selecciona un *subconjunto* de elementos basado en una condición. El número de elementos resultante es menor o igual que el original.
*   **List Comprehensions:** Pueden realizar tanto mapeo (`[expresion for ...]`) como filtrado (`[... for ... if condicion]`) en una sola expresión, y a menudo resultan más legibles para casos comunes. Sin embargo, `map` y `filter` pueden ser útiles con funciones más complejas o cuando se prefiere un estilo puramente funcional, y su naturaleza de iteradores puede ser más eficiente en memoria para datos muy grandes.

Dominar `lambda`, `map` y `filter` te proporciona herramientas poderosas para procesar datos de manera eficiente y concisa en Python.
# Módulo 2: Introducción a Decoradores

Los **Decoradores** son una característica poderosa y expresiva de Python, aunque pueden parecer un poco mágicos al principio. En esencia, un decorador es una **función que toma otra función como argumento, le añade alguna funcionalidad extra, y devuelve otra función**, todo esto sin modificar el código fuente de la función original.

Se utilizan ampliamente para:

*   Logging (registrar cuándo se llama a una función, qué argumentos recibe, etc.).
*   Control de acceso y permisos (ej. verificar si un usuario está logueado antes de ejecutar una función).
*   Instrumentación y temporización (ej. medir cuánto tarda en ejecutarse una función).
*   Validación de argumentos.
*   Caching de resultados.
*   Y mucho más...

## Entendiendo las Bases: Funciones como Objetos

Para entender los decoradores, recuerda que en Python, las funciones son **objetos de primera clase**. Esto significa que puedes:

*   Asignar una función a una variable.
*   Pasar una función como argumento a otra función.
*   Devolver una función desde otra función.
*   Definir una función dentro de otra función (funciones anidadas).

```python
def funcion_original():
    print("Ejecutando la función original.")

# 1. Asignar a variable
mi_variable_funcion = funcion_original
mi_variable_funcion() # Llama a funcion_original

# 2. Pasar como argumento
def ejecutar_funcion(func):
    print("Antes de ejecutar la función pasada.")
    func()
    print("Después de ejecutar la función pasada.")

ejecutar_funcion(funcion_original)

# 3. Devolver una función
def crear_saludador(saludo):
    def saludar_interno(nombre):
        print(f"{saludo}, {nombre}!")
    return saludar_interno # Devuelve la función anidada

saludador_hola = crear_saludador("Hola")
saludador_hola("Mundo") # Salida: Hola, Mundo!
```

## Creando un Decorador Simple

Un decorador es, típicamente, una función que define una función "envoltoria" (wrapper) anidada. Esta envoltoria realiza acciones antes y/o después de llamar a la función original que se le pasó.

```python
# Paso 1: El decorador es una función que recibe otra función (func)
def mi_decorador_simple(func):
    # Paso 2: Define la función envoltoria (wrapper)
    # Esta wrapper recibirá los mismos argumentos que la función original
    def wrapper(*args, **kwargs):
        print("--- Algo ANTES de llamar a la función original ---")
        # Paso 3: Llama a la función original pasada como argumento
        resultado = func(*args, **kwargs) # Pasa los argumentos recibidos
        print("--- Algo DESPUÉS de llamar a la función original ---")
        # Paso 4: La wrapper devuelve el resultado de la función original (si lo hay)
        return resultado
    # Paso 5: El decorador devuelve la función envoltoria
    return wrapper

# --- Aplicando el decorador ---

# Forma 1: Sintaxis Clásica (menos común hoy en día)
def decir_hola():
    print("¡Hola!")

# 'Decoramos' la función manualmente
funcion_decorada = mi_decorador_simple(decir_hola)
print("\nLlamando a la función decorada manualmente:")
funcion_decorada() # Ejecuta la wrapper, que a su vez ejecuta decir_hola

# Forma 2: Usando la sintaxis de azúcar '@' (MUCHO más común y legible)
@mi_decorador_simple
def decir_adios(nombre):
    print(f"¡Adiós, {nombre}!")
    return f"Mensaje de despedida para {nombre}"

print("\nLlamando a la función decorada con '@':")
valor_devuelto = decir_adios("Ana") # Llama directamente a decir_adios, pero se ejecuta la wrapper
print(f"Valor devuelto por la función decorada: {valor_devuelto}")

# ¿Qué hace '@mi_decorador_simple' encima de 'def decir_adios(...):'?
# Es exactamente equivalente a hacer esto después de definir decir_adios:
# decir_adios = mi_decorador_simple(decir_adios)
```

**Explicación del `wrapper(*args, **kwargs)`:**

*   `*args`: Permite a la función `wrapper` aceptar cualquier número de argumentos posicionales. Los recoge en una tupla llamada `args`.
*   `**kwargs`: Permite a la función `wrapper` aceptar cualquier número de argumentos de palabra clave. Los recoge en un diccionario llamado `kwargs`.
*   `func(*args, **kwargs)`: Al llamar a la función original `func`, usamos `*args` y `**kwargs` para "desempaquetar" los argumentos recibidos por `wrapper` y pasárselos correctamente a `func`, sin importar cuántos o qué tipo de argumentos eran. Esto hace que el decorador sea genérico y funcione con funciones que tengan diferentes firmas (diferentes parámetros).

## Ejemplo: Decorador de Temporización

```python
import time

def temporizador(func):
    def wrapper(*args, **kwargs):
        inicio = time.time() # Tiempo antes de ejecutar
        resultado = func(*args, **kwargs) # Ejecuta la función original
        fin = time.time() # Tiempo después de ejecutar
        duracion = fin - inicio
        print(f"'{func.__name__}' tardó {duracion:.6f} segundos en ejecutarse.")
        return resultado
    return wrapper

@temporizador
def calculo_largo(n):
    """Simula un cálculo que toma tiempo."""
    suma = 0
    for i in range(n):
        suma += i
    time.sleep(0.5) # Pausa para simular trabajo
    return suma

@temporizador
def saludar_rapido(nombre):
    return f"Hola {nombre}"

print("\n--- Probando decorador temporizador ---")
resultado_calculo = calculo_largo(100000)
# print(f"Resultado del cálculo: {resultado_calculo}") # Descomentar si quieres ver el resultado
saludo = saludar_rapido("Equipo")
print(saludo)
```

**Salida esperada (los tiempos exactos variarán):**

```
--- Probando decorador temporizador ---
'calculo_largo' tardó 0.50xxxx segundos en ejecutarse.
'saludar_rapido' tardó 0.000xxx segundos en ejecutarse.
Hola Equipo
```

Los decoradores son un concepto clave para escribir código Python avanzado, limpio y reutilizable. Permiten añadir funcionalidades transversales (como logging, timing, control de acceso) a tus funciones de una manera elegante y separada de la lógica principal de la función. Aunque la sintaxis `@` oculta parte de la mecánica, entender cómo funcionan por debajo (funciones que envuelven otras funciones) es fundamental.
# Módulo 2: Estructura de un Proyecto Python Estándar

Cuando empiezas un nuevo proyecto en Python, especialmente uno que crecerá más allá de un simple script, es crucial adoptar una **estructura de directorios organizada y estándar**. Esto ofrece múltiples beneficios:

*   **Claridad:** Es más fácil para ti y para otros entender dónde encontrar cada tipo de archivo (código fuente, pruebas, documentación, configuración, etc.).
*   **Mantenibilidad:** Simplifica la modificación y la adición de nuevas funcionalidades.
*   **Reutilización:** Facilita la conversión de tu proyecto en un paquete instalable si es necesario.
*   **Colaboración:** Permite que los miembros del equipo trabajen de manera más eficiente al seguir convenciones conocidas.
*   **Herramientas:** Muchas herramientas de desarrollo (testing, documentación, empaquetado) esperan una cierta estructura.

No existe una única estructura "oficial" obligatoria, pero sí hay patrones y convenciones muy extendidos en la comunidad Python. A continuación, se describe una estructura común y recomendada para muchos tipos de proyectos.

## Estructura Típica

```
nombre_del_proyecto/
│
├── .gitignore             # Archivos/patrones a ignorar por Git
├── README.md              # Descripción del proyecto, instrucciones de uso/instalación
├── requirements.txt       # Lista de dependencias (para pip)
├── environment.yml        # Lista de dependencias (para conda - opcional/alternativo)
├── setup.py               # Metadatos y script de instalación (más tradicional)
│   o pyproject.toml       # Metadatos y configuración de build (más moderno)
│
├── src/                   # Directorio principal del código fuente (opción 1)
│   └── nombre_paquete/    # El paquete Python real de tu proyecto
│       ├── __init__.py    # Marca el directorio como paquete
│       ├── modulo1.py
│       ├── modulo2.py
│       └── subpaquete/
│           ├── __init__.py
│           └── modulo3.py
│
├── nombre_paquete/        # Directorio principal del código fuente (opción 2 - si no usas src/)
│   ├── __init__.py
│   ├── modulo1.py
│   └── ...
│
├── tests/                 # Directorio para las pruebas unitarias/integración
│   ├── __init__.py        # A veces necesario para que pytest descubra tests
│   ├── test_modulo1.py
│   └── test_subpaquete/
│       └── test_modulo3.py
│
├── docs/                  # Directorio para la documentación (ej. Sphinx)
│   ├── conf.py
│   ├── index.rst
│   └── ...
│
├── data/                  # Directorio para archivos de datos (opcional)
│   ├── raw/
│   └── processed/
│
└── scripts/               # Directorios para scripts auxiliares (opcional)
    ├── procesar_datos.py
    └── generar_reporte.py

```

## Descripción de Componentes:

*   **Directorio Raíz (`nombre_del_proyecto/`)**: La carpeta principal que contiene todo el proyecto. Debería ser un repositorio Git (`git init` aquí).
*   **`.gitignore`**: Especifica qué archivos o directorios Git debe ignorar (ej. `__pycache__/`, `*.pyc`, `*.env`, `*.log`, entornos virtuales como `venv/` o `env/`). Es fundamental para mantener limpio el repositorio.
*   **`README.md`**: Archivo Markdown esencial que describe el proyecto: qué hace, cómo instalarlo, cómo ejecutarlo, cómo contribuir, etc. Es lo primero que alguien (¡incluido tu yo futuro!) verá.
*   **`requirements.txt`**: Lista las dependencias externas del proyecto que se instalan con `pip`. Se genera comúnmente con `pip freeze > requirements.txt` (dentro del entorno virtual activado). Se usa para instalar dependencias con `pip install -r requirements.txt`.
*   **`environment.yml`**: Alternativa (o complemento) a `requirements.txt` si usas `conda`. Define el entorno `conda`, incluyendo la versión de Python y las dependencias (de conda y pip). Se usa para crear el entorno con `conda env create -f environment.yml`. Muy común en proyectos de ciencia de datos.
*   **`setup.py` / `pyproject.toml`**: Archivos de metadatos utilizados por herramientas como `setuptools` y `pip` para construir, empaquetar y distribuir tu proyecto como una biblioteca instalable. `pyproject.toml` es el estándar más moderno para definir dependencias de construcción y metadatos.
*   **`src/` (Directorio Fuente - Opción 1, Recomendada)**:
    *   Contiene el código fuente principal de tu aplicación o biblioteca, organizado como un paquete Python (`nombre_paquete/`).
    *   **Ventaja:** Separa claramente el código fuente de los archivos de configuración, pruebas, etc., en la raíz. Evita problemas de importación accidentales si tienes un archivo con el mismo nombre en la raíz y dentro del paquete.
*   **`nombre_paquete/` (Directorio Fuente - Opción 2)**:
    *   Alternativamente, puedes colocar tu paquete Python directamente en la raíz del proyecto. Es más simple para proyectos pequeños, pero puede volverse menos claro a medida que el proyecto crece.
*   **`nombre_paquete/__init__.py`**: Marca el directorio `nombre_paquete` como un paquete Python, permitiendo importaciones como `import nombre_paquete.modulo1`. Puede estar vacío o contener inicialización del paquete.
*   **`tests/`**: Contiene todo el código de prueba (unitarias, de integración, etc.). La estructura de `tests/` a menudo refleja la estructura de tu paquete fuente para facilitar la localización de las pruebas correspondientes a cada módulo. Herramientas como `pytest` suelen descubrir y ejecutar pruebas automáticamente desde este directorio.
*   **`docs/`**: Contiene archivos para generar la documentación del proyecto. Herramientas como Sphinx son comunes para esto, utilizando formatos como reStructuredText (`.rst`) o Markdown (`.md`).
*   **`data/` (Opcional)**: Para almacenar archivos de datos necesarios para el proyecto, a menudo separados en subdirectorios como `raw` (datos originales) y `processed` (datos limpios o transformados). **Importante:** Si los datos son muy grandes, considera no incluirlos directamente en el repositorio Git (usa `.gitignore`) y proporciona instrucciones sobre cómo obtenerlos.
*   **`scripts/` (Opcional)**: Para scripts auxiliares que no forman parte de la biblioteca principal pero son útiles para el desarrollo, despliegue, procesamiento de datos, etc.

**Adaptaciones:**

Esta estructura es una guía. Puedes adaptarla según las necesidades de tu proyecto:

*   Proyectos muy pequeños pueden omitir `src/` o `docs/`.
*   Proyectos web (Django/Flask) tienen sus propias estructuras generadas por los frameworks, aunque a menudo incorporan elementos de esta estructura general.
*   Proyectos de ciencia de datos pueden tener carpetas adicionales como `notebooks/` para Jupyter Notebooks de exploración.

Adoptar una estructura de proyecto estándar desde el principio te ahorrará muchos dolores de cabeza a medida que tu proyecto evolucione. Facilita la navegación, las pruebas, la documentación y la colaboración.
# Módulo 2: Introducción a las Pruebas Unitarias (`unittest` / `pytest`)

Escribir código que funcione es solo una parte del desarrollo de software. ¿Cómo te aseguras de que tu código sigue funcionando correctamente a medida que añades nuevas características o modificas las existentes (refactorización)? La respuesta es **escribir pruebas automatizadas**.

Las **Pruebas Unitarias (Unit Tests)** son el tipo más básico de prueba automatizada. Se centran en verificar que las **unidades individuales** de código (generalmente funciones o métodos de una clase) funcionan como se espera de forma aislada.

**¿Por qué escribir Pruebas Unitarias?**

*   **Detectar Errores Temprano:** Atrapan bugs durante el desarrollo, cuando son más fáciles y baratos de corregir.
*   **Confianza en la Refactorización:** Te permiten modificar o reestructurar tu código con la seguridad de que si las pruebas pasan, no has roto la funcionalidad existente.
*   **Documentación Viva:** Las pruebas sirven como ejemplos ejecutables de cómo se supone que debe usarse tu código.
*   **Mejor Diseño:** Pensar en cómo probar una función a menudo te lleva a diseñarla de manera más modular y desacoplada.
*   **Regresión:** Evitan que errores ya corregidos vuelvan a aparecer accidentalmente en el futuro.

## Frameworks de Pruebas en Python

Python tiene varias herramientas para escribir y ejecutar pruebas unitarias. Dos de las más importantes son:

1.  **`unittest`:**
    *   Es el framework de pruebas **incorporado** en la biblioteca estándar de Python.
    *   Está inspirado en los frameworks xUnit (como JUnit para Java).
    *   Utiliza un enfoque basado en clases: escribes clases que heredan de `unittest.TestCase` y defines métodos de prueba dentro de ellas (que suelen empezar con `test_`).
    *   Proporciona métodos de aserción (assertions) como `assertEqual()`, `assertTrue()`, `assertRaises()`, etc., para verificar los resultados.

2.  **`pytest`:**
    *   Es un framework de pruebas de **terceros** (necesita instalarse: `pip install pytest` o `conda install pytest`).
    *   Es **extremadamente popular** en la comunidad Python por su sintaxis más simple y concisa, su potente sistema de fixtures (para configuración de pruebas) y su extensibilidad.
    *   Permite escribir pruebas como funciones simples (que suelen empezar con `test_`) usando la palabra clave `assert` de Python directamente para las verificaciones.
    *   Tiene un excelente sistema de descubrimiento de pruebas.

**Recomendación:** Aunque `unittest` está incorporado, **`pytest` es generalmente preferido** por su facilidad de uso y características avanzadas. Aprenderemos lo básico de ambos.

## Ejemplo Básico con `unittest`

1.  **Crea tu código a probar:** Guarda esto como `calculadora_simple.py`.

    ```python
    # calculadora_simple.py
    def sumar(a, b):
        """Suma dos números."""
        return a + b

    def restar(a, b):
        """Resta b de a."""
        return a - b
    ```

2.  **Crea el archivo de prueba:** Guarda esto como `test_calculadora_unittest.py` en el mismo directorio o en un subdirectorio `tests/`.

    ```python
    # test_calculadora_unittest.py
    import unittest
    from calculadora_simple import sumar, restar # Importa las funciones a probar

    class TestCalculadoraSimple(unittest.TestCase): # Hereda de unittest.TestCase

        # Un método de prueba (debe empezar con 'test_')
        def test_sumar_positivos(self):
            """Prueba la suma de dos números positivos."""
            resultado = sumar(5, 3)
            self.assertEqual(resultado, 8) # Afirma que resultado es igual a 8

        def test_sumar_negativos(self):
            """Prueba la suma de dos números negativos."""
            self.assertEqual(sumar(-5, -3), -8)

        def test_sumar_cero(self):
            """Prueba la suma con cero."""
            self.assertEqual(sumar(10, 0), 10)
            self.assertEqual(sumar(0, 7), 7)

        def test_restar_basico(self):
            """Prueba la resta básica."""
            self.assertEqual(restar(10, 4), 6)

        def test_restar_resultando_negativo(self):
            """Prueba la resta que da un resultado negativo."""
            self.assertEqual(restar(5, 10), -5)

    # Esto permite ejecutar las pruebas directamente desde este archivo
    if __name__ == '__main__':
        unittest.main()
    ```

3.  **Ejecuta las pruebas:** Abre tu terminal en el directorio del proyecto y ejecuta:
    *   `python -m unittest test_calculadora_unittest.py`
    *   O si añadiste el `if __name__ == '__main__': unittest.main()`, puedes ejecutar: `python test_calculadora_unittest.py`

    Verás una salida indicando cuántas pruebas se ejecutaron y si pasaron (`OK`) o fallaron (`FAIL` o `ERROR`).

## Ejemplo Básico con `pytest`

1.  **Usa el mismo `calculadora_simple.py`** de antes.
2.  **Crea el archivo de prueba:** Guarda esto como `test_calculadora_pytest.py`. `pytest` descubre automáticamente archivos que empiezan con `test_` o terminan con `_test.py`, y funciones dentro de ellos que empiezan con `test_`.

    ```python
    # test_calculadora_pytest.py
    from calculadora_simple import sumar, restar # Importa las funciones

    # Simples funciones de prueba (empiezan con 'test_')
    def test_sumar_positivos():
        """Prueba la suma de dos números positivos."""
        resultado = sumar(5, 3)
        assert resultado == 8 # Usa 'assert' directamente

    def test_sumar_negativos():
        """Prueba la suma de dos números negativos."""
        assert sumar(-5, -3) == -8

    def test_sumar_cero():
        """Prueba la suma con cero."""
        assert sumar(10, 0) == 10
        assert sumar(0, 7) == 7

    def test_restar_basico():
        """Prueba la resta básica."""
        assert restar(10, 4) == 6

    def test_restar_resultando_negativo():
        """Prueba la resta que da un resultado negativo."""
        assert restar(5, 10) == -5

    # Pytest también puede probar métodos dentro de clases (si la clase NO hereda de unittest.TestCase)
    class TestRestaAdicional:
         def test_restar_cero(self):
             assert restar(5, 0) == 5
             assert restar(0, 5) == -5
    ```

3.  **Ejecuta las pruebas:** Abre tu terminal en el directorio del proyecto y simplemente ejecuta:
    *   `pytest`

    `pytest` buscará automáticamente todos los archivos y funciones de prueba en el directorio actual y subdirectorios y los ejecutará. La salida es a menudo más informativa y concisa que la de `unittest`.

**Buenas Prácticas Iniciales:**

*   **Nombra tus archivos de prueba** de forma clara (ej. `test_mi_modulo.py`).
*   **Nombra tus funciones/métodos de prueba** empezando con `test_`.
*   **Cada prueba debe ser independiente:** No debe depender del resultado de otra prueba.
*   **Prueba una sola cosa** en cada función/método de prueba.
*   **Usa nombres descriptivos** para tus pruebas para entender qué están verificando.
*   **Escribe pruebas para casos límite y erróneos**, no solo para el "camino feliz". (Ej. ¿qué pasa si `sumar` recibe texto en lugar de números? Podrías probar que lance un `TypeError` usando `assertRaises()` en `unittest` o `pytest.raises()` en `pytest`).

Las pruebas unitarias son una inversión que da sus frutos a largo plazo, especialmente en proyectos complejos o colaborativos. Empezar a escribirlas desde el principio es una excelente práctica de ingeniería de software.
