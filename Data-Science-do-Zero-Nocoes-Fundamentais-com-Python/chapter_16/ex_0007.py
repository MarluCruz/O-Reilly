from datetime import date, timedelta
from ex_0006 import age

class Poligons:
    """Cubo = (Year*4) +1 ; Year = (Month31*7) + (Month30*4) + Month28; Month31= 31*dias; Month30 = 30*dia; Month28 = 28*dia; dia = 1"""

def date_to_days(date):
    thisdict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    thisdict2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    poligon = poligons()
    newDate = date
    days = 0
    if (date.year/4) <= 1:
        days += (date.year - 1) * poligon.year
        if (date.year%4) == 0:
            for x in range(1, date.month):
                days += thisdict2.get(x, None)
        else:
            for x in range(1, date.month):
                days += thisdict.get(x, None)
        days += date.day
        newDate = timedelta(days)
        return newDate
    
    else:
        if (date.year % 4) == 0:
            days += ((date.year / 4)*poligon.cube) - (poligon.year + 1)
            for x in range(1, date.month):
                days += thisdict2.get(x, None)
            days += date.day
            newDate = timedelta(days)
            return newDate
        else: 
            days += ((int((date.year / 4))*poligon.cube) + ((date.year%4))*poligon.year) - poligon.year
            for x in range(1, date.month):
                days += thisdict.get(x, None)
            days += date.day
            newDate = timedelta(days)
            return newDate

def poligons():
    poligon = Poligons()
    poligon.day = 1
    poligon.month28 = 28*poligon.day
    poligon.month30 = 30*poligon.day
    poligon.month31 = 31*poligon.day
    poligon.year = (poligon.month31*7) + (poligon.month30*4) + (poligon.month28)
    poligon.cube = (poligon.year*4) + 1
    return poligon

def age_2(birthday1, birthday2):

    thisAge = birthday2.year - birthday1.year
    if (birthday2.month >= birthday1.month):
        if (birthday2.month == birthday1.month) and (birthday2.day < birthday1.day):
            return thisAge -1
        else:
            return thisAge
    else:
        return thisAge -1

def input_dates():
    
    monthDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    print("Digite o ano da data de nascimento:")
    year = int(input())
    if year <= 0:
            while year <= 0:
                print("Estamos usando o Calendário Gegoriano! Não existe ano menor que 1!")
                print("Por Favor! Digite um número maior que 0 para o ano do aniversário:")
                year = int(input())

    print("Digite o mês da data de nascimento:")
    month = int(input())
    if month <= 0 or month > 12:
        while month <= 0 or month > 12:
            print("Estamos usando o Calendário Gegoriano! Não existem meses menores que 0 ou maiorees 12!")
            print("Por Favor! Digite um número maior que 1 e menor que 12 para o mês do aniversário:")
            month = int(input())

    print("Digite o dia da data de nascimento:")
    day = int(input())
    if (month == 2 and ((year % 4) != 0) == 0) and  day == 29:
        return date(year, month, day)
    elif day > monthDays.get(month, 0) or day < 0:
        while day > monthDays.get(month, 0) or day < 0:
            print("Estamos usando o Calendário Gegoriano!\nPor favor! digite um numero menor que seja igual ou menor que {} para este mês e maior do que 0:".format(monthDays.get(month, 0)))
            day = int(input())
        return date(year, month, day)
    return date(year, month, day)

