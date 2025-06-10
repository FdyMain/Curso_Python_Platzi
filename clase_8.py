to_do = ["Dirigirnos al hotel",
         "Almorzar",
         "Visitar el museo",
         "Cenar"]

print("Lista de actividades:", to_do)

numbers = [1,2,3,4, "cinco"]
print("Lista de números:", type(numbers))

mix = ["uno", 2,3.14, True, [1,2,3]]
print("Lista mixta:", mix)
print(len(mix))
print("Primer elemento de la lista mixta:", mix[0])
print("Segundo elemento de la lista mixta:", mix[1])
print("último elemento de la lista mixta:", mix[-1])

string = "Hola mundo"
print("Primer elemento de la lista mixta:", string[0])
print("Segundo elemento de la lista mixta:", string[1])
print("último elemento de la lista mixta:", string[-1])

print(mix[0:2])  # Imprime los elementos del índice 0 al 1
print(mix[2:])  # Imprime los elementos desde la posición 2 hasta el final

#Agregar elementos a la lista
mix.append(False)
print("Lista mixta después de agregar un elemento:", mix) #Agrega elemento al final de la lista
mix.append(["a","b"])
print("Lista mixta después de agregar una lista:", mix) #Agrega una lista al final de la lista


#Insertar elementos en una posición específica
mix.insert(1,["a","b"])
print("Lista mixta después de insertar una lista en la posición 1:", mix) 
#Consultar la posición de un elemento
print(mix.index(["a","b"]))

#Calcular el mayor y menor de una lista de números
numbers_1 = [1.2, 2, 3, 4, 5, 6, 100.01, 90.45, 9.1]
print("Número mayor:", max(numbers_1))
print("Número menor:", min(numbers_1))

#Eliminar un elemento de la lista
del numbers_1[-1]
print(numbers_1)

#Eliminar una porción de la lista
del numbers_1[:2]
print("Lista después de eliminar los dos primeros elementos:", numbers_1)

#Eliminar toda la lista
del numbers_1
print("Lista numbers_1 eliminada.", numbers_1)

