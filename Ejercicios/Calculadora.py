
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))


suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2


if num2 != 0:
    division = num1 / num2
else:
    division = "Indefinido (no se puede dividir por cero)"


print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division}")
