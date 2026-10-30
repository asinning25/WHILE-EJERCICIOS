# Genera números de Fibonacci hasta superar 100.
a = 0
b = 1

while a <= 100:
    print(a)
    a, b = b, a + b
