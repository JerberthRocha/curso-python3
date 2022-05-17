
try:
    a = {}
    print(a)
except NameError as erro:
    print(f'Erro: {erro}')
except (IndexError, KeyError) as erro:
    print(f'Erro de índice ou chave. {erro}')
except Exception as erro:
    print(f'Ocorreu um erro inesperado. {erro}')
else:
    print('O else será executado se o cógido não apresentar erro')
finally:
    print('O finally toda vez será executado')
