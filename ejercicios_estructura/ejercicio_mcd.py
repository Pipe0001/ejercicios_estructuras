def mcd_recursivo(a, b):
    
    if b == 0:
        return a  
    else:
        return mcd_recursivo(b, a % b)  

a = 48
b = 18
resultado = mcd_recursivo(a, b)
print(f"El MCD de {a} y {b} es: {resultado}")  