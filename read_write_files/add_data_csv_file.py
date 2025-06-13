import csv

new_product = {
    'name': 'Cocina',
    'price': 75,  # corregido el campo
    'quantity': 100,
    'brand': 'Corona',
    'category': 'Utils',
    'entry_date': '2025-07-12'
}

# Primero escribimos (modo append)
with open('resources/products.csv', mode='a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)

# Luego leemos (modo read)
with open('resources/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)