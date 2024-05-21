# Creamos una lista vacía para almacenar las tareas pendientes
tareas_pendientes = []

while True:
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        # Agregar tarea
        tarea = input("Introduce la tarea que quieres agregar: ")
        tareas_pendientes.append(tarea)
        print(f"La tarea '{tarea}' ha sido agregada.")
    elif opcion == 2:
        # Mostrar tareas
        print("\nTareas pendientes:")
        for tarea in tareas_pendientes:
            print(tarea)
    elif opcion == 3:
        # Salir
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
