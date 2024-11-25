def mas_larga(palabras):
    # Usamos max() con key=len para encontrar la palabra más larga
    return max(palabras, key=len)

# Prueba
print(mas_larga(["yo", "zoe", "bosho", "pepe"]))  # Debería imprimir "bicicleta"
