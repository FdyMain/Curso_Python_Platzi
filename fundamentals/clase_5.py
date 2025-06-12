x = 10 #int
y = 5.678 #float
z = 1.2e6 
a = 1.2e-6
print(type(x))
print(type(y))
print(z)
print(a)

print(x + x)
print(x + y)
print(y + y)

is_true = True #Boolean / Bool
is_false = False

print(is_true)
print(type(is_true))

#str example of print, con la coma separa argumentos, más no los concatena
print("Nunca","Pares","de","aprender")

# sep, la forma en la que quiero que se separen los argumentos
# en este ejemplo imprime "Nunca: Pares: de: aprender"
print("Nunca","Pares","de","aprender", sep=": ")

#end garantiza que se elimine el salto de línea
print("Nunca", end=" ")
print("pares de aprender")

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#Uso de f
frase = "Nunca pares de aprender"
author = "Platzi"

print(f"Frase: {frase}, Author: {author}")

#Uso de format
print("Frase: {}, Author: {}".format(frase, author))


#Formato a los decimales
valor = 3.14159
print("Valor: {:.2f}".format(valor))

#Saltos de línea
print("Hola\nmundo")

#Comillas
print("Hola soy \'Fdy\'")