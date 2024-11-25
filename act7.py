# Definimos una tupla con edades
edades = (15, 25, 30, 19, 22, 18, 21, 20, 35, 40)
# Contamos las personas con edad mayor a 20
mayores_20 = sum(1 for edad in edades if edad > 20)
#Aqui se ejecuta la funcion
print("Cantidad de personas mayores a 20 años:", mayores_20)
