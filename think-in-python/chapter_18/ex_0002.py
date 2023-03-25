class Time:
    """ Represents the time of  day
        attributes: hour, minute, second"""
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def print_time(self):
        print(str(self))
    

    
    def __str__(self):
        return'(%.2d:%.2d:%.2d)' % (self.hour, self.minute, self.second)
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def __lt__(self, other):
        t1 = self.time_to_int()
        t2 = other.time_to_int()
        return t1 < t2
    


if __name__  == '__main__': 
    time = Time(9, 45, 56)
    time2 = Time (12, 0, 0)

    print(time < time2)
    