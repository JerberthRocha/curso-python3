class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.enderecos = []

    @property # GETTER 
    def nome(self):
        return self.__nome
    
    @nome.setter # SETTER
    def nome(self, nome):
        self.__nome = nome

    @property # GETTER 
    def idade(self):
        return self.__idade

    @idade.setter # SETTER
    def idade(self, idade):
        self.__idade = idade
    
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    
    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado