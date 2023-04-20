from typing import List
from lesson import Lesson
from action import Action
from Break import Break
from lines import Lines
from BasicTimetable import BasicTimetable
from term import Term

class TimetableWithBreakes(BasicTimetable):
    def __init__(self, breaks: List[Break]):
        self.timetable = {}
        self.breaks = sorted(breaks, key=lambda x: x.startTime())
        self.timetableLines = self.makeTimetableLines()
        self.skipBrakes = True

    def __str__(self):
        days = ['', 'Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek', 'Sobota', 'Niedziela']
        result = ""
        column = 14
        for day in days:
            result += f'{day:^13}*'
        linebreak = ""*column + "*"*column*8 + "\n"
        result += "\n"
        result += linebreak
        for line in self.timetableLines:
            result += str(line)
            result += linebreak
        return result

    def makeTimetableLines(self):
        lines = []
        start = (8, 0)
        for brake in self.breaks:
            lines.append(Lines(start, brake.startTime(), False, self))
            lines.append(Lines(brake.startTime(), brake.endTime(), True, self))
            start = brake.endTime()
        lines.append(Lines(start, (20, 0), False, self))
        return lines

##########################################################
    def busy(self, term: Term) -> bool:
        if term in self.timetable:
            return True
        for line in self.timetableLines:
            if line.start == term.startTime():
                if line.duration == term.duration:
                    return False
                else:
                    return True
        return True

##########################################################
    def put(self, lesson: Lesson) -> bool:
        if not self.can_be_transferred_to(lesson.term, lesson.fullTime):
            return False
        self.timetable[Term(lesson.term.day, lesson.term.hour, lesson.term.minute, lesson.term.duration)] = lesson
        return True

##########################################################
    def perform(self, actions: List[Action]):
        lessons_quantity = len(self.timetable.values())
        i = 0
        for action in actions:
            lesson = list(self.timetable.values())[i%lessons_quantity]
            term = Term(lesson.term.day, lesson.term.hour, lesson.term.minute, lesson.term.duration)
            if action == Action.DAY_LATER:
                allow = lesson.laterDay()
            elif action == Action.DAY_EARLIER:
                allow = lesson.earlierDay()
            elif action == Action.TIME_LATER:
                next = False
                breakTime = 0
                for line in self.timetableLines:
                    if next:
                        breakTime = line.duration
                        break
                    # print(term.startTime(), line.start)
                    if term.startTime() == line.start:
                        next = True
                    # print(breakTime)
                # print(breakTime)
                allow = lesson.laterTime(breakTime + lesson.term.duration)
                # print(allow)
            elif action == Action.TIME_EARLIER:
                if not self.skipBreaks:
                    continue
                breakTime = 0
                curr = 0
                for line in self.timetableLines:
                    curr = line.duration
                    if term.startTime() == line.start:
                        breakTime = curr
                        break
                allow = lesson.earlierTime(breakTime + lesson.term.duration)
            if allow:
                self.timetable.pop(term)
                self.timetable[Term(lesson.term.day, lesson.term.hour, lesson.term.minute, lesson.term.duration)] = lesson

##########################################################

    def get(self, term: Term):
        return self.timetable.get(term)