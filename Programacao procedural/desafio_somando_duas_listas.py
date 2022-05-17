lista_a = [1, 2, 3, 4, 5, 2, 40]
lista_b = [1, 2, 10, 1, 6]

print()
print('# SOLUÇÃO 01')
lista_soma = []
for indice, valor in enumerate(lista_b):
    for index, v in enumerate(lista_a):
        if indice == index:
            lista_soma.append(valor + v)
            break
print(lista_soma)

print()
print('# SOLUÇÃO 02')
lista_soma.clear()
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

print()
print('# SOLUÇÃO 03')
lista_soma.clear()
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

print()
print('# SOLUÇÃO 04')
lista_soma.clear()
lista_soma = [x+y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
