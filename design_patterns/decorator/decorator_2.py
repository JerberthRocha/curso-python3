"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.

Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.
Do livro "Python Fluente", por Luciano Ramalho (pág. 223)
"""

from abc import ABC
from dataclasses import dataclass
from copy import deepcopy
from typing import List

# Ingredients


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99


# Hotdogs
class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> ({self.ingredients})'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoSticks()

        ]

# Decorators


class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)


    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'



if __name__ == '__main__':
        simple_hotdog = SimpleHotdog()
        # decorated_simple_hotdog = HotdogDecorator(simple_hotdog)
        # bacon_simple_hotdog = BaconDecorator(bacon_simple_hotdog)

        print(simple_hotdog)

        bacon_simple_hotdog = HotdogDecorator(simple_hotdog,Bacon())
        egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog,Egg())
        mashed_potato_egg_bacon_simple_hotdog = HotdogDecorator(
            egg_bacon_simple_hotdog, 
            MashedPotatoes()
        )

        print(bacon_simple_hotdog)
        print(egg_bacon_simple_hotdog)
        print(mashed_potato_egg_bacon_simple_hotdog)


    # special_hotdog = SpecialHotdog()
    # print(special_hotdog)