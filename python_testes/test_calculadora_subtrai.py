import unittest
from calculadora import subtrai


class TestCalculadoraSubtrai(unittest.TestCase):
    def test_subtrai_5_e_5_deve_retonar_0(self):
        self.assertEqual(subtrai(5, 5), 0)

    def test_subtrai_5_negativo_e_5_deve_retonar_0(self):
        self.assertEqual(subtrai(-5, 5), -10)

    def test_subtrai_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 0),
            (1, 17, -16),
            (10, 5, 5),
            (116, 10, 106),
            (7, 3.5, 3.5),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai('8', 2)

    def test_subtrai_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(8, '2')

if __name__ == '__main__':
    unittest.main(verbosity=2)
