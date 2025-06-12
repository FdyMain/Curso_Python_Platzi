class BanckAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")

    def withdraw(self, amount):
        if self.is_active and amount <= self.balance:
            self.balance -= amount
            print(f"Se ha retirado {amount}. El saldo es: {self.balance}")

    def desactive_account(self):
        if self.is_active:
            self.is_active = False
            print("La cuenta ha sido desactivada")
        else:
            print("La cuenta ya está inactiva")

    def active_account(self):
        if self.is_active == False:
            self.is_active = True
            print("La cuenta ha sido activada")
        else:
            print("La cuenta ya está Activa")


account_1 = BanckAccount("Ana", 500)
account_2 = BanckAccount("Luis", 1000)

#Llamada a los métodos

account_1.deposit(200)
account_2.deposit(100)

account_1.desactive_account()
account_1.deposit(50)

account_1.active_account()
account_1.withdraw(50)
        
                
