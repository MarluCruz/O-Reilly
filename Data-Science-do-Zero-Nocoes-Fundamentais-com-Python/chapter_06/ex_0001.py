def compare (x, y):
  if x > y:
    return 1
  if x == y:
    return 0
  if x < y:
    return -1
print("Digite um valor para x:")
x = float(input())
print("Digite um valor para y:")
y = float(input())
print(compare(x, y))