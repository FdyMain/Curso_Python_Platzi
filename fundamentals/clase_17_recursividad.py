#Para hallar el factorial de:
# 5! = 5*4*3*2*1
# 4! = 4*3*2*1
# Podemos usar recursividad para hallar los factoriales así:
# 5! = 5*4   (esto significa que el factorial de 5 es igual al de 5 por el factorial de 4)
# 4! = 4*3

#Esto en Python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

factorial_5 = factorial(5)
print(factorial_5)



#finonacci

def fibonacci(n):
    if n == 0:
        return(0)
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = 4
print(fibonacci(number))

#Calcular la suma de número naturales a partir de un número dado

def natural_numbers(n):
    if n == 0:
        return (0)
    elif n == 1:
        return (1)
    else:
        return n + natural_numbers(n-1)
    
num = 2
print(natural_numbers(num))