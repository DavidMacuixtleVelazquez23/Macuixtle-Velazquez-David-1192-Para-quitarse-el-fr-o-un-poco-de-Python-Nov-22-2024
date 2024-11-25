def calcular_edades():
    # Pedimos el año actual al usuario
    anio_actual = int(input("Ingresa el año en curso: "))
    # Repetimos para tres personas
    for _ in range(3):
        # Pedimos el nombre y año de nacimiento de la persona
        nombre = input("Nombre: ")
        anio_nacimiento = int(input("Año de nacimiento: "))
        # Calculamos la edad actual
        edad = anio_actual - anio_nacimiento
        # Mostramos la edad calculada
        print(f"{nombre} cumplirá {edad} años este año.")

#Aqui se ejecuta la funcion
calcular_edades()
