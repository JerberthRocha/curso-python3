# função strip - tira espaços do início e do fim da frase/palavra
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')  # a função split divide a string com base no caracter passado por parâmetro
lista_2 = string.split(',')
print(string)
print(lista_1)
print(lista_2)

# função join - junta palavras/strings
nova_string = ' '.join(lista_1)
print(nova_string)

# enumerate - enumera os indices de uma lista/tupla
for indice, valor in enumerate(lista_1):
    print(indice, valor, lista_1[indice])
