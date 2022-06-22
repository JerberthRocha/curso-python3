import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()
    
    def inserir(self, nome, telefone):
        comando = 'INSERT OR IGNORE INTO agenda(nome, telefone) VALUES (?, ?)'
        self.cursor.execute(comando, (nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        comando = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(comando, (nome, telefone, id))
        self.conexao.commit()

    def excluir(self, id):
        comando = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(comando, (id,))
        self.conexao.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conexao.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Maria Ana', 125546)
    # agenda.inserir('Ana Maria', 125536)
    # agenda.inserir('Maria Carla', 122546)
    # agenda.inserir('Maria Paula', 121546)
    # agenda.inserir('Mariana', 125526)

    # agenda.listar()
    
    agenda.buscar('Maria')