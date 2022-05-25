from Orientacao_a_objetos.classe_pessoa import Pessoa
from Orientacao_a_objetos.classe_produto import Produto

pessoa1 = Pessoa('Maria', 29)
pessoa2 = Pessoa('José', 32)

# pessoa1.comer('pizza')
# pessoa1.falar('POO')
# pessoa1.parar_de_comer()
# pessoa1.comer('pizza')
# pessoa2.comer('sorvete')
# pessoa2.parar_de_comer()
# pessoa1.parar_de_comer()
# pessoa2.falar('futsal')
# pessoa1.falar('futebol')
# pessoa1.comer('carne')
# pessoa2.comer('pipoca')
# pessoa1.parar_de_falar()
# pessoa2.parar_de_falar()

# print(pessoa1)
# print(pessoa1.nome, pessoa1.idade)
# pessoa1.get_ano_nascimento()

# @PROPERTY - GETTERS e SETTERS 
produto1 = Produto('CAMISETA', 100)
produto1.desconto(10)
print(produto1.nome, produto1.preco)

produto2 = Produto('Calça', 'R$250')
produto2.desconto(20)
print(produto2.nome, produto2.preco)

produto3 = Produto('Meias', 20)
produto3.desconto(10)
print(produto3.preco)
