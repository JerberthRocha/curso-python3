from itertools import zip_longest, count
"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
indice = count()
cidades = ['São Paulo', 'Luis Domingues', 'Salvador', 'Manaus', 'Carutapera']
estados = ['SP', 'MA', 'BA', 'AM']

print('FUNÇÃO zip COM count()')
estados_cidades = zip(
    indice,
    estados,
    cidades
)
for indice, estado, cidade in estados_cidades:
    print(indice, estado, cidade)

print()
print('FUNÇÃO zip_longest')
estados_cidades = zip_longest(
    estados,
    cidades,
    fillvalue='Estado'
)  # fillvalue SETA UM VALOR PADRÃO NO LUGAR DO none
for valor in estados_cidades:
    print(valor)
