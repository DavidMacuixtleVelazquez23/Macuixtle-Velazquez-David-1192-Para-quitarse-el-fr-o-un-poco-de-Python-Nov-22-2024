def contar_nombres_con_letra(nombres, letra):
    # Contamos cuántos nombres empiezan con la letra dada
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

#aqui se ejcuta la funcion
nombres = ["Boshi", "Zoe", "Andrian", "Puga", "Escobedo", "ximena"]
#aqui se te pide qeu ingreses una letra
letra = input("Ingresa la letra a buscar: ")
print("Cantidad de nombres que comienzan con", letra, ":", contar_nombres_con_letra(nombres, letra))
