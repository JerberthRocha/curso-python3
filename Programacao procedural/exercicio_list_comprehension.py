string = '01234567890123456789012345678901234567890123456789'
n = 10
contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i + n) for i in range(0, len(string), n)]
linhas = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
lista = [string[i:i + n] for i in range(0, len(string), n)]
print(f'Contadores: {contadores}')
print(f'Tupla: {tuplas}')
print(f'Linhas: {linhas}')
print(f'Linha: {lista}')

retorno = '.'.join(lista)
print(retorno)
