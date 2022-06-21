"""
https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
"""

import PyPDF2
import os

caminho_dos_pdfs = ''

"""# UNE ARQUIVOS NO FORMATO PDF
novo_pdf = PyPDF2.PdfFileMerger()
for raiz, diretorio, arquivos  in os.walk(caminho_dos_pdfs):
    for arquivo in arquivos:
        print(arquivo)
        caminho_completo_arquivo = os.path.join(raiz, arquivo)

        with open('caminho_completo_arquivo', 'rb') as arquivo_pdf:
            novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)"""

with open('pdf/novo_arquivo.pdf') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.numPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)