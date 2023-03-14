from ex_0001 import Time, print_time
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(time, seconds):
    seconds = time_to_int(time) + seconds
    return int_to_time(seconds)

if __name__ == '__main__':
    time = Time() 
    time.hour = 21
    time.minute = 37
    time.second = 46
    time = increment(time, 3600)
    print_time(time)
