import datetime
def weekday():
    time = datetime.date.weekday(datetime.date.today())
    if time == 0:
        return 'Monday'
    elif time == 1:
        return 'Tuesday'
    elif time == 2:
        return 'Wednesdays'
    elif time == 3:
        return 'Thursday'
    elif time == 4:
        return 'Friday'
    elif time == 5:
        return 'Saturday'
    elif time == 6:
        return 'Sunday'

if __name__ == "__main__":
    day = weekday()
    print('Today is {}'.format(day))
