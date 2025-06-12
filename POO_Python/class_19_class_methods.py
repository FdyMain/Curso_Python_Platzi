class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")


persona_1 = Person("Fdy", 33)
persona_2 = Person("Adla", 3)

persona_1.greet()
persona_2.greet()

