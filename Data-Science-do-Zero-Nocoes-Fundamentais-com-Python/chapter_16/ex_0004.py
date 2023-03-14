from ex_0001 import Time, print_time
from ex_0003 import int_to_time, time_to_int

def mul_time(time, n):
    seconds = time_to_int(time)
    return int_to_time(seconds*n)
def time_per_mile(time, distance):
    seconds = time_to_int(time)
    return int_to_time(seconds/distance)
if __name__ == "__main__":
    time = Time()
    time.hour = 00
    time.minute = 30
    time.second = 00
    time = time_per_mile(time, 2)
    print_time(time)