
#Leer archivo línea por línea
"""
with open('resources/cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())
'''
"""


#Leer todas las líneas en una lista

"""
with open('resources/cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
'''
"""

#Añadir texto al final
"""
with open('resources/cuento.txt', 'a') as file:
    file.write("\n\nBy Platzi")

with open('resources/cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())

'''        
"""


#Sobre escribir el texto de todo el archivo
with open('resources/cuento_sobreescribir.txt', 'w') as file:
    file.write("\n\nBy Platzi")

with open('resources/cuento_sobreescribir.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())





