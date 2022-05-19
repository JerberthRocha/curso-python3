def f(var):
    print(var)


def dumb():
    return f  # a Função dum() retorna a função f sem executar. Quando uma função é chamada sem () ela não é executada


dumb()('Passando parâmetro para a função f')

var = dumb()

print(f"Os id's na memória do computador: variável var: {id(var)}, função f: {id(f)}")
if var == f:
    var('A variável var pode imprimir algo na tela igual a função f')
    print('var e f são a mesma função.')
else:
    print('São diferentes.')


def retorna_tupla():
    return 'jerberth', 'rocha'


retorno = retorna_tupla()
print(retorno)
