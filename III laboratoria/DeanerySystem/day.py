from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def __str__(self):
        match self.value:
            case 1:
                return "Poniedziałek"
            case 2:
                return "Wtorek"
            case 3:
                return "Środa"
            case 4:
                return "Czwartek"
            case 5:
                return "Piątek"
            case 6:
                return "Sobota"
            case 7:
                return "Niedziela"

    def difference(self, day):
        differ = day.value - self.value
        
        if differ > -3:
            if differ > 3:
                return differ - 7  
            else:
                return differ
        else:
            return differ + 7 

def nthDayFrom(n, day):
    new_day = day.value + n
    if new_day < 1:
        new_day = new_day%7 + 7
    elif new_day > 7:
        new_day = new_day%7
    return Day(new_day)