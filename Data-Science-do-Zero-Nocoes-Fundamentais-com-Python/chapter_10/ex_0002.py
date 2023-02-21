y = [[1,2,3], [4,5,6], [7,8, 9]]
def nested_sum(t):
  y = 0
  for x in range(len(t)):
    y += sum(t[x])
  return y
  

print(nested_sum(y))