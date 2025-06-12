a = [1,2,3,4,5]
b = a.copy()  
#Tambien se puede usar b = a[:] para copiar la lista

print("Lista a:", a)
print("Lista b:", b)

b.append(6)
print("Lista a:", a)
print("Lista b:", b)

