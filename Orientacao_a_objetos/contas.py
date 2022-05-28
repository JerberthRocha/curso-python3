from Orientacao_a_objetos.classes_abstratas import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return
        
        self._saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        # super().__init__(agencia, conta, saldo)
        Conta.__init__(self, agencia, conta, saldo)
        self._limite = limite
    
    @property # GETTER
    def limite(self):
        return self._limite
    
    # @limite.setter
    # def limite(self, valor):
    #     self._limite = valor

    def sacar(self, valor):

        if (self._saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        
        self._saldo -= valor
        self.detalhes()