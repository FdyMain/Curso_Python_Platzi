class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.available = True

class Inventory:
    def __init__(self):
        self.all_cars = []
        self.total = 0
    
    def add_car(self, car):
        self.all_cars.append(car)
        print("El carro ha sido agregado al inventario")
        
    def see_inventory(self):
        if self.all_cars:
            print("La lista de carros disponibles es:")
            for car in self.all_cars:
                if car.available:
                    print(f"{car.model} por valor de {car.price}")

    def see_total_seller(self):
        if self.total > 0:
            print(f"El total de ventas es: {self.total}")
        else:
            print("No se han realizado ventas")        

class Dealer:
    def __init__(self, inventory):
        self.inventory = inventory

    def sell_car(self, car):
        if car in self.inventory.all_cars:
            self.inventory.all_cars.remove(car)
            self.inventory.total += car.price
            print(f"El carro {car.model} ha sido vendido")
        else:
            print("El carro no está en el inventario")


# Crear inventario y carros
inventory = Inventory()
carro_1 = Car("Toyota", 200000000)
carro_2 = Car("Mazda", 100000000)

# Agregar carros al inventario
inventory.add_car(carro_1)
inventory.add_car(carro_2)

# Ver inventario antes de vender
inventory.see_inventory()

# Crear Dealer con acceso al inventario
dealer = Dealer(inventory)

# Vender un carro
dealer.sell_car(carro_1)

# Ver inventario después de vender
inventory.see_inventory()

# Ver total de ventas
inventory.see_total_seller()

# Vender un carro -- El carro no está en el inventario
dealer.sell_car(carro_1)
