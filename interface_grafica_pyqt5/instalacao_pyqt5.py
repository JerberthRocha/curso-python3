"""
PYQT5 É UM TOOLKIT DESENVOLVIDO EM C++ UTILIZADO POR VÁRIOS PROGRAMAS
PARA CRIAÇÃO DE APLICAÇÕES GUI (INTERFACE GRÁFICA). TAMBÉM INCLUI DIVERSAS
FUNCIONALIDADES, COMO: ACESSO A BASE DE DADOS, THREADS, COMUNICAÇÃO DE REDE, ETC...
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('OK')
        self.btn.setStyleSheet('font-size: 15px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.clique_botao)

        self.setCentralWidget(self.cw)

    def clique_botao(self):
        print('Olá Mundo!')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
