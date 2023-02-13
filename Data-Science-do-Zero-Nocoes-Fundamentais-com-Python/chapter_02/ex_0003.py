def conversor(segundos):
  Segundos = 0
  minutos = 0
  horas = 0
  for i in range(segundos):
    Segundos += 1
    if Segundos == 60:
      minutos += 1
      Segundos = 0
    elif minutos == 60:
      horas += 1
      minutos = 0
  print("Ele chegou as", horas, "horas", minutos, "minutos", Segundos, "segundos para o café da manhã")
    


Passo_1 = ((8 * 60) + 15) * 2
print(Passo_1)
Passo_2 = ((7  * 60)+ 12) * 3
print(Passo_2)
Tempo_em_segundos = (Passo_1 + Passo_2 + (52 * 60) + ((6*60)*60))
Tempo_em_segundos_2 = ((Passo_1* 2) + (Passo_2 * 2) + (52 * 60) + ((6*60)*60))
print(Tempo_em_segundos)
conversor(Tempo_em_segundos)
conversor(Tempo_em_segundos_2)