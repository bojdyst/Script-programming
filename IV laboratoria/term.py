from day import Day

class Term():
    def __init__(self, __day, hour, minute, duration = 90):
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration
        self.__day = __day

    @property
    def day(self):
        return self.__day
        
    @day.setter
    def day(self, value):
        self.__day = value
        
    @property
    def hour(self):
        return self.__hour
        
    @hour.setter
    def hour(self, value):
        self.__hour = value
        
    @property
    def minute(self):
        return self.__minute
        
    @minute.setter
    def minute(self, value):
        self.__minute = value
        
    @property
    def duration(self):
        return self.__duration
        
    @duration.setter
    def duration(self, value):
        self.__duration = value

    def __str__(self):
        raw_hours = self.duration // 60
        raw_minutes = self.duration % 60
        if self.minute + raw_minutes > 59:
            raw_hours += 1
            raw_minutes -= 60
        return "{day:} {hour:}:{minute:02d}-{hour1:}:{minute1:02d}".format(day = self._Term__day, hour = self.hour, minute = self.minute, hour1 = (self.hour + raw_hours), minute1 = (self.minute + raw_minutes))
    
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