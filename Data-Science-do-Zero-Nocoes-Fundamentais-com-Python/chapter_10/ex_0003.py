def cumsum(t):
  y = []
  soma = 0
  for x in range(len(t)):
    soma += t[x]
    y.append(soma)
  return y

t = [3, 2 , 1]
print(cumsum(t))