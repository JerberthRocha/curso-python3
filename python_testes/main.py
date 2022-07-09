from calculadora import soma

try:
    print(soma('30', 7))
except AssertionError as e:
    print('Conta Inválida')