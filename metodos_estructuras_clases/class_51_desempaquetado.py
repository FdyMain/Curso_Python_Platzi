#Desempaquetado de args
def suma(a,b,c):
    return a+b+c

values = (1,2,3)
print(suma(*values))

def show_info(name,age):
    print(f'name: {name}, Age: {age}')

data = {'name': 'Ana', 'age': 28}
show_info(**data)