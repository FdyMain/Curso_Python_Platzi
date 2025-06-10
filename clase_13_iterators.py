#Iterator

#Crear una lista de números

my_list = [1, 2, 3, 4, 5]

#Crear un iterador a partir de la lista
my_iterator = iter(my_list)
#Usar el iterador para recorrer la lista
print(next(my_iterator))  # Imprime 1
print(next(my_iterator))  # Imprime 2
print(next(my_iterator))  # Imprime 3
print(next(my_iterator))  # Imprime 4
print(next(my_iterator))  # Imprime 5
print(next(my_iterator))  # No imprime ya que la lista no tiene más elementos