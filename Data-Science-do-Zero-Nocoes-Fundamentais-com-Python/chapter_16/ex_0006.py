from datetime import datetime, timedelta, date

def age(birthday):
    today = date.today()
    thisAge = today.year - birthday.year
    if (today.month >= birthday.month):
        if (today.month == birthday.month) and (today.day < birthday.day):
            return thisAge -1
        else:
            return thisAge
    else:
        return thisAge -1
    
def mbity(birthday):#MyBirthdayIsThisYear
    today = datetime.today()
    if (today.month >= birthday.month):
        if (today.month == birthday.month) and (today.day < birthday.day):
            return True
        else:
            return False
    else:
        return True
    
def date_to_days(date):
    thisdict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    newDate = date
    days = 0
    for x in range(1, date.month):
        days += thisdict.get(x, None)
    days += (date.year*365) + int(date.year/4) + date.day
    newDate = timedelta(days, date.second, date.microsecond, 0, date.minute, date.hour)
    return newDate



def my_next_birthday(birthday):
    todayDateTime = datetime.today()
    if mbity(birthday):
        nextBirthdayDate = datetime(todayDateTime.year, birthday.month, birthday.day, birthday.hour, birthday.minute, birthday.second)
        return nextBirthdayDate - todayDateTime
    else:
        nextBirthdayDate = datetime((todayDateTime.year+1), birthday.month, birthday.day, birthday.hour, birthday.minute, birthday.second)
        return nextBirthdayDate - todayDateTime
    

if __name__ == "__main__":    
    thisAge = age(date(1998, 9, 21))
    My_next_birthday = my_next_birthday(datetime(1998, 4, 13, 5, 20, 30))
    print("You are {} years old".format(thisAge))
    print("My next birthday will be in {}".format(My_next_birthday))