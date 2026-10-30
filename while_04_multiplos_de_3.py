# Recibe dos enteros a y b e imprime cuántos múltiplos de 3 hay entre ellos (inclusive).
def contar_multiplos_de_3(a, b):
    # Si a es mayor que b, se intercambian para que el ciclo funcione.
    if a > b:
        a, b = b, a

    cantidad = 0
    i = a
    while i <= b:
        if i % 3 == 0:
            cantidad += 1
        i += 1          # el incremento va FUERA del if, siempre se ejecuta
    return cantidad


a = int(input("Introduce a: "))
b = int(input("Introduce b: "))
print("Hay", contar_multiplos_de_3(a, b), "múltiplos de 3 entre", a, "y", b)
