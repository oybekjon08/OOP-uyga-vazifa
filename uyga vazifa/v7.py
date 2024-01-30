class Time:
    def __init__ (self, second:int, minute:int, hour:int):
        self.second=second
        self.minute=minute
        self.hour=hour
    def get_hour(self):
        return  self.hour
    def get_minute(self):
        return self.minute
    def get_second(self):
        return self.second
    def set_hour(self, newHour:int) ->None :
        self.hour=newHour
    def set_minute(self, newMinute:int) ->None :
        self.minute=newMinute
    def set_second(self, newSecond:int) ->None :
        self.second=newSecond
    def to_string(self):
        return f"""
    time: %02d : %02d : %02d
    """ %(self.second, self.minute, self.hour)
    def next_second(self):
        print("next second ", (self.second+1))
    def perviousSecond(self):
        print("pervious second", (self.second-1))
a=Time(20, 30, 12)
print(a.to_string())
a.next_second()
a.perviousSecond()
a.set_hour(11)
a.set_minute(23)
a.set_second(25)
print(f"New time {a.to_string()}")
