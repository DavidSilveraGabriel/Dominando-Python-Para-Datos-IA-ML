# Ejercicios: Módulo 8 - Tipado Estático (Type Hints)

# --- Prerrequisitos ---
# Se recomienda usar un editor o IDE que soporte type hints (como VS Code con Pylance)
# y opcionalmente instalar un type checker como MyPy:
# pip install mypy

# Importar tipos necesarios del módulo typing
from typing import List, Tuple, Dict, Optional, Union, Any, Callable
import numpy as np

print("--- Tipado Estático con Type Hints ---")

# --- Ejercicio 1: Tipos Básicos y Colecciones ---
# Instrucciones:
# 1. Define una función `saludar_usuario` que tome un argumento `nombre` de tipo `str`
#    y un argumento `edad` de tipo `int`. La función debe devolver un `str`.
#    Implementa la función para que devuelva un saludo personalizado.
# 2. Define una función `procesar_puntajes` que tome una lista de enteros (`List[int]`)
#    y devuelva la suma de los puntajes (un `int`).
# 3. Define una función `obtener_coordenadas` que no tome argumentos y devuelva
#    una tupla con dos flotantes (`Tuple[float, float]`). Implementa una versión simple.
# 4. Define una función `crear_perfil` que tome un `nombre` (`str`) y un `email` (`str`)
#    y devuelva un diccionario (`Dict[str, str]`) con esas claves y valores.
# 5. Llama a cada función con tipos de datos correctos e incorrectos (puedes comentar
#    las llamadas incorrectas) y observa si tu editor/IDE te da alguna advertencia.
#    (Opcional: Ejecuta MyPy sobre este archivo para ver los errores detectados).

print("--- Ejercicio 1: Tipos Básicos y Colecciones ---")

# 1. Función saludar_usuario
def saludar_usuario(nombre: str, edad: int) -> str:
    """Genera un saludo personalizado."""
    return f"Hola, {nombre}! Veo que tienes {edad} años."

# 2. Función procesar_puntajes
def procesar_puntajes(puntajes: List[int]) -> int:
    """Calcula la suma de una lista de puntajes."""
    return sum(puntajes)

# 3. Función obtener_coordenadas
def obtener_coordenadas() -> Tuple[float, float]:
    """Devuelve coordenadas (x, y) fijas."""
    return (10.5, -3.2)

# 4. Función crear_perfil
def crear_perfil(nombre: str, email: str) -> Dict[str, str]:
    """Crea un diccionario de perfil de usuario."""
    return {"nombre": nombre, "email": email}

# 5. Llamadas a las funciones
saludo = saludar_usuario("Ana", 30)
print(f"Saludo: {saludo}")
# saludo_error = saludar_usuario("Luis", "veinte") # Error de tipo esperado por MyPy/IDE

puntajes_lista = [10, 25, 15, 30]
suma_puntajes = procesar_puntajes(puntajes_lista)
print(f"Suma de puntajes: {suma_puntajes}")
# suma_error = procesar_puntajes(["a", "b"]) # Error de tipo esperado

coords = obtener_coordenadas()
print(f"Coordenadas: {coords}")

perfil = crear_perfil("Carlos", "carlos@email.com")
print(f"Perfil: {perfil}")
# perfil_error = crear_perfil("Eva", 12345) # Error de tipo esperado

print("-" * 20)


# --- Ejercicio 2: Tipos Opcionales y Uniones ---
# Instrucciones:
# 1. Define una función `buscar_usuario(id_usuario: int)` que pueda devolver
#    un diccionario representando al usuario (`Dict[str, Any]`) si lo encuentra,
#    o `None` si no lo encuentra. Usa `Optional` para el tipo de retorno.
#    Simula la búsqueda (ej. devuelve un usuario si id_usuario == 1, sino None).
# 2. Define una función `formatear_valor(valor: Union[int, float, str])` que tome
#    un valor que puede ser entero, flotante o string, y devuelva una representación
#    en string formateada (ej. "Valor: [valor]").
# 3. Llama a `buscar_usuario` con un ID que exista y uno que no. Maneja el caso `None`.
# 4. Llama a `formatear_valor` con un entero, un flotante y un string.

print("\n--- Ejercicio 2: Tipos Opcionales y Uniones ---")

# 1. Función buscar_usuario
def buscar_usuario(id_usuario: int) -> Optional[Dict[str, Any]]:
    """Busca un usuario por ID (simulado)."""
    print(f"Buscando usuario con ID: {id_usuario}")
    if id_usuario == 1:
        return {"id": 1, "nombre": "Admin", "activo": True}
    else:
        return None

# 2. Función formatear_valor
def formatear_valor(valor: Union[int, float, str]) -> str:
    """Formatea un valor de diferentes tipos a string."""
    return f"Valor formateado: {valor}"

