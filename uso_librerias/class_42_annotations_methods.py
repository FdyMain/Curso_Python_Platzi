def divide(a: int, b: int) -> float:
    return a/b

print(divide(10,2))

def divide_2(a: int, b: int) -> float:
    #validar qe ambos parámetros sean enternos int
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('ambos parámetros deben ser int or float')
        #print('Error: ambos parámetros deben ser int or float')
        #return None
    #verificamos que el divisor no sea 0
    if b==0:
        raise TypeError('El divisor no puede ser 0')
        #print('Error: El divisor no puede ser 0')
        #return None
    
    
    return a/b

res_1 = divide_2(10,'2')
res_2 = divide_2(10,0)
res_3 = divide_2(10,2)
print(res_3)


#Ejemplo de uso

try: 
    res = divide_2(10 , '2') # Error de type
    print(res)
except TypeError as e:
    print(f'Error: {e}')