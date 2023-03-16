from datetime import date
from ex_0006 import age 

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
            print("O mais velho terá {}".format(age(date(birthday1.year + (diferenca*2), birthday1.month, birthday1.day))))
            print("O mais novo terá {}".format(age(date(birthday2.year + (diferenca), birthday2.month, birthday2.day))))

        if birthday1.month < birthday2.month:
            print("O dia duplo é {}/{}/{}!".format(birthday1.year + (diferenca*2), birthday2.month, birthday2.day))
            print("O mais velho terá {}".format(age(date(birthday1.year + (diferenca*2), birthday1.month, birthday1.day))))
            print("O mais novo terá {}".format(age(date(birthday1.year + (diferenca), birthday1.month, birthday1.day))))

    elif age1 < age2:

        diferenca = age2 - age1

        if birthday2.month > birthday1.month:
            print("O dia duplo é {}/{}/{}!".format(birthday2.year + (diferenca*2)), birthday2.month, birthday2.day)
            print("O mais velho terá {}".format(age(date(birthday2.year + (diferenca*2), birthday2.month, birthday2.day))))
            print("O mais novo terá {}".format(age(date(birthday1.year + (diferenca), birthday1.month, birthday1.day))))
    
        if birthday2.month < birthday1.month:
            print("O dia duplo é {}/{}/{}!".format(birthday2.year + (diferenca*2)), birthday1.month, birthday1.day)
            print("O mais velho terá {}".format(age(date(birthday2.year + (diferenca*2), birthday2.month, birthday2.day))))
            print("O mais novo terá {}".format(age(date(birthday1.year + (diferenca), birthday1.month, birthday1.day))))
    
    elif age1 == age2:
        print("A diferença entre as idades é menor que 1.\n Portanto não existe dia duplo")
        return

def main():
    print("Vamos escolher o ano da primeira data de nascimento:")
    birthday1 = input_dates()
    print("_____________________")
    print()
    print("Vamos escolher o ano da segunda data de nascimento:")
    birthday2 = input_dates()
    print("_____________________")
    print()
    doubleDay(birthday1, birthday2)

if __name__ == "__main__":
    main()