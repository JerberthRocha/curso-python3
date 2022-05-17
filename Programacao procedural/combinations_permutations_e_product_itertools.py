"""
Combinations, permutations e Product - Itertools
combinação - ordem não importa
permutação - ordem importa
ambos não repetem valores únicos
produto - ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

nomes = ['Maria', 'José', 'Carlos', 'João', 'John', 'Luis']

for grupo in combinations(nomes, 3):
    print(grupo)
# for grupo in permutations(nomes, 2):
#     print(grupo)
# for grupo in product(nomes, repeat=2):
#     print(grupo)
