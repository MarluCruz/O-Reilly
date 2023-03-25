from ex_0001 import Time, print_time
def verification(time):
    word = str(time)
    list_number= list(word)
    number = (int(list_number[-2])*10) + int((list_number[-1]))
    return number
def verification2(time):
    if time < 10:
        return time
    else:
        return verification(time)


def increment(time, seconds):
    if ((seconds / 60)%60) == 0: # Teremos alteração apenas nas horas
        time.hour += (seconds / 60)/60
        return
    elif time.second + seconds >= 3600:
        validation = verification(time.second + seconds) #Teremos alterações na horas minutos e segundos
        if validation != time.second:
            if validation >= 60:
                time.second = validation - 60
                time.minute += ((seconds - time.second) / 60) +1
                if time.minute >= 60:
                    time.hour += int(time.minute / 60)
                    time.minute = int(((time.minute / 60) - int(time.minute / 60)) * 60)
            if validation < 60:
                time.second = validation
                time.minute += ((seconds - time.second) / 60)
                if time.minute >= 60:
                    time.hour += int(time.minute / 60)
                    time.minute = int(((time.minute / 60) - int(time.minute / 60)) * 60) +1
            return
    elif(((seconds / 60)/60) == float) and  ((time.second + seconds) >= 3600):
    #elif (((((((time.second +seconds) / 60) / 60) - int(((time.second+seconds) / 60) / 60))*60)*60) >= 60) and  time.second >= 3600:
        #Termos alteração nas horas e minutos
        time.second += seconds
        time.minute += int((time.second / 60))
        if time.minute >= 60:
            time.hour += int(time.minute / 60)
            time.minute = int(((time.minute / 60) - int(time.minute / 60)) * 60)
            time.second = time.second - seconds
            return
    elif time.second + seconds >= 60:
        validation = verification(time.second + seconds) #Teremos alterações nos minutos e segundos
        if validation != time.second:
            if validation >= 60:
                time.second = validation - 60
                time.minute += ((seconds - time.second) / 60) +1
                if time.minute >= 60:
                    time.hour += int(time.minute / 60)
                    time.minute = int(((time.minute / 60) - int(time.minute / 60)) * 60)
            if validation < 60:
                time.second = validation
                time.minute += ((seconds - time.second) / 60)
                if time.minute >= 60:
                    time.hour += int(time.minute / 60)
                    time.minute = int(((time.minute / 60) - int(time.minute / 60)) * 60)
        time.minute += int(((time.second + seconds) / 60))
        time.second += int((seconds/60) - int((seconds/60))*60)
        if time.minute >= 60:
            time.hour += time.minute / 60
            time.minute = int((time.minute % 60) *60)

if __name__ == "__main__":
    time = Time()
    time.hour = 21
    time.minute = 37
    time.second = 46
    increment(time, 3660)
    print_time(time)
    #Isso é uma vergonha NUNCA MAIS TENTE REINVENTAR A RODA