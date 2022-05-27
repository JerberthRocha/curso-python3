# from Orientacao_a_objetos.classe_pessoa import Pessoa
# from Orientacao_a_objetos.classe_produto import Produto

# pessoa1 = Pessoa('Maria', 29)
# pessoa2 = Pessoa('José', 32)

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
# produto1 = Produto('CAMISETA', 100)
# produto1.desconto(10)
# print(produto1.nome, produto1.preco)

# produto2 = Produto('Calça', 'R$250')
# produto2.desconto(20)
# print(produto2.nome, produto2.preco)

# produto3 = Produto('Meias', 20)
# produto3.desconto(10)
# print(produto3.preco)


# ASSOCIAÇÃO
# from Orientacao_a_objetos.associacao import Escritor, MaquinaDeEscrever, Caneta


# escritor1 = Escritor('Clarisse')
# escritor2 = Escritor('Maria')

# caneta1 = Caneta('Bic')
# maquina1 = MaquinaDeEscrever()

# caneta1.ferramenta = caneta1
# caneta1.ferramenta.escrever()

# escritor2.ferramenta = maquina1
# escritor2.ferramenta.escrever()

# caneta1 = Caneta('Bic')
# print(caneta1.marca)

# maquina1 = MaquinaDeEscrever()
# maquina1.escrever()


# AGREGAÇÃO - UM TIPO DE ASSOCIAÇÃO QUE UMA CLASSE DEPENDE DA OUTRA PARA FUNCIONAR CORRETAMENTE
from Orientacao_a_objetos.agregacao import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Calça', 150)
p3 = Produto('Celular', 1250)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)

carrinho.lista_produto()

print('Valor total: ', carrinho.soma_total())
