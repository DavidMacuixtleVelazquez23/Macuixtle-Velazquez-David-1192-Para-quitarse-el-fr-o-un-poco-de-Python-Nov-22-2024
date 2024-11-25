def contar_vocales(palabra):
    # Lista de vocales a contar
    vocales = "aeiou"
    # Creamos un diccionario con el conteo de cada vocal
    return {vocal: palabra.lower().count(vocal) for vocal in vocales}

#Aqui se ejecuta la fucnion
palabra = input("Ingresa una palabra: ")
print("Conteo de vocales:", contar_vocales(palabra))
