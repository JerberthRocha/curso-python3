from time import sleep
from threading import Thread
from threading import Lock

# class MinhaThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()
    
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)

# t1 = MinhaThread('Thread 1', 7)
# t1.start()

# t2 = MinhaThread('Thread 2', 5)
# t2.start()

# t3 = MinhaThread('Thread 3', 2)
# t3.start()

# for i in range(10):
#     print(i)
#     sleep(1)

# def minha_thread(texto, tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=minha_thread, args=('Olá 1', 6))
# t1.start()

# t2 = Thread(target=minha_thread, args=('Olá 2', 3))
# t2.start()

# t2 = Thread(target=minha_thread, args=('Olá 3', 4))
# t2.start()

# for i in range(15):
#     sleep(.5)
#     print(i)

# t1 = Thread(target=minha_thread, args=('Olá!!', 5))
# t1.start()

# while t1.is_alive():
#     print('Esperando a Thread acabar.')
#     sleep(2)

# # t1.join() # JUNTA AS THREADS

# print('Thread finalizada.')

# O PROBLEMA

# class Ingressos:
#     def __init__(self, estoque):
#         self.estoque = estoque

#     def comprar(self, quantidade):
#         if quantidade < self.estoque:
#             sleep(1)
#             self.estoque -= quantidade
#             print(f'Compra realizada. ainda temos {self.estoque} ingresso(s) disponível(is).')
#             return
#         print('Não temos mais ingressos disponíveis.')

# if __name__ == '__main__':
#     ingresso = Ingressos(10)

#     for i in range(1, 20):
#         t = Thread(target=ingresso.comprar, args=(i,))
#         t.start()

# A SOLUÇÃO

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos mais ingressos disponíveis.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade}. Ainda temos {self.estoque} ingresso(s) disponível(is).')

        # Libera o método
        self.lock.release()

# if __name__ == '__main__':
#     ingresso = Ingressos(10)

#     for i in range(1, 20):
#         t = Thread(target=ingresso.comprar, args=(i,))
#         t.start()

if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []  # Lista para manter as threads
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    # Inicia as threads
    for t in threads:
        t.start()

    # Verifica se todas as threads terminaram
    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(f'Quantidade de ingressos: {ingressos.estoque}')