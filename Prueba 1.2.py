codigo_seccion_valido = "DRY7122-003V"
codigo_seccion = input("Ingrese el código de sección (ej. DRY7122-003V): ")

if codigo_seccion == codigo_seccion_valido:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    sede = input("Sede: ")
    print("Información del alumno:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Código-sección: {codigo_seccion}")
    print(f"Sede: {sede}")
else:
    print("El código de sección ingresado no es válido.")