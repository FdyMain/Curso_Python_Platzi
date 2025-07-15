def suma(a, b):
    return print(f"El resultado de la suma es: {a+b}")

def resta(a, b):
    return print("El resultado de la resta es: ", a-b)

def multiplicacion(a, b):
    return print("El resultado de la multiplicacion es: ", a*b)

def division(a, b):
    if b == 0:
        return print("Error: No es posible dividir entre cero")
    else:
        return print("El resultado de la division es: ", a/b)
    

def calculadora():
    while True:
        print("Operaciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingresa una opción: ")

        if opcion == "5":
            print("Saliendo...")
            break

        if opcion in ["1", "2", "3", "4"]:
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el primer segundo: "))

            if opcion == "1":
                suma(numero1, numero2)
            elif opcion == "2":
                resta(numero1, numero2)
            elif opcion == "3":
                multiplicacion(numero1, numero2)
            elif opcion == "4":
                division(numero1, numero2)
        else:
            print("Opción no válida")

calculadora()
                




