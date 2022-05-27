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

class ClienteVip(Cliente): # TEM TUDO DAS CLASSES PESSOA E CLIENTE
    def __init__(self, nome, sobrenome, idade): # SOBREPOSIÇÃO DE CONSTRUTOR
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        super().falar() # CHAMA O MÉTODO falar() DA SUPER CLASSE
        print('método falar sobreposto')
        print(f'{self.nome} {self.sobrenome}')
    
    # def comprar(self):
    #     print(f'{self.nome_classe} comprando pq sou vip...')