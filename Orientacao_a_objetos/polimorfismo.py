from abc import ABC, abstractmethod

# TIPOS DE POLIMORFISMO: SOBREPOSIÇÃO E SOBRECARGA
# O PYTHON SÓ SUPORTA O POLIMORFISMO DE SOBREPOSIÇÃO

class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()
b.fala('assunto')
c.fala('outro assunto')