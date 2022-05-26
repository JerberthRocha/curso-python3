"""
public, protected, private
### CONVENÇÃO 
_ protected / private -> RECOMENDADO NÃO ACESSAR O ATRIBUTO POR FORA DA CLASSE
__ protected / private -> FORTEMENTE RECOMENDADO NÃO ACESSAR O ATRIBUTO POR FORA DA CLASSE

"""
class BaseDeDados:
    def __init__(self):
        self._dados = {}
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Maria')
bd.inserir_cliente(2, 'José')
bd.inserir_cliente(3, 'João')

# bd.__dados = 'teste'
# print(bd.__dados)

bd.apaga_cliente(3)

bd.lista_clientes()
