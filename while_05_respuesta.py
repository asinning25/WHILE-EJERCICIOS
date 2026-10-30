# Respuesta al punto 5: ¿hay casos en que el programa del punto 4 se ejecuta
# indefinidamente o no se ejecuta correctamente?
#
# SÍ, dependiendo de cómo se escriba:
#
# 1) Ejecución indefinida: si el incremento (i += 1) se escribe DENTRO del if,
#    cuando i no es múltiplo de 3 nunca aumenta y el ciclo no termina.
#
#        while i <= b:
#            if i % 3 == 0:
#                cantidad += 1
#                i += 1      # ERROR: si i no es múltiplo de 3, i no cambia
#
# 2) No funciona correctamente: si a > b, la condición i <= b es falsa desde el
#    inicio, el ciclo no se ejecuta y el programa muestra 0, aunque sí haya
#    múltiplos entre los dos números. Se corrige intercambiando a y b.
#
# 3) Si el usuario escribe algo que no es un entero (por ejemplo "hola"),
#    int() produce un error y el programa se detiene.
#
# En while_04_multiplos_de_3.py estos casos están resueltos.
print("Revisa los comentarios de este archivo: contienen la respuesta al punto 5.")
