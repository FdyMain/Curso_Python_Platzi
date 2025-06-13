num_lineas = 0
with open('resources/cuento.txt', 'r') as file:
    for lineas in file:
        num_lineas +=1
        print(lineas.strip())

print(f"La cantidad de lineas es {num_lineas}")


