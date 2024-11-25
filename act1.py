def max_in_list(lista):
    # Inicializamos el máximo con el primer elemento de la lista
    maximo = lista[0]
    # Recorremos la lista para encontrar el mayor número
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

#aqui se ejecuta la funcion
print(max_in_list([3, 7, 2, 8, 4]))  
