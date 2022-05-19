# *args é um tupla. usado quando não se sabe quantos parâmetros serão passados para função
#  **kwargs é um dicionário


def func(*args):  # os argumentos ficam empacotados em uma tupla
    args = list(args)
    args[0] = 20
    args[4] = 'novo texto'
    print(args)


def desempacotamento(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'])
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


func(1, 2, 3, 3, 'texto')
print()
print('DESEMPACOTAMENTO DA LISTA USANDO ASTERISCO(*)')
lista = [1, 2, 3, 4, 5]
print(*lista, sep=' - ')  # o * significa que a lista será desempacotada
print()
print('Enviando uma lista desempacotada pra função')
desempacotamento(*lista, 10, 20, 30, 40, 50, nome='jerberth', sobrenome='rocha', idade=29)
