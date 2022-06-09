"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
# NÃO RECOMENDADO PARA O CONCEITO DE HERANÇA PQ ALGUMAS CLASSES QUE HERDAM PRECISA TER O __init__ ALTERADO

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple

@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome:str = field(repr=False)

    def __post_init__(self): # O POST INIT É EXECUTADO LOGO APÓS O INIT
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo inválido {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('A', '5')
p2 = Pessoa('C', '4')
p3 = Pessoa('B', '3')
p4 = Pessoa('D', '2')
p5 = Pessoa('E', '1')

pessoas = [p1, p2, p3, p4, p5]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, )) # reverse=True))

# print(p1)
# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo) # UMA PROPERTY É CHAMADA SEM OS PARENTESES ()

# print(p1 == p2) # ESSA COMPARAÇÃO PODE SER FEITA PQ O MÉTODO __eq__ JÁ FOI ESCRITO PELO dataclass 

print(22 * '-=')
print(asdict(p1))
print(astuple(p2))