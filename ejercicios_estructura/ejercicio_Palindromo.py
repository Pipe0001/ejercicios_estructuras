def Palindromo(palabra):

  if len(palabra) <=1:
    return True

  if palabra[0] == palabra[-1]:
    return Palindromo(palabra[1:-1])
  else:
    return False

Palabra1 = "rayar"
Palabra2 = "solos"
Palabra3 = "Jugar"

print(f"La palabra: {Palabra1} es un palindromo ? : {Palindromo(Palabra1)}")
print(f"La palabra: {Palabra2} es un palindromo ? : {Palindromo(Palabra2)}")
print(f"La palabra: {Palabra3} es un palindromo ? : {Palindromo(Palabra3)}")