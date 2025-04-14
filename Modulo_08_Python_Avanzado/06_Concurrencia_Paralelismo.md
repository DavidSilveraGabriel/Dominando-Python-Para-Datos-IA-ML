# Módulo 8: (Opcional) Introducción a Concurrencia y Paralelismo

A medida que las aplicaciones se vuelven más complejas o necesitan manejar tareas que consumen tiempo (como operaciones de red, acceso a disco o cálculos intensivos), surge la necesidad de ejecutar múltiples tareas "al mismo tiempo" para mejorar el rendimiento o la capacidad de respuesta. Aquí es donde entran los conceptos de **concurrencia** y **paralelismo**.

**Nota:** Este es un tema complejo y esta es solo una introducción muy básica a los conceptos y herramientas disponibles en Python.

## Concurrencia vs. Paralelismo

Aunque a menudo se usan indistintamente, no son lo mismo:

*   **Concurrencia (Concurrency):** Se refiere a la capacidad de un sistema para **manejar múltiples tareas superponiendo sus tiempos de ejecución**, aunque no necesariamente se ejecuten *exactamente* en el mismo instante. El sistema puede cambiar rápidamente entre tareas, dando la *ilusión* de simultaneidad. El objetivo principal suele ser mejorar la **respuesta** de la aplicación (ej. que la interfaz de usuario no se bloquee mientras se descarga un archivo).
*   **Paralelismo (Parallelism):** Se refiere a la capacidad de un sistema para ejecutar **múltiples tareas *literalmente* al mismo tiempo**, utilizando múltiples unidades de procesamiento (ej. múltiples núcleos de CPU o múltiples máquinas). El objetivo principal suele ser **acelerar** cálculos intensivos dividiendo el trabajo.

**Analogía:**
*   **Concurrencia:** Un cocinero haciendo malabares con varias ollas en una sola estufa (cambia rápidamente entre ellas).
*   **Paralelismo:** Varios cocineros trabajando cada uno en su propia estufa al mismo tiempo.

## El GIL (Global Interpreter Lock) en CPython

Antes de hablar de las herramientas de Python, es crucial mencionar el **GIL**. En CPython (la implementación más común de Python), el Global Interpreter Lock es un mutex (un bloqueo) que protege el acceso a los objetos de Python, permitiendo que **solo un hilo (thread) ejecute bytecode de Python a la vez** dentro de un único proceso, incluso en máquinas con múltiples núcleos de CPU.

*   **Consecuencia:** Los hilos (`threading`) en CPython son excelentes para la **concurrencia** (especialmente para tareas **ligadas a E/S - I/O-bound**), pero **no logran verdadero paralelismo** para tareas **ligadas a la CPU (CPU-bound)**, ya que solo un hilo puede ejecutar código Python en un momento dado.

## Herramientas de Python para Concurrencia/Paralelismo

1.  **`threading` (Módulo Incorporado):**
    *   **Concepto:** Permite crear múltiples **hilos** de ejecución dentro del **mismo proceso**. Comparten la misma memoria.
    *   **Uso Principal:** **Concurrencia para tareas ligadas a E/S (I/O-bound)**. Mientras un hilo está esperando una operación lenta de E/S (ej. respuesta de red, lectura de disco), el GIL se libera y otro hilo puede ejecutar código Python. Esto mejora la capacidad de respuesta.
    *   **Limitación (CPython):** Debido al GIL, no acelera tareas ligadas a la CPU en máquinas multinúcleo.
    *   **Gestión:** Requiere cuidado con la sincronización (usando `Lock`, `Semaphore`, `Event`, etc.) si múltiples hilos acceden y modifican datos compartidos para evitar condiciones de carrera (race conditions).

    ```python
    import threading
    import time

    def tarea_hilo(nombre, duracion):
        print(f"Hilo {nombre}: Iniciando...")
        time.sleep(duracion) # Simula trabajo (ej. I/O)
        print(f"Hilo {nombre}: Terminando.")

    # Crear hilos
    hilo1 = threading.Thread(target=tarea_hilo, args=("A", 2))
    hilo2 = threading.Thread(target=tarea_hilo, args=("B", 1))

    print("Lanzando hilos...")
    hilo1.start() # Inicia la ejecución del hilo 1
    hilo2.start() # Inicia la ejecución del hilo 2

    print("Hilos lanzados. Esperando a que terminen...")
    hilo1.join() # Espera a que el hilo 1 termine
    hilo2.join() # Espera a que el hilo 2 termine
    print("Todos los hilos han terminado.")
    # Notarás que los mensajes de inicio/fin pueden intercalarse.
    ```

