"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

from random import choice
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo indo buscar cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular indo buscar cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo indo buscar cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular indo buscar cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.veiculo = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.veiculo.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, 'Veículo não existe'

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'carro_popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'

if __name__ == '__main__':
    veiculos_disponiveis_zona_norte = [
        'carro_luxo', 'carro_popular', 'moto_luxo', 'moto_popular']

    print('VEÍCULOS ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()
    
    print()
    veiculos_disponiveis_zona_sul = ['carro_popular']

    print('VEÍCULOS ZONA SUL')
    for i in range(10):
        carro = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul))
        carro.buscar_cliente()
