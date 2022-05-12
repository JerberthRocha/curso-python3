"""
Listas em Python
fatiamento
append, insert, pop, del, clear, min, max
extend: faz a concatenação de listas
range
"""
# lista = [1, 2, 3, 4]
# for numero in lista:
# print(lista[Começo:Fim:Passo])
# print(lista[::-1])

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.extend(l2)
# l2.insert(1, 'novo_item')
# print(l1)
# print(l2)
# l1.pop(4)
# print(l1)

secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Suas chances acabaram!')
        break
    else:
        print(f'Voce possui {chances} chance(s).')

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print('A letra não existe na palavra secreta.')
        digitadas.pop()
        chances -= 1

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns, voce ganhou! A palavra secreta era {secreto}.')
        break
    else:
        print(f'Palavra incompleta: {secreto_temporario}')

    print(20 * '-=')
