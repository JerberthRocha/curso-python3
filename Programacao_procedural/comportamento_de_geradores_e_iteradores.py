# LISTS, TUPLES, STR -> SEQUENCES -> ITERÁVEL
nome = 'João José'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('OLHA O FOR')
for letra in gerador:
    print(letra)

print('OLHA O OUTRO FOR')
for letra in gerador:
    print(letra)

print('PRÓXIMO NEXT')
print(next(gerador))
