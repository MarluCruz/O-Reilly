class Time:
    """ Represents the time of  day
        attributes: hour, minute, second"""
def print_time(time):
    print('(%.2d:%.2d:%.2d)' % (time.hour, time.minute, time.second))
def is_after(t1, t2):
    return (t1.hour < t2.hour) or ((t1.hour == t2.hour) and (t1.minute < t2.minute)) or ((t1.hour == t2.hour) and (t1.minute == t2.minute) and (t1.second < t2.second) )

if __name__ == '__main__':
    time = Time()
    time.hour = 21
    time.minute = 37
    time.second = 46
    time2 = Time()
    time2.hour = 21
    time2.minute = 37
    time2.second = 4
    print(is_after(time, time2))