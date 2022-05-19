# Dict Comprehensions foram introduzidas na linguagem através da especificação PEP 274.

# A sua sintaxe básica é:
# 1 {chave: valor for elemento in iteravel}
# Agora respira que vamos entender cada ponto:
# chave: será a chave de cada elemento do dicionário resultante.
# Valor: valor daquela chave.
# Elemento: é a unidade de iteração do iterável
# (se for uma lista, por exemplo, elemento irá receber o valor iteração a iteração)
# iteravel: conjunto de dados que estão sendo iterados (pode ser uma lista ou um set, por exemplo)

tupla = (
    ('Creme dental', 2),
    ('Tomate', 5.50),
    ('Cebola', 7.25),
)

dicionario = {chave: valor*2 for chave, valor in tupla}
print(dicionario)