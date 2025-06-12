## Comprenssion List

# Calcular los elevado al cuadrado del 1 al 10
squares = [x**2 for x in range(1,11)]
print("Los cuadrados son: ", squares)


# Mostrar los grados celsius en fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
print("Temperatura en F: ", fahrenheit)

#Hallar los pares 
evens = [x for x in range(1,21) if x%2 == 0]
print(evens)

#Hallar los impares 
evens = [x for x in range(1,21) if x%2 == 1]
print(evens)

#Transponer la matriz
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
print(matriz)
print(transposed)