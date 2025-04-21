# Ejercicios: Módulo 1 - Estructuras de Datos (Listas, Tuplas, Diccionarios, Conjuntos)

# --- Ejercicio 1: Listas ---
# Instrucciones:
# 1. Crea una lista llamada `peliculas_favoritas` que contenga tres de tus películas favoritas (como strings).
# 2. Imprime la lista completa.
# 3. Imprime la segunda película de la lista (recordando que el índice empieza en 0).
# 4. Modifica la primera película de la lista por otra que te guste. Imprime la lista modificada.
# 5. Añade una cuarta película a la lista usando `append()`. Imprime la lista final.
# 6. Elimina la segunda película de la lista usando `pop()` o `remove()`. Imprime la lista resultante.
# 7. Imprime la longitud final de la lista.

print("--- Ejercicio 1: Listas ---")
# Escribe tu código aquí
peliculas_favoritas = ["El Padrino", "Pulp Fiction", "Interestelar"]
print(f"Lista inicial: {peliculas_favoritas}")

print(f"Segunda película: {peliculas_favoritas[1]}")

peliculas_favoritas[0] = "Origen"
print(f"Lista modificada (1er elemento): {peliculas_favoritas}")

peliculas_favoritas.append("El Señor de los Anillos")
print(f"Lista con append: {peliculas_favoritas}")

pelicula_eliminada = peliculas_favoritas.pop(1) # Elimina 'Pulp Fiction' (o el que esté ahora en índice 1)
print(f"Película eliminada: {pelicula_eliminada}")
print(f"Lista después de pop(1): {peliculas_favoritas}")

print(f"Longitud final: {len(peliculas_favoritas)}")


# --- Ejercicio 2: Tuplas ---
# Instrucciones:
# 1. Crea una tupla llamada `coordenadas_gps` que contenga una latitud y una longitud (números float).
# 2. Imprime la tupla completa.
# 3. Imprime solo la latitud (el primer elemento).
# 4. Intenta modificar la longitud (el segundo elemento). Observa el error (comenta la línea que da error).
# 5. Verifica si un valor específico (ej. la latitud que pusiste) está dentro de la tupla usando `in`. Imprime el resultado.

print("\n--- Ejercicio 2: Tuplas ---")
# Escribe tu código aquí
coordenadas_gps = (-34.6037, -58.3816) # Ejemplo: Buenos Aires
print(f"Coordenadas GPS: {coordenadas_gps}")

print(f"Latitud: {coordenadas_gps[0]}")

# coordenadas_gps[1] = -58.4 # Esto dará TypeError: 'tuple' object does not support item assignment
# print(coordenadas_gps)

latitud_buscada = -34.6037
print(f"¿Está la latitud {latitud_buscada} en las coordenadas? {latitud_buscada in coordenadas_gps}")


# --- Ejercicio 3: Diccionarios ---
# Instrucciones:
# 1. Crea un diccionario llamado `info_libro` para almacenar información sobre un libro. Debe tener las claves: "titulo", "autor", "año_publicacion", "genero". Asigna valores apropiados.
# 2. Imprime el diccionario completo.
# 3. Imprime el valor asociado a la clave "autor".
# 4. Utiliza el método `get()` para obtener el valor de "genero". Imprime el resultado.
# 5. Utiliza el método `get()` para intentar obtener el valor de una clave inexistente como "editorial", proporcionando un valor por defecto "Desconocida". Imprime el resultado.
# 6. Modifica el valor de "año_publicacion" a un año diferente. Imprime el diccionario modificado.
# 7. Añade un nuevo par clave-valor: "isbn" con un valor inventado (string). Imprime el diccionario final.
# 8. Elimina el par clave-valor "genero" usando `del` o `pop()`. Imprime el diccionario resultante.
# 9. Imprime todas las claves del diccionario usando `.keys()`.
# 10. Imprime todos los valores del diccionario usando `.values()`.

print("\n--- Ejercicio 3: Diccionarios ---")
# Escribe tu código aquí
info_libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año_publicacion": 1967,
    "genero": "Realismo mágico"
}
print(f"Diccionario inicial: {info_libro}")

print(f"Autor: {info_libro['autor']}")

print(f"Género (con get): {info_libro.get('genero')}")

print(f"Editorial (con get y default): {info_libro.get('editorial', 'Desconocida')}")

info_libro["año_publicacion"] = 1968 # Corregimos si fuera necesario
print(f"Diccionario con año modificado: {info_libro}")

info_libro["isbn"] = "978-0307474728"
print(f"Diccionario con ISBN añadido: {info_libro}")

genero_eliminado = info_libro.pop("genero")
# del info_libro["genero"] # Alternativa
print(f"Género eliminado: {genero_eliminado}")
print(f"Diccionario sin género: {info_libro}")

print(f"Claves del libro: {list(info_libro.keys())}") # Convertimos a lista para verlas claramente
print(f"Valores del libro: {list(info_libro.values())}")


# --- Ejercicio 4: Conjuntos ---
# Instrucciones:
# 1. Crea un conjunto llamado `lenguajes_programacion` con los siguientes elementos (strings): "Python", "Java", "C++", "Python", "JavaScript", "Java".
# 2. Imprime el conjunto. Observa que los duplicados ("Python", "Java") han sido eliminados.
# 3. Añade el lenguaje "Ruby" al conjunto usando `add()`. Imprime el conjunto.
# 4. Intenta añadir "Python" de nuevo. Imprime el conjunto (no debería cambiar).
# 5. Elimina "C++" del conjunto usando `remove()` o `discard()`. Imprime el conjunto.
# 6. Verifica si "Java" está en el conjunto usando `in`. Imprime el resultado.
# 7. Crea un segundo conjunto `otros_lenguajes` con "Go" y "Rust".
# 8. Calcula e imprime la unión de `lenguajes_programacion` y `otros_lenguajes`.
# 9. Calcula e imprime la intersección entre `lenguajes_programacion` y `set(["Python", "Go", "C#"])`.

print("\n--- Ejercicio 4: Conjuntos ---")
# Escribe tu código aquí
lenguajes_programacion = {"Python", "Java", "C++", "Python", "JavaScript", "Java"}
print(f"Conjunto inicial: {lenguajes_programacion}")

lenguajes_programacion.add("Ruby")
print(f"Conjunto con Ruby añadido: {lenguajes_programacion}")

lenguajes_programacion.add("Python")
print(f"Conjunto tras añadir Python de nuevo: {lenguajes_programacion}")

lenguajes_programacion.discard("C++") # Usamos discard para evitar error si no existiera
print(f"Conjunto sin C++: {lenguajes_programacion}")

print(f"¿Está 'Java' en el conjunto? {'Java' in lenguajes_programacion}")

otros_lenguajes = {"Go", "Rust"}
print(f"Otros lenguajes: {otros_lenguajes}")

union_lenguajes = lenguajes_programacion.union(otros_lenguajes)
# union_lenguajes = lenguajes_programacion | otros_lenguajes # Alternativa
print(f"Unión: {union_lenguajes}")

set_interseccion = {"Python", "Go", "C#"}
interseccion = lenguajes_programacion.intersection(set_interseccion)
# interseccion = lenguajes_programacion & set_interseccion # Alternativa
print(f"Intersección con {set_interseccion}: {interseccion}")


# --- Fin de los ejercicios ---
