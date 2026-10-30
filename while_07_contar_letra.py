# Cuenta cuántas veces aparece una letra en una frase.
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

frase = frase.lower()
letra = letra.lower()

contador = 0
i = 0
while i < len(frase):
    if frase[i] == letra:
        contador += 1
    i += 1

print("La letra", letra, "aparece", contador, "veces")
