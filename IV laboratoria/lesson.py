from day import Day
from term import Term

class Lesson:
    def __init__(self, timetable, term, name, teacherName, year):
        self.__timetable = timetable
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__full_time = term._Term__day == Day.MON or\
                        term._Term__day == Day.TUE or\
                        term._Term__day == Day.WED or\
                        term._Term__day == Day.THU or\
                        term._Term__day == Day.FRI and term.hour < 17

    @property
    def term(self):
        return self.__term
    
    @term.setter
    def term(self, value):
        self.__term = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def tenamerm(self, value):
        self.__name = value

    @property
    def teacherName(self):
        return self.__teacherName
    
    @teacherName.setter
    def teacherName(self, value):
        self.__teacherName = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def full_time(self):
        return self.__full_time

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

    def earlierDay(self):
        if self.term.day.value == 1:
            return False
        else:
            self.term.day = Day(self.term.day.value - 1)

        if self.__timetable.can_be_transferred_to(self.term, self.__full_time):
            return True
        else:
            self.term.day = Day(self.term.day.value + 1)
            return False
            
    def laterDay(self):
        if self.term.day.value + 1 == 8:
            return False
        else:
            self.term.day = Day(self.term.day.value + 1)

        if self.__timetable.can_be_transferred_to(self.term, self.__full_time):
            return True
        else:
            self.term.day = Day(self.term.day.value - 1)
            return False

    def earlierTime(self):
        raw_hours = self.term.duration // 60
        raw_minutes = self.term.duration % 60
        if self.term.minute - raw_minutes < 0:
            raw_hours += 1
            raw_minutes -= 60

        start_hour = self.term.hour - raw_hours
        start_minute = self.term.minute - raw_minutes

        self.term.hour = start_hour
        self.term.minute = start_minute

        if self.__timetable.can_be_transferred_to(self.term, self.__full_time):
            return True
        else:
            self.term.hour = start_hour + raw_hours
            self.term.minute = start_minute + raw_minutes
            return False
        

    def laterTime(self):
        raw_hours = self.term.duration // 60
        raw_minutes = self.term.duration % 60
        if self.term.minute + raw_minutes > 59:
            raw_hours += 1
            raw_minutes -= 60

        start_hour = self.term.hour + raw_hours
        start_minute = self.term.minute + raw_minutes

        raw_hours1 = start_hour + raw_hours
        raw_minutes1 = start_minute + raw_minutes
        if start_minute + raw_minutes1 > 59:
            raw_hours1 += 1
            raw_minutes1 -= 60

        self.term.hour = start_hour
        self.term.minute = start_minute

        if self.__timetable.can_be_transferred_to(self.term, self.__full_time):
            return True
        else:
            self.term.hour = start_hour - raw_hours
            self.term.minute = start_minute - raw_minutes
            return False