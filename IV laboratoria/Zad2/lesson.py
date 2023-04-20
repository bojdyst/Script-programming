from day import Day
from term import Term

class Lesson:
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.full_time = term._Term__day == Day.MON or\
                        term._Term__day == Day.TUE or\
                        term._Term__day == Day.WED or\
                        term._Term__day == Day.THU or\
                        term._Term__day == Day.FRI and term.hour < 17

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

        return f"{self.name} ({self.term})\n{school_year} studiów {'stacjonarnych' if self.full_time else 'niestacjonarnych'}\nProwadzący: {self.teacherName}"

    def earlierDay(self):
        raw_hours = self.term.duration // 60
        raw_minutes = self.term.duration % 60
        if self.term.minute + raw_minutes > 59:
            raw_hours += 1
            raw_minutes -= 60

        end_hour = self.term.hour + raw_hours
        end_minute = self.term.minute + raw_minutes

        if self.full_time:
            if self.term._Term__day != Day.MON and (self.term.hour >= 8 and ((end_hour == 20 and end_minute == 0) or end_hour < 20)):
                self.term.day = Day(self.term.day.value - 1)
                return True
            else: 
                return False
        else:
            if (self.term._Term__day != Day.FRI and (self.term.hour >= 17 and ((end_hour == 20 and end_minute == 0) or end_hour < 20))) and (self.term._Term__day == Day.SAT and (self.term.hour >= 17 and ((end_hour == 20 and end_minute == 0) or end_hour < 20)) or (self.term._Term__day != Day.SAT and self.term.hour >= 8 and ((end_hour == 20 and end_minute == 0) or end_hour < 20))):
                self.term.day = Day(self.term.day.value - 1)
                return True
            else: 
                return False
            
    def laterDay(self):
        raw_hours = self.term.duration // 60
        raw_minutes = self.term.duration % 60
        if self.term.minute + raw_minutes > 59:
            raw_hours += 1
            raw_minutes -= 60

        end_hour = self.term.hour + raw_hours
        end_minute = self.term.minute + raw_minutes

        if self.full_time:
            if (self.term._Term__day != Day.FRI and self.term._Term__day != Day.THU and (self.term.hour >= 8 and ((end_hour == 20 and end_minute == 0) or end_hour < 20))) or (self.term._Term__day == Day.THU and (self.term.hour >= 8 and ((end_hour == 17 and end_minute == 0) or end_hour < 17))):
                self.term.day = Day(self.term.day.value + 1)
                return True
            else: 
                return False
        else:
            if (self.term._Term__day == Day.FRI and (self.term.hour >= 17 and ((end_hour == 20 and end_minute == 0) or end_hour < 20)) or (self.term._Term__day != Day.FRI and self.term.hour >= 8 and ((end_hour == 20 and end_minute == 0) or end_hour < 20))):
                self.term.day = Day(self.term.day.value + 1)
                return True
            else: 
                return False

    def earlierTime(self):
        raw_hours = self.term.duration // 60
        raw_minutes = self.term.duration % 60
        if self.term.minute - raw_minutes < 0:
            raw_hours += 1
            raw_minutes -= 60

        start_hour = self.term.hour - raw_hours
        start_minute = self.term.minute - raw_minutes

        if self.full_time:
            if start_hour >= 8 and ((self.term.hour == 20 and self.term.minute == 0) or self.term.hour < 20):
                self.term.hour = start_hour
                self.term.minute = start_minute
                return True
            else:
                return False
        else:
            if self.term._Term__day == Day.FRI and (start_hour < 17):
                return False
            elif start_hour >= 8 and ((self.term.hour == 20 and self.term.minute == 0) or self.term.hour < 20):
                self.term.hour = start_hour
                self.term.minute = start_minute
                return True
            else:
                return False

    def laterTime(self):
        raw_hours = self.term.duration // 60
        raw_minutes = self.term.duration % 60
        if self.term.minute + raw_minutes < 59:
            raw_hours += 1
            raw_minutes -= 60
        if self.term.minute + raw_minutes < 0:
            raw_hours -= 1
            raw_minutes += 60
        elif self.term.minute + raw_minutes > 59:
            raw_hours += 1
            raw_minutes -= 60

        start_hour = self.term.hour + raw_hours
        start_minute = self.term.minute + raw_minutes

        raw_hours1 = start_hour + raw_hours
        raw_minutes1 = start_minute + raw_minutes
        if start_minute + raw_minutes1 > 59:
            raw_hours1 += 1
            raw_minutes1 -= 60

        end_hour = raw_hours1 
        end_minute = raw_minutes1

        if self.full_time:
            if ((self.term.hour <= 17 and self.term._Term__day == Day.FRI and (end_hour < 17 or end_hour == 17 and end_minute == 0))) or (start_hour >= 8 and ((end_hour == 20 and end_minute == 0) or end_hour < 20)):
                self.term.hour = start_hour
                self.term.minute = start_minute
                return True
            else:
                return False
        else:
            if start_hour >= 8 and ((end_hour == 20 and end_minute == 0) or end_hour < 20) or self.term._Term__day == Day.FRI and (start_hour >= 17 and (end_hour < 20 or end_hour == 20 and end_minute == 0)):
                self.term.hour = start_hour
                self.term.minute = start_minute
                return True
            else:
                return False