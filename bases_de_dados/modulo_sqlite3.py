import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                 'nome TEXT,'
#                 'peso REAL'
#                 ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Ana', 47.2))
# cursor.execute(
#                 'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', 
#                 {'nome': 'Maria', 'peso': 65.3}
#               )
# cursor.execute(
#                 'INSERT INTO clientes VALUES (:id, :nome, :peso)', 
#                 {'id': None, 'nome': 'João', 'peso': 88}
#               )
# conexao.commit()

# cursor.execute(
#                 'UPDATE clientes SET nome=:nome WHERE id=:id',
#                 {'nome':'Joana', 'id': 2}
#               )
# conexao.commit()

# cursor.execute(
#                 'DELETE FROM clientes WHERE id=:id',
#                 {'id': 4}
#               )
# conexao.commit()

cursor.execute(
                'SELECT nome, peso FROM clientes WHERE peso < :peso',
                {'peso': 50}
              )

for linha in cursor.fetchall():
    nome, peso = linha

    # print(f'Id: {identificador}')
    print(f'Nome: {nome}')
    print(f'Peso: {peso}Kg')
    print(5 * '-=-')

cursor.close()
conexao.close()