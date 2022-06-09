from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Maria', 55)
cliente2 = Cliente('José', 65)
cliente3 = Cliente('João', 45)

conta1 = ContaPoupanca(1111, 12345)
conta2 = ContaCorrente(2222, 12346)
conta3 = ContaPoupanca(1212, 12340)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(10)
    cliente1.conta.sacar(10)
else: 
    print('Cliente não autenticado.')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(100)
    cliente2.conta.sacar(33.4)
else: 
    print('Cliente não autenticado.')

if banco.autenticar(cliente3):
    cliente3.conta.depositar(100)
else: 
    print(f'Cliente {cliente3.nome} não autenticado.')