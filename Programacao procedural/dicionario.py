# import copy

# d1 = {
#     'chave1': 'valor1',
#     'chave2': 'valor2',
#     'chave3': 'valor3'
# }
#
# # FORMAS DE ATUALIZAR E CRIAR VALORES DENTRO DO DICIONÁRIO
# d1['chave4'] = 'valor4'
# d1.update({'chave4': 'valor5'})
# print(d1)
#
# if d1.get('chave5'):
#     print(d1.get('chave5'))
#
# print('chave1' in d1)
# print('chave1' in d1.keys())
# print('valor' in d1.values())
#
# print(len(d1))
#
# for k, v in d1.items():
#     print(k, v)
# print()
# print('CHAVES')
# for keys in d1.keys():
#     print(keys, end=' ')
# print()
# print()
# print('VALORES')
# for values in d1.values():
#     print(values, end=' ')

# clientes = {
#     'cliente1': {
#         'nome': 'Maria',
#         'sobrenome': 'Rocha'
#     },
#     'cliente2': {
#         'nome': 'José',
#         'sobrenome': 'Silva'
#     },
#     'cliente3': {
#         'nome': 'Ana',
#         'sobrenome': 'Pereira'
#     }
# }
#
# for cliente_chave, cliente_valor in clientes.items():
#     print(f'Dados do {cliente_chave}')
#     for chave_cliente, valor_cliente in cliente_valor.items():
#         print(f'\t{chave_cliente} = {valor_cliente}')
#
# # FAZENDO UMA CÓPIA PROFUNDA DE UM DICIONÁRIO
# para_copiar = {1: 'a', 2: 'b', 3: 'c', 'd': ['Maria', 'José']}
# copia = copy.deepcopy(para_copiar)
# # copia = para_copiar.copy() - CÓPIA RASA
# copia[1] = 'Novo'
# copia['d'][0] = 'João'
# print(para_copiar)
# print(copia)
para_concat = {
    4: 'd',
    5: 'e',
    6: 'f',
}

d1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
}
print(f'DICIONÁRIO COMPLETO: {d1}')

d1.pop(5)  # apaga o item especificado por parâmetro
print()
print(f'DICIONÁRIO APÓS A FUNÇÃO pop: {d1}')

d1.popitem()  # apaga sempre o último item do dicionário
print()
print(f'DICIONÁRIO APÓS A FUNÇÃO popitem: {d1}')

print()
d1.update(para_concat)
print(f'DICIONÁRIO APÓS A FUNÇÃO CONCATENAÇÃO: {d1}')
