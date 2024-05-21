import random
import string

# Solicitamos la longitud de la contraseña al usuario
longitud = int(input(""))

# Definimos los caracteres que se pueden usar en la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

# Generamos la contraseña
contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

# Imprimimos la contraseña
print(f"Tu contraseña aleatoria es: {contrasena}")
