import os # https://docs.python.org/pt-br/3/library/os.html

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')

def formata_tamanho(tamanho_arquivo):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho_arquivo < kilo:
        texto = 'B'
    elif tamanho_arquivo < mega:
        tamanho_arquivo /= kilo
        texto = 'K'
    elif tamanho_arquivo < giga:
        tamanho_arquivo /= mega
        texto = 'M'
    elif tamanho_arquivo < tera:
        tamanho_arquivo /= giga
        texto = 'G'
    elif tamanho_arquivo < peta:
        tamanho_arquivo /= tera
        texto = 'T'
    else:
        tamanho_arquivo /= peta
        texto = 'P'
    
    tamanho_arquivo = round(tamanho_arquivo, 2)
    return f'{tamanho_arquivo}{texto}'.replace('.',',')

contador = 0
for raiz, diretorio, arquivos in os.walk('C:\Fotos\Wallpapers'):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                print(arquivo)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', extensao_arquivo)
                print('Tamanho:', tamanho_arquivo)
                print('Tamanho Formatado:', formata_tamanho(tamanho_arquivo))
            except PermissionError as e:
                print('Sem permissão.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido.', e)

print()
print(f'{contador} arquivo(s) encontrado(s)')