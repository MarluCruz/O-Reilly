from datetime import timedelta, datetime, date
from ex_0006 import date_to_days

today = datetime.today()
dateinDays = date_to_days(today)
print(dateinDays.days)