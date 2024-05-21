import os

# Ruta del archivo
archivo = 'colaboradores.txt'

# Función para leer los colaboradores desde el archivo
def leer_colaboradores():
    if not os.path.exists(archivo):
        return []
    with open(archivo, 'r') as f:
        colaboradores = f.read().splitlines()
    return colaboradores

# Función para mostrar los colaboradores
def mostrar_colaboradores(num_colaboradores=5):
    colaboradores = leer_colaboradores()
    for i, colaborador in enumerate(colaboradores[:num_colaboradores], start=1):
        print(f"{i}. {colaborador}")

# Función para agregar un nuevo colaborador
def agregar_colaborador(nuevo_colaborador):
    colaboradores = leer_colaboradores()
    if len(colaboradores) >= 15:
        print("No se puede agregar más colaboradores. El límite es de 15.")
        return
    
    if nuevo_colaborador not in colaboradores:
        colaboradores.append(nuevo_colaborador)
        with open(archivo, 'w') as f:
            f.write('\n'.join(colaboradores))
        print(f"Colaborador '{nuevo_colaborador}' agregado exitosamente.")
    else:
        print(f"El colaborador '{nuevo_colaborador}' ya está en la lista.")

# Función principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar colaboradores")
        print("2. Agregar colaborador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            num_colaboradores = input("Ingrese el número de colaboradores a mostrar (por defecto 5): ")
            if num_colaboradores.strip() == '':
                num_colaboradores = 15
            else:
                num_colaboradores = int(num_colaboradores)
            mostrar_colaboradores(num_colaboradores)
        
        elif opcion == '2':
            nuevo_colaborador = input("Ingrese el nombre del nuevo colaborador: ")
            agregar_colaborador(nuevo_colaborador)
        
        elif opcion == '3':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el script
if __name__ == "__main__":
    main()
