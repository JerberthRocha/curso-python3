try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), # PEGA O CAMINHO ATUAL DO DIRETÓRIO
                '..' # .. SOBRE UMA PASTA -> /scr ENTRA NA PASTA ESPECIFICADA
            )
        )
    )
except:
    raise

from unittest import TestCase
from unittest.mock import patch
from pessoa import Pessoa
import unittest


class TestPessoa(TestCase):
    def setUp(self):
        self.pessoa1 = Pessoa('Peter', 'Parker')
        self.pessoa2 = Pessoa('Tony', 'Stark')

    def test_pessoa_atributo_nome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa1.nome, 'Peter')
        self.assertEqual(self.pessoa2.nome, 'Tony')

    def test_pessoa_atributo_nome_e_str(self):
        self.assertIsInstance(self.pessoa1.nome, str)
        self.assertIsInstance(self.pessoa2.nome, str)

    def test_pessoa_atributo_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa1.sobrenome, 'Parker')
        self.assertEqual(self.pessoa2.sobrenome, 'Stark')

    def test_pessoa_atributo_sobrenome_e_str(self):
        self.assertIsInstance(self.pessoa1.sobrenome, str)
        self.assertIsInstance(self.pessoa2.sobrenome, str)

    def test_pessoa_atributo_dados_obtidos_inicia_false(self):
        self.assertFalse(self.pessoa1.dados_obtidos)
        self.assertFalse(self.pessoa2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        # -> SIMULA UMA REQUISIÇÃO (REQUISIÇÃO FALSA)
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.pessoa1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa1.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa2.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.pessoa1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa1.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa2.dados_obtidos)

    def test_obter_todos_os_dados_sucesse_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.pessoa1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa1.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.pessoa1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa1.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa2.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
