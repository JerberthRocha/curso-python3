import random
import string

# inteiro = random.randint(1, 10)
# inteiro = random.randrange(100, 1000, 100)
# flutuante = random.uniform(1, 5) # GERA NÚMERO FLUTUANTE ENTRE DOIS NÚMEROS ESPECIFICADOS POR PARAMETRO
# flutuante = random.random() # GERA NÚMERO FLUTUANTE ENTRE 0 E 1
# print(inteiro)
# print(f'{flutuante:0.2f}')

# nomes = ['Maria', 'Ana', 'José', 'Carlos', 'João']

# sorteio = random.choice(nomes)
# print(sorteio)

# sorteio1 = random.choices(nomes, k=2) # REPETE OS NOMES
# print(sorteio1)

# sorteio2 = random.sample(nomes, 2) # NÃO REPETE OS NOMES
# print(sorteio2)

# random.shuffle(nomes)
# print(nomes)

letras = string.ascii_letters
numeros = string.digits
caracteres = '%$&*@#!'
geral = letras + numeros + caracteres
senha = ''.join(random.choices(geral, k=10))
print(senha)