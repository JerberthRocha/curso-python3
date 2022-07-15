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


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation_1()
        self.operation_2()
        self.base_class_method()

    def base_class_method(self):
        print('Esse método pertence a classe abstract')

    def hook(self): pass

    @abstractmethod
    def operation_1(self): pass

    @abstractmethod
    def operation_2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Utilizando o método hook')
    def operation_1(self):
        print('Operação 1 concluida (ConcreteClass1)')

    def operation_2(self):
        print('Operação 2 concluida (ConcreteClass1)')


class ConcreteClass2(Abstract):
    def operation_1(self):
        print('Operação 1 concluida (ConcreteClass2)')

    def operation_2(self):
        print('Operação 2 concluida (ConcreteClass2)')


if __name__ == '__main__':
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
