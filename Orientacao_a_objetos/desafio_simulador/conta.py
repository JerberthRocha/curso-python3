from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor): pass

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()
    
    def detalhes(self):
        print(f'Número da Agência: {self.agencia} '
              f'Número da Conta: {self.conta} '
              f'Saldo: R$ {self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=300):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo Insuficiente!')
            return
        
        self.saldo -= valor
        self.detalhes()
    
    # def depositar(self, valor):
    #     self.saldo += valor

    # def detalhes(self):
    #     print(f'Número da Agência: {self.agencia}')
    #     print(f'Número da Conta: {self.conta}')
    #     print(f'Saldo: R$ {self.saldo}')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return
        
        self.saldo -= valor
        self.detalhes()
    
    # def depositar(self, valor):
    #     self.saldo += valor
    
    # def detalhes(self):
    #     print(f'Número da Agência: {self.agencia}')
    #     print(f'Número da Conta: {self.conta}')
    #     print(f'Saldo: R$ {self.saldo}')