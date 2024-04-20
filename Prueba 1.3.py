def validar_acl_ipv4(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Layer 2 Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Layer 3 Estándar"
    elif numero_acl >= 1000 and numero_acl <= 1099:
        return "ACL Layer 2 Extendida"
    elif numero_acl >= 1100 and numero_acl <= 1199:
        return "ACL Layer 3 Extendida"
    else:
        return "Número de ACL no válido"

# Ejemplo de uso
numero_acl = int(input("Ingrese el número de ACL IPv4: "))
tipo_acl = validar_acl_ipv4(numero_acl)
print(f"El número de ACL IPv4 {numero_acl} corresponde a: {tipo_acl}")