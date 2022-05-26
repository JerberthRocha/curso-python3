# SETTER: É UMA FUNÇÃO QUE VAI CONFIGURAR O VALOR DE ALGO
# GETTER: RETORNA O VALOR QUE FOI SETADO PELO SETTER
# GETTER PODE EXISTIR SEM O SETTER E PODE RETORNAR QUALQUER VALOR

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property #GETTER
    def nome(self):
        return self._nome

    @nome.setter # SETTER
    def nome(self, nome):
        print('SETTER FOI EXECUTADO')
        self._nome = nome 

p1 = Pessoa('MARIA')
print(p1.nome)

