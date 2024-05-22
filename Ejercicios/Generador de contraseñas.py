import random
import string


longitud = int(input(""))


caracteres = string.ascii_letters + string.digits + string.punctuation


contrasena = ''.join(random.choice(caracteres) for i in range(longitud))


print(f"Tu contraseña aleatoria es: {contrasena}")
