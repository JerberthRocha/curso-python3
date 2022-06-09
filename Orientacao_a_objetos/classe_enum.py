from enum import Enum, auto

class Direcoes(Enum):
    direita = auto()
    esquerda = auto()
    cima = auto()
    baixo = auto()


def move(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Você não pode mover para essa direção.')
    
    return f'Movendo para {direcao.name}'

if __name__ == '__main__':
    print(move(Direcoes.direita))
    print(move(Direcoes.esquerda))
    print(move(Direcoes.cima))
    print(move(Direcoes.baixo))

    print(22 * '-=')

    for direcao in Direcoes:
        print(direcao, direcao.value, direcao.name)