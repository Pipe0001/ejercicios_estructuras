def contar_digitos(numero, digitos):
    if numero <10:
        return digitos +1
    else:
        return contar_digitos(numero//10,digitos+1)
    
print(contar_digitos(12345,0))
