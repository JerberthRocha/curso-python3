"""
PILHAS E FILAS
PILHAS (STACK): LIFO: LAST IN, FIRST OUT
EX: PILHA DE LIVRO

FILAS (QUEUE): FIFO: FIRST IN, FIRST OUT
EX: FILA DE BANCO
"""

from collections import deque
import queue
from time import sleep

# FUNCIONALIDADE DE FILA
"""fila = deque()
fila.append('Maria')
fila.append('João')
fila.append('Ana')

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

for nome in fila:
    print(nome)

fila_2 = deque(maxlen=5)
fila_2.extend([1, 2, 3, 4])
fila_2.append(5)
fila_2.append(6)
fila_2.append(7)
fila_2.append(8)
fila_2.append(9)
fila_2.append(10)
print(fila_2)"""

fila_3 = deque(maxlen=3)

for i in range(10):
    fila_3.append(i)
    sleep(1)
    print(fila_3)   
