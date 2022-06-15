import os
import shutil

caminho_origem = 'C:\Fotos\Wallpapers'
caminho_novo = 'C:\Fotos\Wallpapers2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'A Pasta {caminho_novo[9:]} já existe.')

for raiz, diretorio, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        caminho_antigo_do_arquivo = os.path.join(raiz, arquivo)
        novo_caminho_do_arquivo = os.path.join(caminho_novo, arquivo)

        # MOVENDO ARQUIVOS
        # shutil.move(caminho_antigo_do_arquivo, novo_caminho_do_arquivo)
        # print(f'Arquivo {arquivo} movido com sucesso.')

        # COPIANDO ARQUIVOS
        # if '.jpg' in arquivo:
        #     shutil.copy(caminho_antigo_do_arquivo, novo_caminho_do_arquivo)
        #     print(f'Arquivo {arquivo} copiado com sucesso.')
    
# for raiz, diretorio, arquivos in os.walk(caminho_novo):
#     for arquivo in arquivos:
#         caminho_antigo_do_arquivo = os.path.join(raiz, arquivo)
#         novo_caminho_do_arquivo = os.path.join(caminho_novo, arquivo)

#         #APAGANDO ARQUIVOS
#         if '.jpg' in arquivo:
#             os.remove(novo_caminho_do_arquivo)
#             print(f'O arquivo {arquivo} foi apagado com sucesso.')