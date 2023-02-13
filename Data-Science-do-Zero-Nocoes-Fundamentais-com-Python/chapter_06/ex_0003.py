def is_between(x, y, z):
  return x <= y <= z

print("Digite um valor para x:")
x = float(input())
print("Digite um valor para y:")
y = float(input())
print("Digite um valor para z:")
z = float(input())
if is_between(x, y, z):
  print("O valor de y está entre x e z.")
else:
  print("O valor de y não está entre x e z.")