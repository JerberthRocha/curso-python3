import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()

# INSERE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         # cursor.execute(sql, ('Jerberth', 'Rocha', 29, 58.9)) # EXECUTE INSERTE SOMENTE 1 REGISTRO POR VEZ
#         dados = [
#             ('Marta','Oliveira', 33, 67),
#             ('Zlatan','Ibrahimovic', 40, 75),
#             ('Fikayo','Tomori', 23, 62),
#             ('Pierre','Kalulu', 20, 61),
#         ]

#         cursor.executemany(sql, dados) # EXECUTEMANY INSERE VÁRIOS REGISTROS DE UMA VEZ
#         conexao.commit()

# DELETE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (13,))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         # sql = 'DELETE FROM clientes WHERE id IN (%s, %s)' # DELETE OS REGISTROS INFORMADOS NA TUPLA
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s' # DELETA REGISTRO EM UM RANGE
#         cursor.execute(sql, (6, 8))
#         conexao.commit()

# UPDATE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome = %s WHERE id = %s'
#         cursor.execute(sql, ('JERBERTH', 5))
#         conexao.commit()

# SELECIONA
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 50')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
