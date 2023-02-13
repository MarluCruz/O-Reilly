def right_justify(palavra):
  justificado = ' '
  for i in range(69 - len(palavra)):
    justificado = justificado + justificado
  print(justificado+palavra)

print("Digite uma palavra:\n")
palavra = str(input())
right_justify(palavra)