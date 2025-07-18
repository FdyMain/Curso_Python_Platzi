import statistics
import csv

#Leer los datos de ventas mensuales desde un archivo csv
monthly_sales = {}
with open('uso_librerias/class_35_ventas/montly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#Hallar la media o promedio de los datos
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana: {median_sales}")

#Hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#Hallar la desviación estándar
stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar es: {stdev_sales}")

#Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La varianza es: {variance_sales}")

#máximo y mínimo de ventas
max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f"Rango de ventas: {range_sales}")