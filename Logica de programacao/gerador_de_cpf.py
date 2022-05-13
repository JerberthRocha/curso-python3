from random import randint
n = randint(100000000, 999999999)
cpf = str(n)
reverso = 10
total = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        proximo_digito = 11 - (total % 11)

        if proximo_digito > 9:
            proximo_digito = 0
        total = 0
        cpf += str(proximo_digito)

print(f'CPF gerado: {cpf}.')
