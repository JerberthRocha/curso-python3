# funcao_anonima = lambda x, y: x * y
# print(funcao_anonima(2, 3))


lista =[
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]


# def func(item):
#     return item[1]

# lista.sort(key=func)

# lista.sort(key=lambda item: item[1])  # ,reverse=True)

print(sorted(lista, key=lambda item: item[1]))
