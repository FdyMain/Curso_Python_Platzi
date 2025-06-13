import json

new_product = {
    'name': 'Cocina',
    'price': 75,  # corregido el campo
    'quantity': 100,
    'brand': 'Corona',
    'category': 'Utils',
    'entry_date': '2025-07-12'
}


#Agregar un objeto al final del json

with open('resources/products.json', mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open('resources/products.json', mode='w') as file:
    json.dump(products, file, indent=4)
 