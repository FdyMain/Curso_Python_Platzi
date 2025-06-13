import json

#Lectura del archivo
with open('resources/products.json', mode='r') as file:
    products = json.load(file)

#Mostrar la información del archivo
for product in products:
    #print(product)
    print(f"Producto: {product['name']}, Price: {product['price']}")

