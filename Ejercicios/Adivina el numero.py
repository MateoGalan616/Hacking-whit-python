import random


numero_aleatorio = random.randint(1, 100)


print("He generado un número aleatorio entre 1 y 100. ¿Puedes adivinarlo?")
while True:
    numero_usuario = int(input("Introduce un número: "))
    
    
    if numero_usuario < numero_aleatorio:
        print("Demasiado bajo. Intenta de nuevo.")
    elif numero_usuario > numero_aleatorio:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Correcto! Has adivinado el número.")
        break
