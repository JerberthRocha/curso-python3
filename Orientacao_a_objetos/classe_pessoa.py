from random import randint

class Pessoa:
    ano_atual = 2022 # ATRIBUTO DA CLASSE
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def get_ano_nascimento(self): # MÉTODO DE INSTÂNCIA
        print(self.ano_atual - self.idade)

    @classmethod # MÉTODO DA CLASSE
    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod # MÉTODO ESTÁTICO - NÃO UTILIZA CLASSE NEM INSTÂNCIA
    def gera_id():
        rand = randint(10000, 19999)
        return rand

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False