def doubleDay(birthday1, birthday2):
    
    age1 = age(birthday1)
    age2 = age(birthday2)

    diferenca = int()

    if age1 > age2:

        diferenca = age1 - age2

        if birthday1.month > birthday2.month:
            print("O dia duplo é {}/{}/{}!".format(birthday1.year + (diferenca*2), birthday1.month, birthday1.day ))
            print("O mais velho terá {}".format(age_2(birthday1, date(birthday1.year + (diferenca*2), birthday1.month, birthday1.day))))
            print("O mais novo terá {}".format(age_2(birthday2, date(birthday2.year + (diferenca), birthday2.month, birthday2.day))))

        if birthday1.month < birthday2.month:
            print("O dia duplo é {}/{}/{}!".format(birthday1.year + (diferenca*2), birthday2.month, birthday2.day))
            print("O mais velho terá {}".format(age_2(birthday1, date(birthday1.year + (diferenca*2), birthday1.month, birthday1.day))))
            print("O mais novo terá {}".format(age_2(birthday2, date( birthday2.year + (diferenca), birthday2.month, birthday2.day))))

    elif age1 < age2:

        diferenca = age2 - age1

        if birthday2.month > birthday1.month:
            print("O dia duplo é {}/{}/{}!".format((birthday2.year + (diferenca*2)), birthday2.month, birthday2.day))
            print("O mais velho terá {}".format(age_2(birthday2, date(birthday2.year + (diferenca*2), birthday2.month, birthday2.day))))
            print("O mais novo terá {}".format(age_2 (birthday1, date(birthday1.year + (diferenca), birthday1.month, birthday1.day))))
    
        if birthday2.month < birthday1.month:
            print("O dia duplo é {}/{}/{}!".format((birthday2.year + (diferenca*2)), birthday1.month, birthday1.day))
            print("O mais velho terá {}".format(age_2(birthday2, date(birthday2.year + (diferenca*2), birthday2.month, birthday2.day))))
            print("O mais novo terá {}".format(age_2(birthday1, date(birthday1.year + (diferenca), birthday1.month, birthday1.day))))
    
    elif age1 == age2:
        print("A diferença entre as idades é menor que 1.\n Portanto não existe dia duplo")
        return

def days_to_date(days):
 
    thisdict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    thisdict2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    poligon = poligons()

    cubes = int(days.days / poligon.cube)
    if cubes < 1:
        year = int((days.days - (days.days - int(days.days / poligon.year) * poligon.year))/poligon.year) +1
        daysOfMonths = (days.days - int(days.days / poligon.year) * poligon.year)
        count = 0
        month = 0

        if days.days > poligon.year*3:
            while (daysOfMonths > 0):
                count += 1
                daysOfMonths -= thisdict2.get(count, 0)
                month += 1
            day = daysOfMonths + thisdict2.get(count, 0)
            thisdate = date(year, month, day)
            return thisdate
        else:
            while (daysOfMonths > 0):
                count += 1
                daysOfMonths -= thisdict.get(count, 0)
                month += 1
            day = daysOfMonths + thisdict.get(count, 0)
            thisdate = date(year, month, day)
            return thisdate
        
    elif (days.days - ((cubes*poligon.cube) + poligon.year*3)) > 0:
        anoBisexto = int(((days.days - (days.days - (poligon.cube * cubes))) /poligon.cube) * 4)
        year = anoBisexto + int((days.days%poligon.cube) /poligon.year) + 1
        daysOfMonths = days.days - ((poligon.cube*cubes) + ((int((days.days%poligon.cube) / poligon.year))*poligon.year))
        count = 0
        month = 0
        while (daysOfMonths > 0):
            count += 1
            daysOfMonths -= thisdict2.get(count, 0)
            month += 1
        day = daysOfMonths + thisdict2.get(count, 0)
        thisdate = date(year, month, day)
        return thisdate
    else:
        anoBisexto = int(((days.days - (days.days - (poligon.cube * cubes))) /poligon.cube) * 4)
        year = anoBisexto + int((days.days%poligon.cube) /poligon.year) + 1
   
        daysOfMonths = days.days - ((poligon.cube*cubes) + (int((days.days%poligon.cube) /poligon.year)* poligon.year)) 
        count = 0
        month = 0
        while (daysOfMonths > 0):
            count += 1
            daysOfMonths -= thisdict.get(count, 0)
            month += 1
        day = daysOfMonths + thisdict.get(count, 0)
        thisdate = date(year, month, day)
        return thisdate
    
def doubleDay2(birthday1, birthday2):
    birthday1_to_days = date_to_days(birthday1)
    birthday2_to_days = date_to_days(birthday2)
    if birthday1_to_days > birthday2_to_days:
        diference = birthday1_to_days - birthday2_to_days

        print('O dia duplo será {}'.format(days_to_date(birthday1_to_days+diference)))


def main():
    print("Vamos escolher o ano da primeira data de nascimento:")
    birthday1 = input_dates()
    print("_____________________")
    print()
    print("Vamos escolher o ano da segunda data de nascimento:")
    birthday2 = input_dates()
    print("_____________________")
    print()
    doubleDay2(birthday1, birthday2)

if __name__ == "__main__":
    main()