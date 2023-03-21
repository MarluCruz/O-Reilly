class Time:

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.__add_time(other)
        else:
            return self.__increment(other)
                
    def __add_time(self, other):   
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def __increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
if __name__ == "__main__":

    start = Time(9, 45, 00)
    duration = 5700
    actualTime = start + duration
    actualTime.print_time()
