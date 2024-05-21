import os
import fnmatch
# Define las extensiones de archivos sensibles
sensitive_extensions = ['*.db', '*.sql', '*.key', '*.pem']

# Función para listar archivos sensibles
def list_sensitive_files(directory):
    sensitive_files = []
    for root, dirs, files in os.walk(directory):
        for extension in sensitive_extensions:
            for filename in fnmatch.filter(files, extension):
                sensitive_files.append(os.path.join(root, filename))
    return sensitive_files

# Directorio a escanear
directory_to_scan = '/path/to/your/directory'

# Llamar a la función y obtener los archivos sensibles
sensitive_files = list_sensitive_files(directory_to_scan)

# Imprimir los archivos encontrados
for file in sensitive_files:
    print(file)
