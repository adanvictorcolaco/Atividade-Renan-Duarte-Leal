import unittest
from calculadora import calcular_media, aplicar_desconto

class TestCalculadora(unittest.TestCase):

    def test_calcular_media(self):
        # Arrange & Act
        resultado = calcular_media([10, 8, 6])
        # Assert
        self.assertEqual(resultado, 8.0)

    def test_aplicar_desconto(self):
        # Arrange & Act
        resultado = aplicar_desconto(200, 10)
        # Assert
        self.assertEqual(resultado, 180.0)

if __name__ == '__main__':
    unittest.main()