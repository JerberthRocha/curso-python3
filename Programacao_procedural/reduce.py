from dados_para_o_map import produtos, pessoas, lista
from functools import reduce

# recude -> (acumulador, item: acumulador + item, lista, valor inicial do acumulador)

soma_lista = reduce(lambda total, preco_produto: total + preco_produto, lista, 0)
soma_precos = reduce(lambda acumulador, item: acumulador + item['preco'], produtos, 0)
soma_idades = reduce(lambda acumula_idade, pessoa: acumula_idade + pessoa['idade'], pessoas, 0)
print(soma_lista)
print(soma_precos)
print(soma_idades / len(pessoas))
