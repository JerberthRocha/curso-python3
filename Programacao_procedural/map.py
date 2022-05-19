from dados_para_o_map import pessoas, produtos, lista

# nova_lista = map(lambda x: x * 2, lista)
# print(list(nova_lista))
#
# for produto in produtos:
#     print(produto)


# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
#
# novos_precos = map(aumenta_preco, produtos)
# for preco in novos_precos:
#     print(preco)

nomes = map(lambda n: n['nome'], pessoas)
for nome in nomes:
    print(nome)
