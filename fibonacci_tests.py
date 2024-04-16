import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)

    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    
    def test_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)

    def test_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)
        
    def test_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)

    def test_negativo(self):
        resultado = fibonacci(-20)
        self.assertEqual(resultado, "Error")

    def test_not_int(self):
        resultado = fibonacci(0.2)
        self.assertEqual(resultado, "Error")

    def test_not_int_2(self):
        resultado = fibonacci("roman")
        self.assertEqual(resultado, "Error")

unittest.main()