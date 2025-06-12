class BankAccounts:
    def __init__(self,client, total):
        self.client = client
        self.total = total
        self.is_active = True

    def add_money(self,amount):
        if self.is_active:
            self.total += amount
            print(f"Se ha agregado {amount} de forma exitosa, salto total: {self.total}")
        else:
            print("La cuenta está inactiva, no es posible realizar el depósito")

    def out_money(self, amount):
        if self.is_active and amount <= self.total:
            self.total -= amount
            print(f"Se ha retirado {amount}, saldo total es: {self.total}")
        else:
            print("No es posible realizar el retiro, cuenta inactiva")

    def active_account(self):
        if self.is_active == False:
            self.is_active = True
            print("La cuenta ha sido activada")
        else:
            print("No es posible activar, la cuenta ya está activa")
    
    def inactive_account(self):
        if self.is_active == True:
            self.is_active = False
            print("La cuenta ha sido desactivada")
        else:
            print("No es posible desactivar, la cuenta ya está inactiva")





person_1 = BankAccounts("Fdy", 500)
person_1.add_money(200)
person_1.active_account()
person_1.inactive_account()

person_1.add_money(100)
person_1.out_money(50)
person_1.active_account()
person_1.out_money(50)

    
