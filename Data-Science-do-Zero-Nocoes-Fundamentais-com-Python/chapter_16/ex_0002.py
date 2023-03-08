from ex_0001 import Time, print_time

def increment(time, seconds):
    time.second += seconds

    if time.second >= 3600:
        if (((((time.second / 60) / 60) - int((time.second / 60) / 60))*60)*60) >= 60: 
            time.minute += int(((time.second / 60) - int(time.second / 60))  * 60)
        else:
            time.hour += int((time.second / 60) / 60)
            time.second = int((((time.second / 3600) - int(time.second / 3600)) *60)*60)
        if time.minute >= 60:
            time.hour += int(time.minute / 60)
            time.minute = int(((time.minute / 60) - int(time.minute / 60)) * 60)
    if time.second >= 60:
        time.minute += time.second / 60
        time.second = int((time.second % 60) * 60)
        if time.minute >= 60:
            time.hour += time.minute / 60
            time.minute = int((time.minute % 60) *60)

if __name__ == "__main__":
    time = Time()
    time.hour = 21
    time.minute = 37
    time.second = 46
    increment(time, 7200)
    print_time(time)