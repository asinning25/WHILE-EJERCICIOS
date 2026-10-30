# Saluda mientras la línea leída sea distinta de vacío ("").
def saludar():
    nombre = input("Escribe un nombre (Enter para salir): ")
    while nombre != "":
        print("Hola,", nombre)
        nombre = input("Escribe un nombre (Enter para salir): ")
    print("Hasta luego")


saludar()
