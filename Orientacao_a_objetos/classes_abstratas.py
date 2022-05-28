# CLASSE ABSTRATA É UMA CLASSE QUE NÃO PODE SER INSTANCIADA

from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractclassmethod
#     def falar(self):
#         pass

# class B(A):
#     def falar(self):
#         print('Falar...')

# c = B()
# c.falar()

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

        @property
        def agencia(self):
            return self._agencia

        @property
        def conta(self):
            return self._conta

        @property
        def saldo(self):
            return self._saldo
        
        @agencia.setter
        def agencia(self, valor):
            self._agencia = valor

        @conta.setter
        def conta(self, valor):
            self._conta = valor

        @saldo.setter
        def saldo(self, valor):
            if not isinstance(valor, (int, float)):
                raise ValueError('Saldo precisa ser numérico')
            
            self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico')

        self._saldo += valor
        self.detalhes()
    
    def detalhes(self):
        print(f'Agência: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: {self._saldo}')
        
    @abstractmethod
    def sacar(self, valor):
        pass

# class Teste(Conta):
#     pass

# t = Teste(111, 222, 333)