class Time:

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.seconds = self.time_to_int(hour, minute, second)
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
                
    def add_time(self, other):   
        return Time(0, 0 , self.seconds + other.seconds)
    
    def increment(self, seconds):
        return Time(0,0, self.seconds + seconds)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)
    
    def print_time(self):
        print(str(self))
    
    def __str__(self):
        """Returns a string representation of the time."""
        time = self.int_to_time()
        return '%.2d:%.2d:%.2d' % (time[0], time[1], time[2])
    
    def time_to_int(self , hour, minute, second):
        minutes = hour * 60 + minute
        seconds = minutes * 60 + second
        return seconds
    
    def int_to_time(self):
        hour = 0
        minute = 0
        second = 0
        minute, second = divmod(self.seconds, 60)
        hour, minute = divmod(minute, 60)
        return hour, minute, second

    
    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.seconds
    
    """
    def is_valid(self):
        Checks whether a Time object satisfies the invariants.
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True"""

    
def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)

    
if __name__ == "__main__":

    main()