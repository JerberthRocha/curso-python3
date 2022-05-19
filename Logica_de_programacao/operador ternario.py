logged_user = False

# if logged_user:
#     msg = 'Usuário logado.'
# else:
#     msg = 'Usuário precisa logar.'
#
# print(msg)

# COM OPERADOR TERNÁRIO
# Se condição True                   Condição           Se condição False
msg_ternario = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg_ternario)

idade = 18
# if idade >= 18:
#     print('Liberado!')
# else:
#     print('Barrado!')

var = 'Liberado!' if idade >= 18 else 'Barrado'

print(var)

