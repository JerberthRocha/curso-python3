def converte_numero(n):
    try:
        n = int(n)
        return n
    except (ValueError, TypeError):
        try:
            n = float(n)
            return n
        except (ValueError, TypeError):
            pass


while True:
    numero = converte_numero(input('Informe um número: '))

    if numero is None:
        print('Erro. Informe um número.')
    else:
        resultado = numero * 2
        print(resultado)
