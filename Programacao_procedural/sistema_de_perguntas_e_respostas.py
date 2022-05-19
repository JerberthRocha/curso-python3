respostas_certas = 0

perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': 3, 'b': 4, 'c': 5},
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 2 * 3?',
        'respostas': {'a': 8, 'b': 2, 'c': 6},
        'resposta_certa': 'c',
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 10 - 2?',
        'respostas': {'a': 8, 'b': 5, 'c': 7},
        'resposta_certa': 'a',
    },
}

for perguntas_chaves, perguntas_valor in perguntas.items():
    print()
    print(perguntas_valor['pergunta'])

    print('Escolha um das opções abaixo: ')
    for p_chaves, p_valor in perguntas_valor['respostas'].items():
        print(f'[{p_chaves}]: {p_valor}')

    resposta_usuario = input('Qual a resposta certa? ')
    if resposta_usuario == perguntas_valor['resposta_certa']:
        print('Certo!')
        respostas_certas += 1
    else:
        print('Errado!')
print(f'Você acertou {respostas_certas} pergunta(s)!')
