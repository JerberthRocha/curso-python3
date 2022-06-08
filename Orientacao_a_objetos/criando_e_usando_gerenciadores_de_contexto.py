# FORMAS DE CRIAR GERENCIADORES DE CONTEXTO 

# class Arquivo:
#     def __init__(self, arquivo, modo):
#         print('ABRINDO ARQUIVO')
#         self.arquivo = open(arquivo, modo)
    
#     def __enter__(self):
#         print('RETORNANDO ARQUIVO')
#         return self.arquivo
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('FECHANDO ARQUIVO')
#         self.arquivo.close()
#         # OS PARÂMETROS SOMENTE SERÃO EXECUTADOS SE HOUVER ALGUMA EXCEÇÃO


# with Arquivo('arquivo', 'w') as arquivo:
#     arquivo.write('Escrevendo no arquivo')

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open('arquivo', 'w')
        yield arquivo
    finally:
        print('FECHANDO ARQUIVO')
        arquivo.close()

with abrir('arquivo', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')