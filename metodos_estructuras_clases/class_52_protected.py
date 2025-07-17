"""
Se sabe que es una variable o método protegido antes dle nombre de
#la variable o el método el _
"""

class BaseClass:

    def __init__(self):
        self._protected_variable = 'Protected'
    
    def _protected_method(self):
        print('Este es un método protegido')

base = BaseClass()
#print(base._protected_variable)
base._protected_method()