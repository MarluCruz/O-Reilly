from ex_0007 import Poligons, poligons, date_to_days, days_to_date, age_2
from datetime import timedelta, date

def nday(birthday1, birthday2, n):
    birthday1_to_days = date_to_days(birthday1)
    birthday2_to_days = date_to_days(birthday2)

    if birthday1_to_days > birthday2_to_days:
        diference = birthday1_to_days - birthday2_to_days
        x = 1
        y = diference.days
        razao = y/x
        while razao > n:
            x += 1
            y += 1
            razao = y/x

        n_day = days_to_date(timedelta(birthday1_to_days.days+x))
        olderAGe = age_2(birthday2, n_day )
        youngerAge = age_2(birthday1, n_day)
        
        print('O dia duplo será {}'.format(n_day))
        print('A idade do mais velho tera {} anos de idade'.format(olderAGe))
        print('A idade do mais novo será {} anos de idade'.format(youngerAge))
        return True
    
    elif birthday1_to_days < birthday2_to_days:
        diference = birthday2_to_days - birthday1_to_days
        double_day = days_to_date(birthday2_to_days+diference)
        olderAGe = age_2(birthday1, double_day )
        youngerAge = age_2(birthday2, double_day)
        print('O dia duplo será {}'.format(double_day))
        print('A idade do mais velho terá {} anos de idade'.format(olderAGe))
        print('A idade do mais novo será {} anos de idade'.format(youngerAge))
        return True
    
    elif birthday1_to_days == birthday2_to_days:
        print('Ambos nasceram no mesmo dia não haverá dia duplo')
        return False


nday(date(2010, 6, 11), date(1998,9,21), 2)