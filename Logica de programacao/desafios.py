decrescente = 11
for numero in range(11):
    if numero <= 8:
        print(numero, end=' ')
    else:
        break
    decrescente -= 1
    print(decrescente)

print(15 * '-=')

for crescente, decrescente in enumerate(range(10, 1, -1)):
    print(crescente, decrescente)
