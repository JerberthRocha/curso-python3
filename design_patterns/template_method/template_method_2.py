"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredients()
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()
        self.cook()  # Abstract
        self.cut()  # Concrete
        self.serve()  # Concrete

    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'Cortando a pizza {self.__class__.__name__}')

    def serve(self) -> None:
        print(f'Servindo a pizza {self.__class__.__name__}')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('Fazendo algo antes de adicionar os ingredientes')

    def add_ingredients(self) -> None:
        print('Adicionando ingredientes presunto, queijo')

    def cook(self) -> None:
        print('Assando pizza: 45 minutos no forno')


class Mussarela(Pizza):
    def add_ingredients(self) -> None:
        print('Adicionando ingredientes queijo, queijo e mais queijo')

    def hook_after_add_ingredients(self) -> None:
        print('Fazendo algo após adicionar os ingredientes')

    def cook(self) -> None:
        print('Assando pizza: 25 minutos no forno')


if __name__ == '__main__':
    pizza_1 = AModa()
    pizza_1.prepare()

    print()

    pizza_2 = Mussarela()
    pizza_2.prepare()
