# def ola_mundo():
#     return 'Olá mundo!'
#
#
# def principal(funcao):
#     return funcao()
#
#
# ola = principal(ola_mundo)
# print(ola)

def principal(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi, {nome}'


def saudacao(cumprimento, nome):
    return f'{cumprimento} {nome}'


executando = principal(fala_oi, 'Maria')
executando2 = principal(saudacao, 'Boa tarde', 'José')
print(executando)
print(executando2)
