def factorial(numero):
    if numero <0 :
        return-1
    if numero == 0:
        return 1
    if numero > 0:
        return numero * factorial(numero-1)
    
calculo_fac = factorial(38)  
print(f"factorial calculado:" +str(calculo_fac))