# def fala():
#     print('OI')
#
#
# variavel = fala
# variavel()
# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Agora estou decorada.')
#         funcao(*args, **kwargs)
#     return slave
#
#
# @master
# def fala():
#     print('OI')
#
#
# @master
# def outra_msg(msg):
#     print(msg)
#
#
# outra_msg('Enviando mensagem')

from time import time


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função {funcao.__name__} '
              f'levou {tempo:.2f}ms para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(1000):
        print(i, end='')


demora()
