from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

# Terça-feira, 14 de junho de 2022

setlocale(LC_ALL, 'pt-br') # 'pt_BR.utf-8'

data = datetime.now()
formatacao1 = data.strftime('%A, %d de %B de %Y')
formatacao2 = data.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

mes_atual = int(data.strftime('%m'))
print(mes_atual, mdays[mes_atual])