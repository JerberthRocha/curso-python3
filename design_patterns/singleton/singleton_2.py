"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.
"""


def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        # O INIT SERÁ CHAMADO TODAS AS VEZES

        self.tema = 'Escuro'
        self.fonte = '18px'


@singleton
class FalaOi:
    def __init__(self):
        print('Oi...')


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)

    oi_1 = FalaOi()
    oi_2 = FalaOi()
    print(oi_1 == oi_2)
