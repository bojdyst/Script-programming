import zadanie2
import unittest

class Test_Correctness(unittest.TestCase):
    def test_ala(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("Ala"), (["Ala"], []))
        
    def test_ma(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("ma"), (["ma"], []))
        
    def test_1kota(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("1kota"), (["kota"], ["1"]))
        
    def test_oraz(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("oraz"), (["oraz"], []))
        
    def test_psów20(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("psów20"), (["psów"], ["20"]))
        
    def test_ponadto(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("ponadto"), (["ponadto"], []))
        
    def test_50(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("50"), ([], ["50"]))
        
    def test_chomików(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("chomików"), (["chomików"], []))
        
    def test_123ala456ma789kota(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("123ala456ma789kota"), (["ala", "ma", "kota"], ['123', '456', '789']))

    def test_special_chars(self):
         self.assertEqual(zadanie2.divide_text_on_str_int("..//##$%^*__-",), ([], []))

    def test_special_chars_and_str_int(self):
        self.assertEqual(zadanie2.divide_text_on_str_int("{??//#ala#$%^*_123_-",), (["ala"], ["123"]))


if __name__ == "__main__":
    unittest.main()