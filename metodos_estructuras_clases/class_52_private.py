"""
Se sabe que es una variable o método protegido antes dle nombre de
#la variable o el método el _
"""

class BaseClass:

    def __init__(self):
        self._protected_variable = 'Protected'
        self.__private_variable = 'Private'
    
    def _protected_method(self):
        print('Este es un método protegido')

    def __private_method(self):
        print('Esto es un método privado')

    def public_method(self):
        self.__private_method()

base = BaseClass()

#En este caso el método aunque es público se ejecuta porque ese método está dentro de la clase que llama al método privado
base.public_method()

#Como la variavle es provada no puedo acceder desde afuera de la clase
#Ejempo: print(base.__private_variable)
