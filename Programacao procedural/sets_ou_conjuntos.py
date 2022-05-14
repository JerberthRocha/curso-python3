# O Set/Conjuntos é um tipo de dado bastante peculiar do Python que possui as seguintes características:
# - Sets são desordenados
# - Não possuem elementos duplicados, ou seja, cada elemento é único.
# - Um set em si pode ser modificado, contudo os elementos contidos dentro dele precisam ser de tipos imutáveis.
# criando um set
# set_1 = {1, 2, 3}
#
# print(set_1)
# for v in set_1:
#     print(v)
#
# # criando um set vazio
# set_2 = set()
# # adicionando valor
# set_2.add(5)
# set_2.add(6)
# print(set_2)
#
# # removendo valor
# set_1.discard(2)
# print(set_1)
#
# set_2.update('Python')  # o update itera sobre a string informada
# print(set_2)
# set_2.add('Python')
# print(set_2)

set_3 = {1, 2, 3, 4, 5}
set_4 = {1, 2, 6, 4, 7}
set_5 = set_3 | set_4  # union (|) faz a união dos dois conjuntos
print(set_5)

set_6 = set_3 & set_4  # intersection (&) pega os elementos que estão presentes nos dois conjuntos
print(set_6)

set_7 = set_3 - set_4  # difference (-) pega os elementos que estão somente no set da esquerda
print(set_7)

set_8 = set_3 ^ set_4  # symmetric difference (^) pega os elementos exclusivos de cada conjunto
print(set_8)

nomes_lista = ['Maria', 'Ana', 'Carol', 'João', 'Maria', 'Ana', 'Carol', 'João', 'Maria', 'Carol', 'João', 'José']
print(nomes_lista)

nomes_conjuntos = set(nomes_lista)
print(nomes_conjuntos)

nomes_lista = list(nomes_conjuntos)
print(nomes_lista)
