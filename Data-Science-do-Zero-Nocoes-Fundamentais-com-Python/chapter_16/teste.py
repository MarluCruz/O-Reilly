from ex_0007 import Poligons, poligons, date_to_days, days_to_date
from datetime import timedelta, date



dateindays = date_to_days(date(2010,6,11))

daysindate = days_to_date(dateindays)
print(daysindate)