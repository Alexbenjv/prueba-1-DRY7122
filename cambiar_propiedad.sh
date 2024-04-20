#!/bin/bash

# Cambiar la propiedad del archivo a root
sudo chown root:root $0

# Dar permisos de ejecución al archivo
chmod +x $0

echo "Propiedad del archivo cambiada a root y permisos de ejecución otorgados."

