# class A:
#     def falar(self):
#         print('Falando... Está em A')

# class B(A):
#     def falar(self):
#         print('Falando... Está em B')

# class C(A):
#     def falar(self):
#         print('Falando... Está em C')
        
# class D(B, C):
#     pass

# d = D()
# d.falar()

from heranca_multipla_log import LogMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
    
    def ligar(self):
        if self._ligado:
            return
        self._ligado = True
        print(f'{self._nome} foi ligado')
    
    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False
        print(f'{self._nome} foi desligado')


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        Eletronico.__init__(self, nome)
        self._conectado = False
    
    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.log_error(error)
            return
        
        if self._conectado:
            error = f'{self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return
        
        self._conectado = True
        info = f'{self._nome} está conectado'
        print(info)
        self.log_info(info)
    
    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado'
            print(error)
            self.log_error(error)
            return
        
        info = f'{self.nome} foi desligado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = False