# Módulo 8: Tipado Estático (Type Hinting)

Python es tradicionalmente un lenguaje de **tipado dinámico**. Esto significa que no necesitas declarar el tipo de una variable explícitamente; el tipo se determina en tiempo de ejecución cuando asignas un valor.

```python
# Tipado dinámico
mi_variable = 10       # Python infiere que es int
print(type(mi_variable))
mi_variable = "hola"   # Ahora es str
print(type(mi_variable))
```

Si bien esto ofrece flexibilidad, también puede llevar a errores que solo se descubren en tiempo de ejecución (ej. intentar sumar un número y un string).

Desde Python 3.5 (con PEP 484), se introdujeron las **Type Hints (Indicaciones de Tipo)**. Estas permiten **anotar** el tipo esperado de variables, parámetros de función y valores de retorno.

**¡Importante!** Las type hints son **opcionales** y **no son verificadas por el intérprete de Python en tiempo de ejecución** por defecto. Python sigue siendo dinámicamente tipado. El propósito principal de las type hints es:

1.  **Mejorar la Legibilidad y Documentación:** Hacen más claro qué tipo de datos se espera que maneje una función o variable.
2.  **Análisis Estático:** Permiten usar herramientas externas llamadas **verificadores de tipos estáticos** (como **MyPy**, Pyright, Pytype) para analizar tu código *antes* de ejecutarlo y detectar posibles errores de tipo.
3.  **Mejor Soporte del Editor (IDE):** Los editores como VS Code usan las type hints para ofrecer mejor autocompletado, refactorización y detección de errores mientras escribes.

## Sintaxis Básica de Type Hints

*   **Variables:** Usa dos puntos (`:`) después del nombre de la variable, seguido del tipo.
    ```python
    edad: int = 30
    nombre: str = "Alice"
    precio: float = 19.99
    activo: bool = True
    ```
    *Nota: La asignación del valor sigue siendo necesaria.*

*   **Parámetros de Función:** Usa dos puntos (`:`) después del nombre del parámetro, seguido del tipo.
*   **Valor de Retorno de Función:** Usa una flecha (`->`) después de los paréntesis de los parámetros, seguido del tipo de retorno esperado. Si la función no devuelve nada explícitamente (devuelve `None`), usa `-> None`.

    ```python
    def saludar(nombre: str) -> None:
        """Saluda a alguien (con type hints)."""
        print(f"Hola, {nombre}")

    def sumar(a: int, b: int) -> int:
        """Suma dos enteros y devuelve un entero."""
        return a + b

    def procesar_datos(datos: list[float]) -> float: # Hint para lista de floats
        """Calcula la media de una lista de floats."""
        if not datos:
            return 0.0
        return sum(datos) / len(datos)

    # Llamadas
    saludar("Bob")
    resultado_suma = sumar(5, 3)
    media = procesar_datos([1.0, 2.5, 3.0])

    print(f"Resultado suma: {resultado_suma}")
    print(f"Media: {media}")
    ```

## Tipos Complejos (Módulo `typing`)

Para tipos más complejos (listas de un tipo específico, diccionarios, tuplas, opcionales, etc.), se utiliza el módulo `typing` de la biblioteca estándar.

```python
from typing import List, Tuple, Dict, Set, Optional, Union, Any, Callable

# Listas de un tipo específico
nombres: List[str] = ["Ana", "Luis", "Eva"]
puntos: list[Tuple[int, int]] = [(1, 2), (3, 4)] # Sintaxis moderna (Python 3.9+)

# Tuplas con tipos específicos para cada elemento
coordenada: Tuple[float, float, str] = (10.5, -3.2, "origen")
# O con número variable de elementos del mismo tipo
numeros_tupla: Tuple[int, ...] = (1, 2, 3, 4)

# Diccionarios (clave, valor)
edades: Dict[str, int] = {"Ana": 30, "Luis": 25}
config: dict[str, Union[str, int, bool]] = {"host": "localhost", "port": 8080, "debug": True} # Python 3.9+

# Conjuntos
ids_unicos: Set[int] = {101, 102, 103}

# Valores Opcionales (puede ser del tipo especificado o None)
# Útil para valores por defecto o retornos que pueden ser None
def buscar_usuario(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Admin"
    # Si no se encuentra, devuelve None implícitamente
    return None

usuario: Optional[str] = buscar_usuario(1)
no_encontrado: Optional[str] = buscar_usuario(99)
print(f"\nUsuario encontrado: {usuario}")
print(f"Usuario no encontrado: {no_encontrado}")

# Unión de Tipos (puede ser uno de varios tipos)
identificador: Union[int, str] = "ID-123"
identificador = 456

# Cualquier Tipo (Any) - Usar con moderación, pierde beneficios del tipado
# Útil para código muy dinámico o al interactuar con bibliotecas sin tipos.
variable_dinamica: Any = 10
variable_dinamica = "texto"

# Tipos Callable (para funciones)
# Callable[[lista de tipos de argumento], tipo de retorno]
def aplicar(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

resultado_aplicar = aplicar(lambda a, b: a * b, 5, 6)
print(f"\nResultado de aplicar: {resultado_aplicar}")

# Type Aliases (Alias de Tipo)
# Para tipos complejos o repetitivos
Vector = List[float]
Coordenadas = Tuple[float, float]

def norma(v: Vector) -> float:
    return sum(x*x for x in v)**0.5

punto: Coordenadas = (3.0, 4.0)
vector_ejemplo: Vector = [1.0, 2.0, 3.0]
print(f"\nNorma del vector: {norma(vector_ejemplo)}")
```
*Nota: Desde Python 3.9+, puedes usar los tipos genéricos incorporados directamente (ej. `list[int]`, `dict[str, float]`) en lugar de importar `List`, `Dict`, etc., desde `typing`.*

## Verificación Estática con MyPy

Como se mencionó, Python no verifica los tipos en tiempo de ejecución. Para aprovechar las type hints para la detección de errores, necesitas un verificador de tipos estático como **MyPy**.

1.  **Instalación:** `pip install mypy` o `conda install mypy`
2.  **Ejecución:** Abre tu terminal en el directorio de tu proyecto y ejecuta:
    ```bash
    mypy tu_archivo.py
    ```
    O para verificar todos los archivos en un directorio:
    ```bash
    mypy tu_directorio/
    ```

MyPy analizará tu código usando las type hints y reportará cualquier inconsistencia o error de tipo que encuentre.

**Ejemplo de Error Detectado por MyPy:**

```python
# archivo_con_error_tipo.py
def duplicar(numero: int) -> int:
    return numero * 2

resultado: int
resultado = duplicar(5)
print(resultado)

# Error intencional: pasar un string a una función que espera int
resultado_error = duplicar("hola") # MyPy detectará esto
print(resultado_error)
```

Al ejecutar `mypy archivo_con_error_tipo.py`, MyPy mostraría un error similar a:
`archivo_con_error_tipo.py:9: error: Argument 1 to "duplicar" has incompatible type "str"; expected "int"  [arg-type]`

**Beneficios:**

*   Detecta errores comunes (pasar tipos incorrectos, llamar métodos inexistentes) *antes* de ejecutar el código.
*   Mejora la robustez y fiabilidad del código, especialmente en proyectos grandes.
*   Sirve como documentación precisa y verificable.

Adoptar type hints es una práctica moderna en Python que, aunque opcional, mejora significativamente la calidad, mantenibilidad y robustez del código, especialmente en el contexto de proyectos complejos como los de ciencia de datos y desarrollo de software.
