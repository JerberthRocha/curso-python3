"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # O INIT SERÁ CHAMADO TODAS AS VEZES

        self.tema = 'Escuro'
        self.fonte = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)
