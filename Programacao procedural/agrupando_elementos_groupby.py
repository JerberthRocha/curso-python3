from itertools import groupby, tee

#  tee faz cópias do iterador

alunos = [
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Carla', 'nota': 'B'},
    {'nome': 'José', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Maignan', 'nota': 'A'},
    {'nome': 'Tomori', 'nota': 'A'},
    {'nome': 'Mariana', 'nota': 'A'},
    {'nome': 'Ana Carla', 'nota': 'C'},
    {'nome': 'Luiza', 'nota': 'B'},
    {'nome': 'Mariane', 'nota': 'A'},
    {'nome': 'Carli', 'nota': 'B'},
    {'nome': 'Josy', 'nota': 'A'},
    {'nome': 'Ana Maria', 'nota': 'C'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    copia_iterador_01, copia_iterador_02 = tee(valores_agrupados
                   )
    print(f'Agrupamento: {agrupamento}')

    for aluno in copia_iterador_01:
        print(f'\t{aluno}')

    quantidade = len(list(copia_iterador_02))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