2.  **`multiprocessing` (Módulo Incorporado):**
    *   **Concepto:** Permite crear **múltiples procesos** del sistema operativo. Cada proceso tiene su propio intérprete de Python y su propio espacio de memoria (y su propio GIL).
    *   **Uso Principal:** **Paralelismo para tareas ligadas a la CPU (CPU-bound)**. Como cada proceso se ejecuta de forma independiente, pueden ejecutarse en diferentes núcleos de CPU simultáneamente, logrando verdadero paralelismo y acelerando cálculos intensivos.
    *   **Limitación:** La comunicación entre procesos es más compleja y lenta que entre hilos (requiere mecanismos como `Queue`, `Pipe`, memoria compartida) porque no comparten memoria directamente. Crear procesos tiene más sobrecarga que crear hilos.

    ```python
    import multiprocessing
    import time
    import os

    def tarea_proceso(nombre):
        pid = os.getpid() # Obtener ID del proceso
        print(f"Proceso {nombre} (PID: {pid}): Iniciando...")
        # Simular trabajo intensivo de CPU
        resultado = 0
        for i in range(10**7):
            resultado += i
        print(f"Proceso {nombre} (PID: {pid}): Terminando. Resultado={resultado}")

    if __name__ == "__main__": # Necesario en algunos SO para multiprocessing
        print("\nLanzando procesos...")
        proceso1 = multiprocessing.Process(target=tarea_proceso, args=("A",))
        proceso2 = multiprocessing.Process(target=tarea_proceso, args=("B",))

        proceso1.start()
        proceso2.start()

        print("Procesos lanzados. Esperando...")
        proceso1.join()
        proceso2.join()
        print("Todos los procesos han terminado.")
        # Si tienes múltiples núcleos, verás que terminan más rápido que si se ejecutaran secuencialmente.
    ```

3.  **`asyncio` (Módulo Incorporado - Python 3.4+):**
    *   **Concepto:** Framework para escribir código **concurrente** usando la sintaxis **`async`/`await`**. Se basa en un **bucle de eventos (event loop)** y **coroutines** (funciones especiales definidas con `async def`). Es **monohilo (single-threaded)**.
    *   **Uso Principal:** **Concurrencia de alto nivel para tareas ligadas a E/S (I/O-bound)**, especialmente operaciones de red (servidores web, clientes API, etc.). Es muy eficiente manejando miles de conexiones concurrentes.
    *   **Funcionamiento:** Cuando una coroutine encuentra una operación `await` (que normalmente es una operación de E/S que tomaría tiempo), cede el control al bucle de eventos, permitiendo que otras coroutines se ejecuten mientras la primera espera. Cuando la operación de E/S se completa, el bucle de eventos reanuda la coroutine que estaba esperando. Es **multitarea cooperativa**.
    *   **Limitación:** No proporciona paralelismo para tareas CPU-bound (porque es monohilo). Requiere bibliotecas compatibles con `asyncio` para las operaciones de E/S.

    ```python
    import asyncio
    import time

    async def tarea_async(nombre, duracion):
        print(f"Async {nombre}: Iniciando, esperando {duracion}s...")
        await asyncio.sleep(duracion) # Simula I/O no bloqueante
        print(f"Async {nombre}: Terminado.")
        return f"Resultado de {nombre}"

    async def main():
        print("\nLanzando tareas asyncio...")
        # Crear tareas (coroutines envueltas)
        tarea1 = asyncio.create_task(tarea_async("X", 2))
        tarea2 = asyncio.create_task(tarea_async("Y", 1))
        tarea3 = asyncio.create_task(tarea_async("Z", 3))

        print("Tareas creadas. Esperando resultados...")
        # Esperar a que todas las tareas terminen y obtener resultados
        resultado1, resultado2, resultado3 = await asyncio.gather(tarea1, tarea2, tarea3)
        print("Todas las tareas asyncio han terminado.")
        print(f"Resultados: {resultado1}, {resultado2}, {resultado3}")

    # Ejecutar la función principal async
    if __name__ == "__main__":
        # En scripts, se usa asyncio.run()
        # En Jupyter, a veces se necesita manejo especial del bucle de eventos
        # o usar 'await main()' directamente si el notebook lo soporta (ej. IPython 7+)
        try:
            asyncio.run(main())
        except RuntimeError as e:
            print(f"Nota: Es posible que necesites ejecutar 'await main()' directamente en un entorno como Jupyter. Error: {e}")

    ```

**¿Cuándo usar qué?**

*   **`threading`:** Para concurrencia I/O-bound si no necesitas paralelismo real o si interactúas con código C que libera el GIL durante el bloqueo. Más simple para compartir datos (con cuidado).
*   **`multiprocessing`:** Para paralelismo CPU-bound real en máquinas multinúcleo. La comunicación entre procesos es más costosa.
*   **`asyncio`:** Para concurrencia I/O-bound de alto rendimiento, especialmente con muchas operaciones de red. Requiere un estilo de programación diferente (`async`/`await`) y bibliotecas compatibles.

La concurrencia y el paralelismo son temas avanzados pero esenciales para construir aplicaciones Python eficientes y escalables.
