class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @idade.setter
    def idade(self, nome):
        self._idade = nome

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def inserir_conta(self, conta):
        self.conta = conta