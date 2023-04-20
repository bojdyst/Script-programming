from day import Day

class Term():
    def __init__(self, __day, hour, minute, duration = 90):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.__day = __day

    def __str__(self):
        return "{day:} {hour:}:{minute:02d} [{duration:}]".format(day = self._Term__day, hour = self.hour, minute = self.minute, duration = self.duration)
    
    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __gt__(self, termin):
        return self.laterThan(termin)

    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    def __eq__(self, termin):
        return self.equals(termin)

    def __sub__(self, termin):
        return Term(termin.__day, termin.hour, termin.minute, ((self.hour - termin.hour)*60 + (self.minute - termin.minute) + self.duration))

    def earlierThan(self, termin):
        if self._Term__day.difference(termin._Term__day) < 0:
            return True
        elif self._Term__day.difference(termin._Term__day) > 0:
            return False
        else:
            if self.hour < termin.hour:
                return True
            elif self.hour > termin.hour:
                return False
            else:
                if self.minute < termin.minute:
                    return True
                elif self.minute > termin.minute:
                    return False

    def laterThan(self, termin):
        if self._Term__day.difference(termin._Term__day) > 0:
            return True
        elif self._Term__day.difference(termin._Term__day) < 0:
            return False
        else:
            if self.hour > termin.hour:
                return True
            elif self.hour < termin.hour:
                return False
            else:
                if self.minute > termin.minute:
                    return True
                elif self.minute < termin.minute:
                    return False

    def equals(self, termin):
        if self._Term__day.difference(termin._Term__day) == 0 and self.hour == termin.hour and self.minute == termin.minute and self.duration == termin.duration:
            return True
        else:
            return False