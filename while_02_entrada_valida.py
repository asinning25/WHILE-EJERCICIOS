# Espera una entrada válida (un entero) y cuenta los intentos inválidos.
def pedir_entero_valido():
    intentos_invalidos = 0
    while True:
        texto = input("Introduce un número entero: ")
        if texto.lstrip("-").isdigit():
            return int(texto)
        intentos_invalidos += 1
        print("Entrada inválida. Intentos inválidos hasta ahora:", intentos_invalidos)


numero = pedir_entero_valido()
print("Ingresaste:", numero)
