numbers = [1,2,3,4,5,6]

#Instrucción for
for i in numbers:
    print("El valor de i es:",i)

#Ejemplo sumando a i 
for i in numbers:
    print("El valor de i + 1 es:", i + 1 )


for i in range(10):
    print("El valor de i es:", i)

for i in range(3,10):
    print("El valor de i es:", i)

#For con IF

fruits = ["manzana", "banana", "cereza", "durazno"]

for fruit in fruits:
    print("La fruta es:", fruit)
    if fruit == "banana":
        print("Encontré una banana")