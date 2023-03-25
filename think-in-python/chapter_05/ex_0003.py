def askNumber():
  print("Digite um número inteiro para um dos lados do triângulo:")
  l1 = int(input())
  print("Digite outro número inteiro para um dos outros lados do triângulo:")
  l2 = int(input())
  print("Digite outro número inteiro para o último dos lados do triângulo:")
  l3 = int(input())
  is_triangle(l1,l2,l3)

def is_triangle(l1, l2, l3):
   if l1 > (l2 + l3):
     print("NO")
   elif l2 > (l1 + l3):
     print("NO")
   elif l3 > (l1 + l2):
     print("NO")
   else:
     print("Yes")

askNumber()