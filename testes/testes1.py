import unittest
import calculadora_teste
from random import randint

class TesteCalculadora(unittest.TestCase):
    def test_soma(self):
        n1 = randint(0,999)
        n2 = randint(0,999)
        soma = n1 + n2
        self.assertEqual(soma, calculadora_teste.soma(n1,n2))
    

    def test_divisao(self):
        n1 = randint(0,999)
        n2 = randint(0,999)
        div = n1/n2
        self.assertEqual(div, calculadora_teste.divisao(n1,n2))

    def test_divisao_por_zero(self):
        n1 = randint(0,999)
        n2 = 0
        div_zero = 'Não existe divisão por zero'
        self.assertEqual(div_zero, calculadora_teste.divisao(n1,n2))


    if __name__=='__main__':
        unittest.main()