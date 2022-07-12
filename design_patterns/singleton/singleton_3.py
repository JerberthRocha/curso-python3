# class Meta(type):
#     def __call__(cls, *args, **kwargs) :
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)

#     def __init__(self, nome):
#         self.nome = nome

#     def __call__(self, x, y):
#         print('Chamando call', self.nome, x + y)


# if __name__ == '__main__':
#     p1 = Pessoa('Maria')
#     print(p1.nome)
#     p1(5, 5)
from typing import Dict

class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]



class AppSettings(metaclass=Singleton):
    def __init__(self):
        # O INIT SERÁ CHAMADO TODAS AS VEZES

        self.tema = 'Escuro'
        self.fonte = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Claro'

    as2 = AppSettings()
    as3 = AppSettings()
    print(as2.tema)

    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
