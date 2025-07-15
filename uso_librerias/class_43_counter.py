from collections import Counter


def count_sales(products: list[str]) -> Counter:
    #Usa Counter para contar cuántos productos de cada tipo se han vendido
    return Counter(products)

sales = ['laptop', 'smart', 'smart', 'laptop', 'tablet']
result = count_sales(sales)
print(result) 