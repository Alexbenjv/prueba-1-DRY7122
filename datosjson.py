import json
from datetime import datetime, timedelta  # Agrega "timedelta" a los módulos importados

# Ruta del archivo JSON
file_path = "/home/devasc/Documents/myfile.json"

# Abre el archivo JSON
with open(file_path, "r") as json_file:
    # Carga el archivo JSON en un diccionario
    data = json.load(json_file)

    # Obtiene el valor del access_token
    access_token = data["access_token"]
    print(f"Access Token: {access_token}")

    # Obtiene la fecha de expiración del access_token
    expires_in = data["expires_in"]
    expiration_date = datetime.now() + timedelta(seconds=expires_in)
    # Calcula cuánto tiempo falta para la expiración
    remaining_time = expiration_date - datetime.now()
    print(f"Tiempo restante antes de la caducidad del access_token: {remaining_time}")

