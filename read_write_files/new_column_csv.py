import csv

file_path = 'resources/products.csv'
update_file_path = 'resources/products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(update_file_path, mode='w', newline='') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            try:
                price = float(row['price'])
                quantity = int(row['quantity'])
                row['total_value'] = price * quantity
            except (ValueError, KeyError):
                row['total_value'] = 'ERROR'
            csv_writer.writerow(row)
