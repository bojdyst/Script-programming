from day import Day

class Term():
    def __init__(self, __day, hour, minute):
        self.hour = hour
        self.minute = minute
        self._duration = 90
        self.__day = __day

    def __str__(self):
        return "{day:} {hour:}:{minute:02d} [{duration:}]".format(day = self._Term__day, hour = self.hour, minute = self.minute, duration = self._duration)
    
    def earlierThan(self, termin):
        if self._Term__day.difference(termin._Term__day) > 0:
            return True
        elif self._Term__day.difference(termin._Term__day) < 0:
            return False
        else:
            if self.hour == termin.hour:
                if self.minute < termin.minute:
                    return True
                else:
                    return False
            else: 
                return False

    def laterThan(self, termin):
        if self._Term__day.difference(termin._Term__day) < 0:
            return True
        elif self._Term__day.difference(termin._Term__day) > 0:
            return False
        else:
            if self.hour > termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute > termin.minute:
                    return True
                else:
                    return False
            else: 
                return False

    def equals(self, termin):
        if self._Term__day.difference(termin._Term__day) == 0 and self.hour == termin.hour and self.minute == termin.minute and self._duration == termin._duration:
            return True
        else:
            return False