# 3. Llamar a buscar_usuario
usuario_encontrado = buscar_usuario(1)
if usuario_encontrado:
    print(f"Usuario encontrado: {usuario_encontrado}")
else:
    print("Usuario con ID 1 no encontrado.")

usuario_no_encontrado = buscar_usuario(5)
if usuario_no_encontrado:
    print(f"Usuario encontrado: {usuario_no_encontrado}")
else:
    print("Usuario con ID 5 no encontrado.")

# 4. Llamar a formatear_valor
print(formatear_valor(100))
print(formatear_valor(99.9))
print(formatear_valor("Hola Mundo"))
# print(formatear_valor([1, 2])) # Error de tipo esperado

print("-" * 20)


# --- Ejercicio 3: Tipado de Funciones (Callable) ---
# Instrucciones:
# 1. Define una función `aplicar_operacion(a: int, b: int, operacion: Callable[[int, int], int]) -> int`.
#    Esta función toma dos enteros y una función (`operacion`). La función `operacion`
#    debe tomar dos enteros como entrada y devolver un entero. `aplicar_operacion`
#    debe devolver el resultado de llamar a `operacion` con `a` y `b`.
# 2. Define dos funciones simples: `sumar(x: int, y: int) -> int` y `restar(x: int, y: int) -> int`.
# 3. Llama a `aplicar_operacion` pasándole `sumar` como argumento `operacion`.
# 4. Llama a `aplicar_operacion` pasándole `restar` como argumento `operacion`.
# 5. (Opcional) Intenta llamar a `aplicar_operacion` con una función que no coincida
#    con la firma esperada (ej. una lambda que devuelva un string) y observa la advertencia/error.

print("\n--- Ejercicio 3: Tipado de Funciones (Callable) ---")

# 1. Función aplicar_operacion
def aplicar_operacion(a: int, b: int, operacion: Callable[[int, int], int]) -> int:
    """Aplica una operación dada a dos números."""
    print(f"Aplicando '{operacion.__name__}' a {a} y {b}")
    return operacion(a, b)

# 2. Funciones sumar y restar
def sumar(x: int, y: int) -> int:
    return x + y

def restar(x: int, y: int) -> int:
    return x - y

# 3. Llamar con sumar
resultado_suma = aplicar_operacion(10, 5, sumar)
print(f"Resultado (suma): {resultado_suma}")

# 4. Llamar con restar
resultado_resta = aplicar_operacion(10, 5, restar)
print(f"Resultado (resta): {resultado_resta}")

# 5. Opcional: Llamada con tipo incorrecto
def operacion_incorrecta(x: int, y: int) -> str:
    return f"{x} y {y}"

# resultado_error = aplicar_operacion(10, 5, operacion_incorrecta) # Error de tipo esperado
# print(f"Resultado (error): {resultado_error}")

print("-" * 20)


# --- Ejercicio 4: Alias de Tipos ---
# Instrucciones:
# 1. Crea un alias de tipo llamado `Vector` que represente una `List[float]`.
# 2. Crea otro alias de tipo `Punto` que represente una `Tuple[float, float]`.
# 3. Define una función `calcular_distancia(p1: Punto, p2: Punto) -> float` que calcule
#    la distancia euclidiana entre dos puntos.
# 4. Define una función `normalizar_vector(v: Vector) -> Vector` que normalice un vector
#    (divida cada elemento por la magnitud del vector). Puedes calcular la magnitud
#    como la raíz cuadrada de la suma de los cuadrados de los elementos.
# 5. Usa los alias al llamar a las funciones.

print("\n--- Ejercicio 4: Alias de Tipos ---")

# 1. Alias Vector
Vector = List[float]

# 2. Alias Punto
Punto = Tuple[float, float]

# 3. Función calcular_distancia
def calcular_distancia(p1: Punto, p2: Punto) -> float:
    """Calcula la distancia euclidiana entre dos puntos."""
    dist = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    print(f"Distancia entre {p1} y {p2}: {dist:.4f}")
    return dist

# 4. Función normalizar_vector
def normalizar_vector(v: Vector) -> Vector:
    """Normaliza un vector a longitud unitaria."""
    magnitud = np.sqrt(sum(x**2 for x in v))
    if magnitud == 0:
        return [0.0] * len(v) # Evitar división por cero
    vector_normalizado = [x / magnitud for x in v]
    print(f"Vector original: {v}, Normalizado: {vector_normalizado}")
    return vector_normalizado

# 5. Usar las funciones con alias
punto1: Punto = (1.0, 2.0)
punto2: Punto = (4.0, 6.0)
distancia = calcular_distancia(punto1, punto2)

vector1: Vector = [3.0, 4.0, 0.0]
vector_norm = normalizar_vector(vector1)

print("-" * 20)

# --- Fin de los ejercicios ---
