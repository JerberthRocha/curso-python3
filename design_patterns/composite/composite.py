"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    # Component

    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    # Composite

    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self.children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self.children
        ])

    def add(self, child: BoxStructure) -> None:
        self.children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self.children:
            self.children.remove(child)


class Product(BoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price

if __name__ == '__main__':
    # Leaf
    camisa_1 = Product('Camisa 01', 45)
    camisa_2 = Product('Camisa 02', 35)
    camisa_3 = Product('Camisa 03', 20)

    # Composite
    caixa_camisetas = Box('Caixa de camisetas')
    caixa_camisetas.add(camisa_1)
    caixa_camisetas.add(camisa_2)
    caixa_camisetas.add(camisa_3)

    # Leaf
    smartphone_1 = Product('smartphone 1', 2450)
    smartphone_2 = Product('smartphone 2', 7550)

    # Composite
    caixa_smartphones = Box('Caixas de Smatphones')
    caixa_smartphones.add(smartphone_1)
    caixa_smartphones.add(smartphone_2)
    
    # Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()

    print(caixa_grande.get_price())