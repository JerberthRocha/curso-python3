"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Mutáveis (passados por referência)
  list
  set
  dict
  class (o usuário pode mudar isso)
  ...

Imutáveis (copiados)
  bool
  int
  float
  tuple
  str
  ...
  """

from __future__ import annotations
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstame: str, lastname: str) -> None:
        self.firstname = firstame
        self.lastname = lastname
        self.adresses: list[Address] = []

    def add_address(self, address: Address) -> None:
        self.adresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)

class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    joao = Person('João', 'Souza')
    endereco = Address('Rua A', '23')
    joao.add_address(endereco)

    # esposa_joao = deepcopy(joao)
    esposa_joao = joao.clone()
    esposa_joao.firstname = 'Maria'

    print(joao)
    print(esposa_joao)
