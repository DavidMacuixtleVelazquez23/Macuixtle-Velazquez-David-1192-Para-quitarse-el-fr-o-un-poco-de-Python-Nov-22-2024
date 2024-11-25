def filtrar_palabras(palabras, n):
    # Devolvemos una lista con palabras que tengan más de n caracteres
    return [palabra for palabra in palabras if len(palabra) > n]

# Aqui se ejecuta la funcion
print(filtrar_palabras(["hola", "mundo", "python", "programación"], 5))  
