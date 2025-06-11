try:
    divisor = int(input("Ingresa un num divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("El divisor no puede ser cero", e)
except ValueError:
    print("Error: Debes introducir un número válido")



print("Continue...")