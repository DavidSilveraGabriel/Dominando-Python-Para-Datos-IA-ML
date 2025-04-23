# Ejercicios: Módulo 8 - Concurrencia y Paralelismo

# --- Prerrequisitos ---
# Conocimientos básicos de funciones, clases.
# No se requieren instalaciones adicionales para threading y multiprocessing.
# Para asyncio, viene con Python 3.5+.

import threading
import time
import multiprocessing
import asyncio
import random

print("--- Concurrencia y Paralelismo ---")

# --- Función de Tarea Simulada ---
# Usaremos esta función para simular una tarea que toma tiempo
def tarea_simulada(nombre_tarea, duracion):
    print(f"[{nombre_tarea}] Iniciando tarea (duración: {duracion}s)...")
    time.sleep(duracion)
    resultado = f"Resultado de {nombre_tarea}"
    print(f"[{nombre_tarea}] Tarea finalizada.")
    return resultado

# --- Ejercicio 1: Ejecución Secuencial (Base) ---
# Instrucciones:
# 1. Llama a `tarea_simulada` dos veces de forma secuencial:
#    - Tarea "A" con duración 2 segundos.
#    - Tarea "B" con duración 1 segundo.
# 2. Mide y imprime el tiempo total que tarda la ejecución secuencial. Usa `time.perf_counter()`.

print("--- Ejercicio 1: Ejecución Secuencial ---")
# Escribe tu código aquí
tiempo_inicio_sec = time.perf_counter()

print("Iniciando ejecución secuencial...")
resultado_a_sec = tarea_simulada("Sec-A", 2)
resultado_b_sec = tarea_simulada("Sec-B", 1)
print(f"Resultados secuenciales: {resultado_a_sec}, {resultado_b_sec}")

tiempo_fin_sec = time.perf_counter()
duracion_sec = tiempo_fin_sec - tiempo_inicio_sec
print(f"\nDuración total secuencial: {duracion_sec:.4f} segundos")
print("-" * 20)


# --- Ejercicio 2: Concurrencia con `threading` ---
# Instrucciones:
# 1. Importa el módulo `threading`.
# 2. Crea dos objetos `Thread`, uno para cada llamada a `tarea_simulada` (Tarea "TA" con 2s, Tarea "TB" con 1s). Pasa los argumentos usando `args`.
# 3. Inicia ambos hilos usando el método `.start()`.
# 4. Espera a que ambos hilos terminen usando el método `.join()`.
# 5. Mide y imprime el tiempo total de ejecución. ¿Es significativamente menor que la suma de las duraciones individuales (2+1=3s)? ¿Por qué? (Comenta la respuesta).

print("\n--- Ejercicio 2: Concurrencia con `threading` ---")
# Escribe tu código aquí
# 1. Importar (hecho al principio)

tiempo_inicio_th = time.perf_counter()
print("Iniciando ejecución con hilos...")

# 2. Crear hilos
hilo_a = threading.Thread(target=tarea_simulada, args=("Hilo-A", 2), name="Hilo A")
hilo_b = threading.Thread(target=tarea_simulada, args=("Hilo-B", 1), name="Hilo B")

# 3. Iniciar hilos
hilo_a.start()
hilo_b.start()

# 4. Esperar a que terminen
print("Esperando a que los hilos terminen...")
hilo_a.join()
hilo_b.join()
print("Hilos terminados.")

tiempo_fin_th = time.perf_counter()
duracion_th = tiempo_fin_th - tiempo_inicio_th
print(f"\nDuración total con hilos: {duracion_th:.4f} segundos")

# 5. Comentario sobre la duración
# Respuesta: Sí, el tiempo total (~2s) es significativamente menor que la suma (3s).
# Esto se debe a que los hilos ejecutan las tareas de forma *concurrente*. Mientras una tarea
# está "dormida" (time.sleep), el GIL (Global Interpreter Lock) de Python se libera
# (en operaciones de I/O como sleep o espera de red), permitiendo que el otro hilo se ejecute.
# No es verdadero paralelismo (ejecución simultánea en múltiples cores para CPU-bound),
# pero es efectivo para tareas limitadas por I/O (I/O-bound).

print("-" * 20)


# --- Ejercicio 3: Paralelismo con `multiprocessing` ---
# Instrucciones:
# 1. Importa el módulo `multiprocessing`.
# 2. Crea dos objetos `Process`, uno para cada llamada a `tarea_simulada` (Tarea "PA" con 2s, Tarea "PB" con 1s).
# 3. **Importante:** En algunos sistemas (especialmente Windows), el código que crea procesos debe estar dentro de `if __name__ == "__main__":`. Asegúrate de que tu script principal lo incluya si es necesario.
# 4. Inicia ambos procesos usando `.start()`.
# 5. Espera a que ambos procesos terminen usando `.join()`.
# 6. Mide y imprime el tiempo total de ejecución. Compara con los resultados anteriores. ¿Esperarías una mejora significativa respecto a `threading` para esta tarea específica (`time.sleep`)? (Comenta la respuesta).

