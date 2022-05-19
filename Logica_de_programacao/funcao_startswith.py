lista = ['Maria', 'João', 'Carlos']

# A função starswith verifica se uma palavra começa com um determinado caracter ou frase
# a função endswith faz a mesma coisa, só que com o final da frase ou palavra

for letra in lista:
    if letra.lower().startswith('j'):
        print('Existe palavra que começa com J.')
        break
else:
    print('Não existe palavra que começa com J.')
