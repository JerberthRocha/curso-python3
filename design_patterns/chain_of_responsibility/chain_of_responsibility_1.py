"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

# Implemantando com funções

def handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']
    if letter in letters:
        return print(f'O handler_ABC tratou a letra {letter}')
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']
    if letter in letters:
        return print(f'O handler_DEF tratou a letra {letter}')
    return handler_unsoveld(letter)

def handler_unsoveld(letter: str) -> str:
    return print(f'A letra {letter} não foi tratada')


if __name__ == '__main__':
    handler_ABC('A')
    handler_ABC('B')
    handler_ABC('C')
    handler_ABC('D')
    handler_ABC('E')
    handler_ABC('F')
    handler_ABC('G')