"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as 'classes' que criam classes.
type é uma metaclasse
"""

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método')
        
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'Valor'

    def b_fala(self):
        print('Oi')

A = type(
    'A',
    (),
    {'attr':'Olá Mundo!'}
)

a = A()
print(type(a))