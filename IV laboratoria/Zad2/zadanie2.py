from day import Day
from term import Term
from lesson import Lesson
import unittest

class Test_TestDeanerySystem(unittest.TestCase):
    def test_earlierDay(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertFalse(lesson1.earlierDay())
        self.assertFalse(lesson2.earlierDay())
        self.assertTrue(lesson3.earlierDay())
        self.assertFalse(lesson4.earlierDay())
        self.assertTrue(lesson5.earlierDay())

        self.assertEqual(str(lesson1), "Programowanie (Poniedziałek 8:30-10:00)\nDrugi rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson2), "Programowanie1 (Piątek 17:30-19:30)\nTrzeci rok studiów niestacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson3), "Programowanie2 (Środa 17:30-18:01)\nCzwarty rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson4), "Programowanie3 (Sobota 8:05-8:09)\nPiąty rok studiów niestacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson5), "Programowanie3 (Piątek 17:00-17:45)\nPiąty rok studiów niestacjonarnych\nProwadzący: Polak")


    def test_laterDay(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertTrue(lesson1.laterDay())
        self.assertTrue(lesson2.laterDay())
        self.assertFalse(lesson3.laterDay())
        self.assertTrue(lesson4.laterDay())
        self.assertTrue(lesson5.laterDay())

        self.assertEqual(str(lesson1), "Programowanie (Wtorek 8:30-10:00)\nDrugi rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson2), "Programowanie1 (Sobota 17:30-19:30)\nTrzeci rok studiów niestacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson3), "Programowanie2 (Czwartek 17:30-18:01)\nCzwarty rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson4), "Programowanie3 (Niedziela 8:05-8:09)\nPiąty rok studiów niestacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson5), "Programowanie3 (Niedziela 17:00-17:45)\nPiąty rok studiów niestacjonarnych\nProwadzący: Polak")


    def test_laterTime(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 29), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 10, 15, 20), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertTrue(lesson1.laterTime())
        self.assertFalse(lesson2.laterTime())
        self.assertTrue(lesson3.laterTime())
        self.assertTrue(lesson4.laterTime())
        self.assertTrue(lesson5.laterTime())

        self.assertEqual(str(lesson1), "Programowanie (Poniedziałek 10:00-11:30)\nDrugi rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson2), "Programowanie1 (Piątek 17:30-19:30)\nTrzeci rok studiów niestacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson3), "Programowanie2 (Czwartek 17:59-18:28)\nCzwarty rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson4), "Programowanie3 (Sobota 10:35-10:55)\nPiąty rok studiów niestacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson5), "Programowanie3 (Sobota 17:45-18:30)\nPiąty rok studiów niestacjonarnych\nProwadzący: Polak")


    def test_ealierTime(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertFalse(lesson1.earlierTime())
        self.assertFalse(lesson2.earlierTime())
        self.assertTrue(lesson3.earlierTime())
        self.assertTrue(lesson4.earlierTime())
        self.assertTrue(lesson5.earlierTime())


    def test_str(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Matematyka", "Nowak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "WF", "Lewandowski", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)

        self.assertEqual(str(lesson1), "Programowanie (Poniedziałek 8:30-10:00)\nDrugi rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson2), "Matematyka (Piątek 17:30-19:30)\nTrzeci rok studiów niestacjonarnych\nProwadzący: Nowak")
        self.assertEqual(str(lesson3), "WF (Czwartek 17:30-18:01)\nCzwarty rok studiów stacjonarnych\nProwadzący: Lewandowski")
        self.assertEqual(str(lesson4), "Programowanie3 (Sobota 8:05-8:09)\nPiąty rok studiów niestacjonarnych\nProwadzący: Polak")

if __name__ == '__main__':
    unittest.main()