print("\n--- Ejercicio 3: Paralelismo con `multiprocessing` ---")
# Escribe tu código aquí (dentro del if __name__ == "__main__")

def ejecutar_multiprocessing():
    tiempo_inicio_mp = time.perf_counter()
    print("Iniciando ejecución con procesos...")

    # 2. Crear procesos
    proceso_a = multiprocessing.Process(target=tarea_simulada, args=("Proc-A", 2))
    proceso_b = multiprocessing.Process(target=tarea_simulada, args=("Proc-B", 1))

    # 4. Iniciar procesos
    proceso_a.start()
    proceso_b.start()

    # 5. Esperar a que terminen
    print("Esperando a que los procesos terminen...")
    proceso_a.join()
    proceso_b.join()
    print("Procesos terminados.")

    tiempo_fin_mp = time.perf_counter()
    duracion_mp = tiempo_fin_mp - tiempo_inicio_mp
    print(f"\nDuración total con procesos: {duracion_mp:.4f} segundos")

    # 6. Comentario sobre la duración
    # Respuesta: El tiempo total (~2s) será similar al de threading para esta tarea específica.
    # `time.sleep` es una operación I/O-bound donde el GIL se libera, permitiendo la concurrencia
    # efectiva con hilos. Multiprocessing introduce una sobrecarga mayor por la creación de procesos
    # separados. La ventaja real de multiprocessing se vería en tareas *CPU-bound* (cálculos intensivos),
    # donde podría ejecutarlas en paralelo en diferentes núcleos de CPU, superando la limitación del GIL.

if __name__ == "__main__":
    # 3. Código dentro del bloque main
    ejecutar_multiprocessing()
    print("-" * 20)

    # --- Ejercicio 4: Concurrencia con `asyncio` ---
    # Instrucciones:
    # 1. Importa el módulo `asyncio`.
    # 2. Define una *corutina* (función `async def`) llamada `tarea_async(nombre_tarea, duracion)` que:
    #    a. Imprima un mensaje de inicio.
    #    b. Use `await asyncio.sleep(duracion)` para simular la espera no bloqueante.
    #    c. Imprima un mensaje de finalización y devuelva un resultado.
    # 3. Define una corutina principal `main_async()` que:
    #    a. Cree dos tareas (futures) a partir de `tarea_async` usando `asyncio.create_task()`.
    #    b. Espere a que ambas tareas completen usando `await asyncio.gather()`.
    #    c. Imprima los resultados obtenidos de `gather`.
    # 4. Ejecuta la corutina `main_async` usando `asyncio.run(main_async())`.
    # 5. Mide y imprime el tiempo total de ejecución. Compara con los métodos anteriores.

    print("\n--- Ejercicio 4: Concurrencia con `asyncio` ---")
    # Escribe tu código aquí

    # 2. Definir corutina
    async def tarea_async(nombre_tarea, duracion):
        print(f"[{nombre_tarea}] Iniciando tarea async (duración: {duracion}s)...")
        await asyncio.sleep(duracion) # Espera no bloqueante
        resultado = f"Resultado de {nombre_tarea}"
        print(f"[{nombre_tarea}] Tarea async finalizada.")
        return resultado

    # 3. Definir corutina principal
    async def main_async():
        tiempo_inicio_async = time.perf_counter()
        print("Iniciando ejecución con asyncio...")

        # a. Crear tareas
        task_a = asyncio.create_task(tarea_async("Async-A", 2))
        task_b = asyncio.create_task(tarea_async("Async-B", 1))

        # b. Esperar y recolectar resultados
        print("Esperando a que las tareas async terminen...")
        resultados = await asyncio.gather(task_a, task_b)
        print("Tareas async terminadas.")

        # c. Imprimir resultados
        print(f"Resultados async: {resultados}")

        tiempo_fin_async = time.perf_counter()
        duracion_async = tiempo_fin_async - tiempo_inicio_async
        print(f"\nDuración total con asyncio: {duracion_async:.4f} segundos")
        # Debería ser similar a threading (~2s) para esta tarea I/O-bound.

    # 4. Ejecutar la corutina main
    asyncio.run(main_async())
    print("-" * 20)

# --- Fin de los ejercicios ---
