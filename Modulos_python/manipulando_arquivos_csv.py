"""
COMMA SEPARATED VALUES - CSV (VALORES SEPARADOS POR VIRGULA)
É UM FORMATO DE DADOS MUITO USADO EM TABELAS (EXCEL, GOOGLE SHEETS), BASES DE
DADOS, CLIENTES DE E-MAIL, ETC...
"""

import csv

# with open('dados_clientes.csv', 'r') as arquivo:
#     dados = csv.reader(arquivo)
#     next(dados) # PULA A PRIMEIRA LINHA POIS O ARQUIVO É UM ITERADOR

#     for dado in dados:
#         print(dado)

# with open('clientes.csv', 'r') as arquivo:
#     dados = csv.DictReader(arquivo)
#     next(dados) # TIRA A PRIMEIRA LINHA POIS O ARQUIVO É UM ITERADOR

#     for dado in dados:
#         print(dado['nome'], dado['sobrenome'], dado['E-mail'], dado['Telefone'])

with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo, 
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    # chaves = dados[0].keys()
    # chaves = list(chaves)
    # escreve.writerow(
    #     [
    #         chaves[0],
    #         chaves[1],
    #         chaves[2],
    #         chaves[3]
    #     ]
    # )

    # for dado in dados:
    #     escreve.writerow(
    #         [
    #             dado['Nome'],
    #             dado['Sobrenome'],
    #             dado['E-mail']
    #             dado['Telefone']
    #         ]
    #     )