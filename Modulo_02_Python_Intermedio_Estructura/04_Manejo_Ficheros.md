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
