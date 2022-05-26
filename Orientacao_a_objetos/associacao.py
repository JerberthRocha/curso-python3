class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property # GETTER
    def nome(self):
        return self.__nome 
    
    @property # GETTER
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca
    
    @property # GETTER
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')