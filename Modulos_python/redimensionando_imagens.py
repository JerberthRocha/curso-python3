import os
from PIL import Image

def main(main_images_folder, nova_largura=250):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe.')
    for raiz, diretorio, arquivos in os.walk(main_images_folder):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            nome_arquivo, extensao = os.path.splitext(arquivo)

            convertido ='_CONVERTIDO'

            novo_arquivo = nome_arquivo + convertido + extensao
            novo_caminho_completo = os.path.join(raiz, novo_arquivo)

            # if convertido in caminho_completo:    
            #     os.remove(caminho_completo)
            
            if convertido in caminho_completo:
                continue
            
            img_pillow = Image.open(caminho_completo)
            largura, altura = img_pillow.size
            nova_altura = round(nova_largura * altura / largura)

            nova_imagem = img_pillow.resize((nova_largura, nova_altura), Image.LANCZOS)
            nova_imagem.save(
                novo_caminho_completo,
                optimize=True,
                quality=70
            )

            img_pillow.close()

if __name__ == '__main__':
    main_images_folder  = '/home/jerberth/Área de Trabalho/imagens'
    main(main_images_folder, nova_largura=800)