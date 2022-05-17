from dados_para_o_map import pessoas, lista, produtos


# def filtra_preco(p):
#     if p['preco'] > 50:
#         return p


# nova_lista = filter(filtra_preco, produtos)
# nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5]
nova_lista = filter(lambda p: p['preco'] > 15, produtos)
# print(list(nova_lista))
# print(nova_lista)
for produto in nova_lista:
    print(produto)
