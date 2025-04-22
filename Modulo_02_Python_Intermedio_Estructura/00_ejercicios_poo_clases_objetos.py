# Ejercicios: Módulo 2 - POO - Clases y Objetos

# --- Ejercicio 1: Definición de Clase y Creación de Objetos ---
# Instrucciones:
# 1. Define una clase llamada `Coche`.
# 2. En el método `__init__`, la clase debe aceptar tres argumentos: `marca`, `modelo` y `año`.
# 3. Dentro de `__init__`, asigna estos argumentos a atributos de instancia con los mismos nombres.
# 4. Añade un atributo de instancia llamado `kilometraje` inicializado en 0.
# 5. Crea dos objetos (instancias) de la clase `Coche` con diferentes marcas, modelos y años.
# 6. Imprime la marca, modelo y año de cada coche creado.

print("--- Ejercicio 1: Definición de Clase y Creación de Objetos ---")

# Escribe tu código aquí
class Coche:
    """Representa un coche con marca, modelo, año y kilometraje."""
    def __init__(self, marca, modelo, año):
        """Inicializa los atributos del coche."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0 # Inicializamos el kilometraje

# Creación de objetos
coche1 = Coche("Toyota", "Corolla", 2021)
coche2 = Coche("Ford", "Mustang", 2022)

# Impresión de atributos
print(f"Coche 1: Marca={coche1.marca}, Modelo={coche1.modelo}, Año={coche1.año}")
print(f"Coche 2: Marca={coche2.marca}, Modelo={coche2.modelo}, Año={coche2.año}")


# --- Ejercicio 2: Métodos de Instancia ---
# Instrucciones:
# 1. Añade un método llamado `mostrar_info` a la clase `Coche` del ejercicio anterior.
#    Este método debe imprimir una cadena formateada con toda la información del coche
#    (marca, modelo, año y kilometraje).
# 2. Añade otro método llamado `conducir` que reciba un argumento `km`.
#    Este método debe incrementar el `kilometraje` del coche por la cantidad `km` dada
#    y luego imprimir un mensaje como "Conduciendo [km] km. Kilometraje actual: [nuevo kilometraje]".
#    Asegúrate de que los km sean positivos antes de incrementar.
# 3. Llama al método `mostrar_info` para ambos coches creados en el ejercicio 1.
# 4. Llama al método `conducir` para el `coche1` con una distancia de 150 km.
# 5. Llama al método `conducir` para el `coche2` con una distancia de 80 km.
# 6. Vuelve a llamar a `mostrar_info` para ambos coches para ver el kilometraje actualizado.

print("\n--- Ejercicio 2: Métodos de Instancia ---")

# Reescribimos la clase Coche con los nuevos métodos
class Coche:
    """Representa un coche con marca, modelo, año y kilometraje."""
    def __init__(self, marca, modelo, año):
        """Inicializa los atributos del coche."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0

    def mostrar_info(self):
        """Muestra la información completa del coche."""
        print(f"Info Coche: {self.marca} {self.modelo} ({self.año}) - Kilometraje: {self.kilometraje} km")

    def conducir(self, km):
        """Simula la conducción, incrementando el kilometraje."""
        if km > 0:
            self.kilometraje += km
            print(f"Conduciendo {km} km. Kilometraje actual: {self.kilometraje} km")
        else:
            print("La distancia a conducir debe ser positiva.")

# Recreamos los objetos (o podríamos modificar la clase anterior si estuviéramos en un entorno interactivo)
coche1 = Coche("Toyota", "Corolla", 2021)
coche2 = Coche("Ford", "Mustang", 2022)

# Llamadas a mostrar_info inicial
print("Información inicial:")
coche1.mostrar_info()
coche2.mostrar_info()

# Llamadas a conducir
print("\nRealizando viajes:")
coche1.conducir(150)
coche2.conducir(80)
coche1.conducir(50) # Otro viaje para coche1
coche2.conducir(-10) # Intento de viaje negativo

# Llamadas a mostrar_info final
print("\nInformación final:")
coche1.mostrar_info()
coche2.mostrar_info()


# --- Ejercicio 3: Atributos de Clase ---
# Instrucciones:
# 1. Define una clase llamada `Producto`.
# 2. Añade un atributo de clase llamado `impuesto` con un valor de 0.16 (representando el 16% de IVA/impuesto).
# 3. En el `__init__`, la clase debe aceptar `nombre` y `precio_base`.
# 4. Añade un método llamado `calcular_precio_final` que calcule y devuelva el precio
#    incluyendo el impuesto (precio_base * (1 + impuesto)). Accede al impuesto usando `self.impuesto` o `Producto.impuesto`.
# 5. Crea dos instancias de `Producto` con diferentes nombres y precios base.
# 6. Llama a `calcular_precio_final` para cada producto e imprime el resultado formateado.
# 7. Intenta cambiar el `impuesto` directamente desde la clase (`Producto.impuesto = 0.18`) y vuelve a calcular
#    el precio final de uno de los productos para ver si el cambio se refleja.

print("\n--- Ejercicio 3: Atributos de Clase ---")

# Escribe tu código aquí
class Producto:
    """Representa un producto con nombre, precio base y un impuesto de clase."""
    # Atributo de clase
    impuesto = 0.16

    def __init__(self, nombre, precio_base):
        """Inicializa el producto."""
        self.nombre = nombre
        self.precio_base = precio_base

    def calcular_precio_final(self):
        """Calcula el precio final incluyendo el impuesto de clase."""
        # Se puede acceder con self.impuesto o Producto.impuesto
        precio_final = self.precio_base * (1 + Producto.impuesto)
        # precio_final = self.precio_base * (1 + self.impuesto) # También funciona
        return precio_final

# Creación de instancias
producto1 = Producto("Laptop", 1200)
producto2 = Producto("Teclado", 80)

# Cálculo de precios iniciales
print(f"Precio final {producto1.nombre}: ${producto1.calcular_precio_final():.2f} (Impuesto: {Producto.impuesto*100}%)")
print(f"Precio final {producto2.nombre}: ${producto2.calcular_precio_final():.2f} (Impuesto: {Producto.impuesto*100}%)")

# Cambiamos el impuesto a nivel de clase
print("\nCambiando impuesto a 18%...")
Producto.impuesto = 0.18

# Recalculamos precios
print(f"Nuevo precio final {producto1.nombre}: ${producto1.calcular_precio_final():.2f} (Impuesto: {Producto.impuesto*100}%)")
print(f"Nuevo precio final {producto2.nombre}: ${producto2.calcular_precio_final():.2f} (Impuesto: {Producto.impuesto*100}%)")


# --- Fin de los ejercicios ---
