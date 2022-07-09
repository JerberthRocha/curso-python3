"""
TDD - Test Driven Develpment (Desenvolvimento Dirigido a Testes)

Siclo TDD:
Parte 1 (Red) -> Criar o teste e ver falhar
Parte 2 (Green) -> Criar o código e ver o teste passar
Parte 3 (Refactor) -> Melhorar o código
"""
from baconcomovos import bacon_com_ovos
import unittest


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bacon_com_ovos_deve_retonar_bacon_com_ovos_se_entrada_for_multipla_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida
                )

    def test_bacon_com_ovos_deve_retonar_bacon_se_entrada_for_multipla_de_3(self):
        entradas = (3, 21, 33, 48, 9)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida
                )

    def test_bacon_com_ovos_deve_retonar_ovos_se_entrada_for_multipla_de_5(self):
        entradas = (140, 215, 335, 485, 95)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida,
                    f'{entrada} não retornou {saida}'
                )

    def test_bacon_com_ovos_deve_retonar_passar_fome_se_entrada_nao_for_multipla_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida
                )


unittest.main(verbosity=2)
