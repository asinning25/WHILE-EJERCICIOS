# Lee dos enteros a y b e imprime los primeros b múltiplos de a.
a = int(input("Introduce a: "))
b = int(input("Introduce b: "))

contador = 1
while contador <= b:
    print(a * contador)
    contador += 1
