#Diccionarios

informacion = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "C++"],}

print(informacion)

del informacion["edad"]  # Eliminar la clave "edad"

print(informacion)

claves = informacion.keys()  # Obtener las claves del diccionario
print(claves)
print(type(claves))

values = informacion.values()  # Obtener los valores del diccionario
print(values)
print(type(values))

pairs = informacion.items()  # Obtener los pares clave-valor del diccionario
print(pairs)

contacts = {"Carla": {"Apellido": "Gomez", "Edad": 25},
            "Luis": {"Apellido": "Perez", "Edad": 28},
            "Ana": {"Apellido": "Lopez", "Edad": 22}
            }

print(contacts)

print(contacts["Carla"])