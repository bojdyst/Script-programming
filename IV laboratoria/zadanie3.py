import unittest
from day import Day
from term import Term
from lesson import Lesson
from TimetableWithoutBreaks import TimetableWithoutBreaks


class Test_TestDeanerySystem(unittest.TestCase):
    def test1(self):
        timetable = TimetableWithoutBreaks()
        lesson1 = Lesson(timetable, Term(Day.TUE, 8, 00), "Programowanie", "Polak", 1)
        lesson2 = Lesson(timetable, Term(Day.MON, 9, 30), "WF", "Lewandowski", 2)
        lesson3 = Lesson(timetable, Term(Day.FRI, 15, 30), "Analiza", "Nowak", 3)

        timetable.list_of_lessons.clear()

        timetable.put(lesson1)
        timetable.put(lesson2)
        timetable.put(lesson3)

        # print(str(timetable))

        timetable.perform(timetable.parse(["d-", "t-", "d-", "t+", "d+", "t-", "t+", "d+", "t-", "d+", "d+", "t-", "d+", "t+", "t-", "d+"]))

        # print(str(timetable))

        self.assertEqual(str(timetable.list_of_lessons[0].term), str(Term(Day.WED, 9, 30)))
        self.assertEqual(str(timetable.list_of_lessons[1].term), str(Term(Day.THU, 9, 30)))
        self.assertEqual(str(timetable.list_of_lessons[2].term), str(Term(Day.THU, 11, 00)))
        
        self.assertFalse(timetable.busy1(Term(Day.SUN, 8, 00)))
        self.assertTrue(timetable.busy1(Term(Day.WED, 9, 30)))
        
        self.assertEqual(timetable.get(Term(Day.THU, 9, 30)), lesson2)
        self.assertEqual(timetable.get(Term(Day.THU, 11, 00)), lesson3)
        

    def test2(self):
        timetable = TimetableWithoutBreaks()
        lesson1 = Lesson(timetable, Term(Day.FRI, 8, 00), "Angielski", "Smith", 1)
        lesson2 = Lesson(timetable, Term(Day.FRI, 18, 30), "WDZC", "Ptak", 2)
        lesson3 = Lesson(timetable, Term(Day.SAT, 17, 00), "Polski", "Brzęszyszczykiewicz", 2)

        timetable.list_of_lessons.clear()

        timetable.put(lesson1)
        timetable.put(lesson2)
        timetable.put(lesson3)

        # print(str(timetable))

        timetable.perform(timetable.parse(["d+", "d+", "d-", "t+", "t-", "t-"]))

        # print(str(timetable))

        self.assertEqual(str(timetable.list_of_lessons[0].term), str(Term(Day.FRI, 9, 30)))
        self.assertEqual(str(timetable.list_of_lessons[1].term), str(Term(Day.SAT, 17, 00)))
        self.assertEqual(str(timetable.list_of_lessons[2].term), str(Term(Day.FRI, 17, 00)))
        
        self.assertFalse(timetable.busy1(Term(Day.SUN, 8, 00)))
        self.assertTrue(timetable.busy1(Term(Day.FRI, 9, 30)))
        
        self.assertEqual(timetable.get(Term(Day.SAT, 17, 00)), lesson2)
        self.assertEqual(timetable.get(Term(Day.FRI, 17, 00)), lesson3)

if __name__ == '__main__':
    unittest.main()
