#variable local, solo puede ser accedida dentro de la función y no fuera de ella

def local_function():
    x = 10
    print(f'El valor de la variable es {x}')

local_function()

#variale global

x = 100
def show_global():
    print(f'el valor de la variable es {x}')


show_global()