import csv

# Leer un archivo
#csv_reader = csv.DictReader(file) = conviernte cada fila en un dic de python
#cada fila es una lista
with open('resources/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

#Mostrar la información por columnas
with open('resources/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"El producto: {row['name']}, Precio: {row['price']}")

