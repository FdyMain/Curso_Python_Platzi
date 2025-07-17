def suma(a: int, b: int):
    return a+b

def resta(a: int, b: int):
    return a-b

def multiplicacion(a: int, b: int):
    return a*b

def division(a: int, b: int):
    if b==0:
        raise ValueError('No se puede dividir en cero')
    return a/b


if __name__ == '__main__':
    print('Operaciones')
    res_1 = suma(3,4)
    print(f'Suma: {res_1}')
    print(division(10,7))