"""
ASSOCIAÇÃO - UM OBJETO USA UM OUTRO OBJETO
AGREGAÇÃO - UM OBJ TEM UM OUTRO OBJ
COMPOSIÇÃO - UM OBJ É DONO DE OUTRO OBJ
HERANÇA - UM OBJ É OUTRO OBJ
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} falando...')

class Cliente(Pessoa): # CLIENTE HERDA DE PESSOA
    def comprar(self):
        print(f'{self.nome_classe} comprando...')

class Aluno(Pessoa): # ALUNO HERDA DE PESSOA
    def estudar(self):
        print(f'{self.nome_classe} estudando...')