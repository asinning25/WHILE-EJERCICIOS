# Muestra una a una las letras de la palabra, empezando por la última.
palabra = input("Introduce una palabra: ")

i = len(palabra) - 1
while i >= 0:
    print(palabra[i])
    i -= 1
