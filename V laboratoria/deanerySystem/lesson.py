from term import Term
from day import Day

class Lesson:
    def __init__(self, term, name, teacherName, year, timetable=None):
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__fullTime = term._Term__day == Day.MON or\
                        term._Term__day == Day.TUE or\
                        term._Term__day == Day.WED or\
                        term._Term__day == Day.THU or\
                        term._Term__day == Day.FRI and term.hour < 17
        self.timetable = None
        if timetable is not None and timetable.put(self):
            self.timetable = timetable

    def earlierDay(self):
        newDay = Day(self.term.day.value - 1)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(Term(newDay,self.term.hour,self.term.minute,self.term.duration), self.fullTime):
            self.term.day = newDay
            return True
        return False

    def laterDay(self):
        newDay = Day(self.term.day.value +1)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(Term(newDay, self.term.hour, self.term.minute, self.term.duration), self.fullTime):
            self.term.day = newDay
            return True
        return False

    def earlierTime(self, duration):
        new_term = findNewTermEarlier(self.term, duration)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        return False

    def laterTime(self, duration):
        new_term = findNewTermLater(self.term, duration)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        return False

    def __str__(self):
        match self.year:
            case 1:
                school_year = "Pierwszy rok"
            case 2:
                school_year = "Drugi rok"
            case 3:
                school_year = "Trzeci rok"
            case 4:
                school_year = "Czwarty rok"
            case 5:
                school_year = "Piąty rok"

        return f"{self.__name} ({self.__term})\n{school_year} studiów {'stacjonarnych' if self.__full_time else 'niestacjonarnych'}\nProwadzący: {self.__teacherName}"

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, val):
        self.__term = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, val):
        self.__teacherName = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        self.__year = val

    @property
    def fullTime(self):
        return self.__fullTime

    @fullTime.setter
    def fullTime(self, val):
        self.__fullTime = val

def findNewTermEarlier(term, duration):
    day = term.day
    dur = term.duration
    hours = duration // 60
    new_hours = term.hour - hours
    minutes = duration % 60
    new_minutes = term.minute - minutes
    if new_minutes < 0:
        new_minutes += 60
        new_hours -= 1
    return Term(day, new_hours, new_minutes, dur)

def findNewTermLater(term, duration):
    day = term.day
    dur = term.duration
    hours = duration // 60
    new_hours = term.hour + hours
    minutes = duration % 60
    new_minutes = term.minute + minutes
    if new_minutes >= 60:
        new_minutes -= 60
        new_hours += 1
    return Term(day, new_hours, new_minutes, dur)