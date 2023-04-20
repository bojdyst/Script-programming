import unittest
from term import Term
from day import Day

class MiniTest(unittest.TestCase):

    def test_proper_display_of_term(self):
        self.assertEqual(str(Term(Day.TUE, 9, 45)), "Wtorek 9:45 [90]")
        self.assertEqual(str(Term(Day.WED, 10, 15)), "Środa 10:15 [90]")
        self.assertEqual(str(Term(Day.SUN, 21, 10)), "Niedziela 21:10 [90]")
        self.assertEqual(str(Term(Day.FRI, 0, 00)), "Piątek 0:00 [90]")
        self.assertEqual(str(Term(Day.MON, 14, 33)), "Poniedziałek 14:33 [90]")
        self.assertEqual(str(Term(Day.THU, 17, 1)), "Czwartek 17:01 [90]")

    def test_earlier_than(self):
        self.assertTrue(Term(Day.TUE, 9, 45).earlierThan(Term(Day.WED, 10, 15)))
        self.assertTrue(Term(Day.MON, 15, 00).earlierThan(Term(Day.MON, 15, 1)))
        self.assertFalse(Term(Day.TUE, 9, 45).earlierThan(Term(Day.MON, 10, 15)))
        self.assertFalse(Term(Day.SUN, 17, 00).earlierThan(Term(Day.FRI, 0, 00)))
        self.assertTrue(Term(Day.SAT, 7, 00).earlierThan(Term(Day.SUN, 2, 33)))

    def test_later_than(self):
        self.assertFalse(Term(Day.TUE, 9, 45).laterThan(Term(Day.WED, 10, 15)))
        self.assertFalse(Term(Day.MON, 15, 00).laterThan(Term(Day.MON, 15, 1)))
        self.assertTrue(Term(Day.TUE, 9, 45).laterThan(Term(Day.MON, 10, 15)))
        self.assertTrue(Term(Day.SUN, 17, 00).laterThan(Term(Day.FRI, 0, 00)))
        self.assertFalse(Term(Day.SAT, 7, 00).laterThan(Term(Day.SUN, 2, 33)))

    def test_equals(self):
        self.assertTrue(Term(Day.TUE, 9, 45).equals(Term(Day.TUE, 9, 45)))
        self.assertTrue(Term(Day.SUN, 0, 55).equals(Term(Day.SUN, 0, 55)))
        self.assertFalse(Term(Day.SUN, 0, 55).equals(Term(Day.SUN, 0, 54)))
        self.assertFalse(Term(Day.MON, 14, 37).equals(Term(Day.TUE, 14, 37)))

if __name__ == '__main__':
    unittest.main()