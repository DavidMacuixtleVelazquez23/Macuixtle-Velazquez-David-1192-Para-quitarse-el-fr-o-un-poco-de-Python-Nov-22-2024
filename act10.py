def es_bisiesto(anio):
    #Aqui se hace la operacion matematica
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

#Aqui se ejecuta la funcion
anio = int(input("Ingresa un año: "))
print("¿Es bisiesto?", es_bisiesto(anio))
