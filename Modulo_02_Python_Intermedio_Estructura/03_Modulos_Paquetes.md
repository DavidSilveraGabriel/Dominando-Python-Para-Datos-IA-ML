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
