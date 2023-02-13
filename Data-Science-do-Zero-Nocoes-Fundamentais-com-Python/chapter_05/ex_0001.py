import time
from datetime import datetime
epoca = time.time()
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
horas = (((epoca) //60) // 60)
minutos = (epoca - (horas *60) *60) // 60
segundos = (epoca - ((horas*60) + minutos)*60) // 1
horario = "Estamos Há {} horas {} minutos {} segundos de 1° de Janeiro de 1970"
print(horario.format(horas, minutos, segundos))