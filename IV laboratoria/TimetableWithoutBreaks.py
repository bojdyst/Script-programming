from typing import List
from day import Day
from term import Term
from lesson import Lesson
from action import Action

class TimetableWithoutBreaks:
    list_of_lessons = []

    """ Class containing a set of operations to manage the timetable """

##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
fullTime : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""  
    
        if self.busy(term):
            return False
        
        if fullTime:
            if 0 < term.day.value and term.day.value < 6 and 7 < term.hour and term.hour < 20:
                return True
            elif term.day.value == 5 and 7 < term.hour and term.hour < 17:
                return True
        else:
           if term.day.value in [6,7] and 7 < term.hour and term.hour < 20:
               return True
           if term.day.value == 5 and 16 < term.hour and term.hour < 20:
               return True
        return False
                    

##########################################################

    def busy(self, term: Term) -> bool:

        i = 0

        if term.day.value == 0:
            term.day.value = 7

        for lesson in self.list_of_lessons:
            if lesson.term.day == term.day and lesson.term.hour == term.hour and lesson.term.minute == term.minute:
                i += 1
        if i > 1:
            return True
        else:
            return False


 ##########################################################

    def busy1(self, term: Term) -> bool:
        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
        """

        for lesson in self.list_of_lessons:
            if lesson.term.day == term.day and lesson.term.hour == term.hour and lesson.term.minute == term.minute:
                return True
        return False

 ##########################################################

    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """
        
        self.list_of_lessons.append(lesson)

        if lesson in self.list_of_lessons:
            return True
        else:
            return False

##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """

        tab = []
        for action in actions:
            if action == "d+":
                tab.append(Action.DAY_LATER)
            elif action == "d-":
                tab.append(Action.DAY_EARLIER)
            elif action == "t+":
                tab.append(Action.TIME_LATER)
            elif action == "t-":
                tab.append(Action.TIME_EARLIER)

        return tab 

##########################################################

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """

        i = 0

        for action in actions:
            if action == Action.DAY_EARLIER:
                self.list_of_lessons[i].earlierDay()
            elif action == Action.DAY_LATER:
                self.list_of_lessons[i].laterDay()
            elif action == Action.TIME_EARLIER:
                self.list_of_lessons[i].earlierTime()
            elif action == Action.TIME_LATER:
                self.list_of_lessons[i].laterTime()
                
            i = (i + 1) % len(self.list_of_lessons)
            
##########################################################

    def get(self, term: Term) -> Lesson:
        """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """

        for lesson in self.list_of_lessons:
            if lesson.term.day == term.day and lesson.term.hour == term.hour and lesson.term.minute == term.minute:
                return lesson

    def __str__(self):
        s = f'{"":<14}| '
        
        for i in range(1, 8):
            s += f'{str(Day(i)):<17}|  '
        s += "\n"
        for i in range(0, 14):
            s += "-"
        s += "|"
        
        for i in range(1, 8):
            for j in range(0, 19):
                if i == 1 and j == 0:
                    continue
                s += "-"
            s += "|"
        s += "\n"
        
        duration = 90
        
        h = 8
        m = 0
        ho = duration // 60
        mo = duration % 60
        
        while h < 20:
            hd = h + ho
            md = m + mo
            
            if md >= 60:
                hd += 1
                md -= 60
                
            s += f'{h:02d}:{m:02d}-{hd:02d}:{md:02d}   | '
            
            for i in range(1, 8):
                found = False
                for lesson in self.list_of_lessons:
                    if lesson.term.day.value == i and lesson.term.hour == h and lesson.term.minute == m:
                        s += f'{lesson.name:<17}|  '
                        found = True
                        break
                
                if not found:
                    s += f'{"":<17}|  '
            
            if h != 18:
                s += f'\n{"":<14}|{"":<18}|{"":<19}|{"":<19}|{"":<19}|{"":<19}|{"":<19}|{"":<19}|\n'
            else:
                s += "\n\n"
            
            h = hd
            m = md
        
        return s