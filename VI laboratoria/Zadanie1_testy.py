from Zadanie1 import Operacje
import unittest

class test_decorators(unittest.TestCase):
    def test_sum(self):
        op = Operacje()
        self.assertEqual(op.suma(1,2,3), 6)
        self.assertEqual(op.suma(1,2), 7)
        self.assertEqual(op.suma(1), 10)
        
        with self.assertRaises(TypeError):
            op.suma()
            
        op['suma'] = [1, 2]
        
        self.assertEqual(op.suma(1), 4)
        
    def test_roznica(self):
        op = Operacje()
        self.assertEqual(op.roznica(2, 1), 1)
        self.assertEqual(op.roznica(2), -2)
        self.assertEqual(op.roznica(), 6)
        
        op.roznica(2) 
        wynik=op.roznica() 
        self.assertEqual(wynik, 6)

        with self.assertRaises(TypeError):
            op.roznica(3, 2, 1)
        
        op['roznica'] = [7, 2, 3]
        
        self.assertEqual(op.roznica(1), -6)


    def test__setitem__(self):
        op = Operacje()
        with self.assertRaises(TypeError):
            op['suma'] = ['a','b', 'c']

if __name__ == '__main__':
    unittest.main()