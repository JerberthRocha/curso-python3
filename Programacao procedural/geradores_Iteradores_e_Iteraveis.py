import sys
import time

# ITERÁVEIS
lista = [1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))  # verifica do o objeto é iterável
lista = 12345
print(hasattr(lista, '__iter__'))  # verifica do o objeto é iterável
lista = ['string', 'string1']
print(hasattr(lista, '__iter__'))  # verifica do o objeto é iterável

# ITERADORES
# o for transforma a lista em um iterador utilizando o método __iter__
for i in lista:
    print(i)

print(hasattr(lista, '__next__'))  # verifica se a lista é um iterador


# GERADORES (GENERATOR)
l1 = [x for x in range(1000)]  # GERA UMA LISTA
l2 = (x for x in range(1000))  # GERA UM GENERATOR

print(type(l1))
print(type(l2))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))


def gera():
    for n in range(10):
        yield n
        time.sleep(0.1)


g = gera()
print(g)
# print(next(g))
# print(next(g))

for v in g:
    print(v)
