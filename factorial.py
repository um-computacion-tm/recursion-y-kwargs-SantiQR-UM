import unittest


def factorial(num):
    if num == 1 or num == 0:
        return 1
    return(num * factorial(num-1))


class TestFactorial(unittest.TestCase):
    def test_0(self):
        resultado = factorial(0)
        self.assertEqual(resultado, 1)

    def test_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)

    def test_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)
    
    def test_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)

    def test_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado, 24)

if __name__ == "__main__":
    unittest.main()
