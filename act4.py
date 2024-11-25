def contar_mayusculas(cadena):
    # Contamos las letras mayúsculas en la cadena usando sum()
    return sum(1 for letra in cadena if letra.isupper())

#Aqui se ejcutqa la funcion
cadena = input("Ingresa una cadena: ")
print("Cantidad de mayúsculas:", contar_mayusculas(cadena))
