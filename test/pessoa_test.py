from unittest import TestCase, main

from pessoa import Pessoa


class PessoaTest(TestCase):
    p = Pessoa('luiz', 'filipy', 1.9, 56.9)

    def test_full_name(self):
        self.assertEqual(self.p.full_name(), 'luiz filipy', 'deve ser \'luiz filipy\'')
        
    
    def test_full_name_return_type(self):
        self.assertIsInstance(self.p.full_name(), str)
        
    
    def test_imc(self):
        self.assertEqual(self.p.imc(), 15.761772853185596, 'deve ser 15.761772853185596')
    
    def test_imc_is_none(self):
        self.assertIsNotNone(self.p.imc())
    
    def test_imc_none(self):
        self.p.altura = '1.9'
        self.p.peso = '56.9'
        
        self.assertIsNone(self.p.imc())

if __name__ == '__main__':
    main()