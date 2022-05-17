carrinho = [
    ('Produto 1', 10.9),
    ('Produto 2', 31.5),
    ('Produto 3', '30'),
    ('Produto 4', 71.1),
    ('Produto 5', 7.3),
    ('Produto 6', 22),
    ('Produto 7', 30),
    ('Produto 8', '33'),
    ('Produto 9', '57'),
    ('Produto 10', 30.6)
]

# total = 0
# for valor in carrinho:
#     total += valor[1]

total = sum([float(valor_produto) for nome_produto, valor_produto in carrinho])
print(f'Valor total = {total:0.2f}')

