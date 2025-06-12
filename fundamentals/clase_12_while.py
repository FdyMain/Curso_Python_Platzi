x = 0

while x < 5:
    print("El valor de x es:", x)
    x += 1


# Ejemplo de bucle while con una condición de salida
x = 0

while x < 5:
    if x == 3:
        print("El valor de x es 3, saliendo del bucle")
        break
    print("El valor de x es:", x)
    x += 1


# Other

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i == 3:
        print("Encontré el número 3, saliendo del bucle")
        break