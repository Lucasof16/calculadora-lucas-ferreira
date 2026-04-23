import unittest
from calculadora import soma, subtrai, multiplica, divide 

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(5, 5), 10)

    def test_subtrai(self):
        self.assertEqual(subtrai(10, 5), 5)

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 3), 9)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_por_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
