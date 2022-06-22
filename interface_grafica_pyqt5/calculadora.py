import sys
from typing import Text
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_butao(QPushButton('7'), 1, 0, 1, 1)
        self.add_butao(QPushButton('8'), 1, 1, 1, 1)
        self.add_butao(QPushButton('9'), 1, 2, 1, 1)
        self.add_butao(QPushButton('+'), 1, 3, 1, 1)
        self.add_butao(
            QPushButton('⌫'), 1, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: FireBrick; color: black; font-weight: 700'
        )

        self.add_butao(QPushButton('4'), 2, 0, 1, 1)
        self.add_butao(QPushButton('5'), 2, 1, 1, 1)
        self.add_butao(QPushButton('6'), 2, 2, 1, 1)
        self.add_butao(QPushButton('-'), 2, 3, 1, 1)
        self.add_butao(
            QPushButton('C'), 2, 4, 1, 1,
            lambda: self.display.setText(''),
            # 'background: DarkOrange; color: #black; font-weight: 700'
        )

        self.add_butao(QPushButton('1'), 3, 0, 1, 1)
        self.add_butao(QPushButton('2'), 3, 1, 1, 1)
        self.add_butao(QPushButton('3'), 3, 2, 1, 1)
        self.add_butao(QPushButton('/'), 3, 3, 1, 1)
        self.add_butao(QPushButton('.'), 3, 4, 1, 1)

        self.add_butao(QPushButton('('), 4, 0, 1, 1)
        self.add_butao(QPushButton('0'), 4, 1, 1, 1)
        self.add_butao(QPushButton(')'), 4, 2, 1, 1)
        self.add_butao(QPushButton('*'), 4, 3, 1, 1)
        self.add_butao(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: green; color: black; font-weight: 700'
        )

        self.setCentralWidget(self.cw)

    def add_butao(self, botao, linha, coluna, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(botao, linha, coluna, rowspan, colspan)
        if not funcao:
            botao.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + botao.text()
                )
            )
        else:
            botao.clicked.connect(funcao)

        if style:
            botao.setStyleSheet(style)

        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)



    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Inválida.')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    qt.exec_()
