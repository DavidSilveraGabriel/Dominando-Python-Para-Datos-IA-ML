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
