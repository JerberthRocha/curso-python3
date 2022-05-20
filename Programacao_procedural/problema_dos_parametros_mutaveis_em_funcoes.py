# mutável: lista, dicionario
# imutável: tupla, string, numeros, booleanos, None

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_cliente_1 = ['Fabricio']
clientes_1 = lista_de_clientes(['João', 'Maria', 'Ana'], lista_cliente_1)
clientes_2 = lista_de_clientes(['Marcos', 'José', 'Mariana'])
clientes_3 = lista_de_clientes(['Joana'])

print(clientes_1)
print(clientes_2)
print(clientes_3)
