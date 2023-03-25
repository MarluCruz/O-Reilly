segundos = (42 * 60) + 42
print('Tem ', segundos, ' segundos\n')
milhas = 10 * 1.6 
print('Tem ', milhas, ' milhas\n')
horas = (segundos / 60) / 60
velocidade_km = 10 / horas
passoMedio_segundo = milhas / segundos
passoMedio_minuto = milhas / (segundos/60)
passoMedio_hora = milhas / ((segundos/60) /60)
print("A velocidade em Km é ", velocidade_km)
print("A velocidade do passo médio por segundo é: ", passoMedio_segundo)
print("A velocidade do passo médio por minutos é: ", passoMedio_minuto)
print("A velocidade do passo médio por hora é: ", passoMedio_hora)