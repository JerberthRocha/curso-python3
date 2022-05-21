"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""
import funcoes

cnpj = funcoes.remove_caracteres('04.252.011/0001-10')
if cnpj == '00000000000000':
    print('INVÁLIDO!')
else:
    novo_cnpj = cnpj[:-2]
    multiplicador = 5
    segundo = 9
    total = 0
    for index in range(26):
        if index < 12:
            if index == 4:
                multiplicador = 9
            if multiplicador > 1:
                total += int(novo_cnpj[index]) * multiplicador
                multiplicador -= 1
        else:
            if index == 12:
                novo_numero = 11 - (total % 11)
                if novo_numero > 9:
                    novo_cnpj += '0'
                else:
                    novo_cnpj += str(novo_numero)

        if index >= 12:
            if index == 12:
                multiplicador = 6
                total = 0
            if index == 17:
                multiplicador = 9
            if multiplicador > 1:
                total += int(novo_cnpj[index-12]) * multiplicador
                multiplicador -= 1
            else:
                if index == 25:
                    novo_numero = 11 - (total % 11)
                    if novo_numero > 9:
                        novo_cnpj += '0'
                    else:
                        novo_cnpj += str(novo_numero)

    if novo_cnpj == cnpj:
        print(f'Novo CNPJ: {novo_cnpj} | CNPJ: {cnpj}')
        print('\n\t\t\t\t\t\tVÁLIDO!')
    else:
        print('INVÁLIDO!')
