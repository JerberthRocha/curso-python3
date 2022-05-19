# # cpf = input('Informe o CPF: ')
# cpf = '05844519388'
# novo_cpf = cpf[:-2]
# iteracoes = 10
# soma = 0
# for n in novo_cpf:
#     numero = int(n)
#     soma += (numero * iteracoes)
#     iteracoes -= 1
#
# proximo_numero = 11 - (soma % 11)
# if proximo_numero > 9:
#     proximo_numero = 0
#
# novo_cpf += str(proximo_numero)
#
# iteracoes = 11
# soma = 0
# for n in novo_cpf:
#     numero = int(n)
#     soma += (numero * iteracoes)
#     iteracoes -= 1
#
# proximo_numero = 11 - (soma % 11)
# if proximo_numero > 9:
#     proximo_numero = 0
#
# novo_cpf += str(proximo_numero)
# msg = f'CPF {cpf} é válido.' if cpf == novo_cpf else f'CPF {cpf} é inválido.'
# print(cpf)
# print(novo_cpf)
# print(msg)

cpf = '16899535009'
novo_cpf = cpf[:9]
reverso = 10
total = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        proximo_digito = 11 - (total % 11)

        if proximo_digito > 9:
            proximo_digito = 0
        total = 0
        novo_cpf += str(proximo_digito)

msg = f'CPF {cpf} é válido.' if cpf == novo_cpf else f'CPF {cpf} é inválido.'
print(msg)
