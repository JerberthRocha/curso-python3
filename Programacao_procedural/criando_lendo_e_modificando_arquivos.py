# https://docs.python.org/3/library/functions.html#open
# file = open('arquivo.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# file.seek(0, 0)
# print('Lendo linhas:')
# print(file.read())
#
# print(15 * '-=')
#
# file.seek(0, 0)
# print(file.readline())
# print(file.readline())
# print(file.readline())
#
# print(15 * '-=')
#
# file.seek(0, 0)
# for linha in file.readlines():
#     print(linha)
#
# file.close()

# try:
#     file = open('arquivo.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

# MELHOR FORMA DE SE TRABALHAR COM ARQUIVO EM PYTHON

# with open('arquivo.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())

# with open('arquivo.txt', 'r') as file:
#     print(file.read())

# with open('arquivo.txt', 'a') as file:
#     file.write('Linha 5\n')
#
# import os
# os.remove('arquivo.txt')
import json

d1 = {
    'pessoa1':{
        'nome': 'ana',
        'idade': 25
    },'pessoa2':{
        'nome': 'Jhon',
        'idade': 22
    },
}


d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('arquivo.json', 'w+') as file:
    file.write(d1_json)