# List Comprehension nada mais é do que uma forma rápida e eficiente de criar uma lista
# a partir de outra lista. Por exemplo, pense numa lista no Python: [1,2,3,4,5]. Agora
# imagine que você precisa multiplicar todos os números dessa lista por 5 e colocar todos
# os resultados numa nova lista. É exatamente isso que a List Comprehension vai fazer para você.

lista_1 = [1, 2, 3, 4, 5]
exemplo_1 = [variavel for variavel in lista_1]
exemplo_2 = [v * 2 for v in lista_1]
exemplo_3 = [(v, v2) for v in lista_1 for v2 in range(3)]
# print(exemplo_2)
# print(exemplo_3)

lista_2 = ['Maria', 'José', 'Carla']
exemplo_4 = [v.replace('a', '@').upper() for v in lista_2]
# print(exemplo_4)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)

exemplo_5 = [(valor, chave) for chave, valor in tupla]
exemplo_5 = dict(exemplo_5)
# print(exemplo_5)

lista_3 = list(range(1, 51))
exemplo_6 = [v for v in lista_3 if v % 2 == 0]
exemplo_7 = [v for v in lista_3 if v % 3 == 0 if v % 8 == 0]
exemplo_8 = [v if v % 2 == 0 and v % 8 == 0 else 0 for v in lista_3]
print(exemplo_6)
print(exemplo_7)
print(exemplo_8)

