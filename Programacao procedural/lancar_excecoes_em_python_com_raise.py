# https://docs.python.org/3/library/exceptions.html

# def divide(n1, n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as erro:
#         print(erro)
#         raise
#
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as e:
#     print(e)

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero (0)')
    return n1 / n2


try:
    print(divide(2, 0))
except ValueError as e:
    print('Você está tentando dividir por 0.')
    print('Log: ', e)
