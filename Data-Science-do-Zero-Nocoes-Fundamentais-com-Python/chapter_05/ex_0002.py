def A():
  print("Digite um número inteiro para a:")
  a = int(input())
  if a <= 0:
    print("Números negativos e 0 são inválidos. Por favor digite um número inteiro e positivo:")
    A()
  return a

def B():
  print("Digite um número inteiro para b:")
  b= int(input())
  if b <= 0:
    print("Números negativos e 0 são inválidos. Por favor digite um número inteiro e positivo:")
    B()
  return b

def C():
  print("Digite um número inteiro para c:")
  c= int(input())
  if c <= 0:
    print("Números negativos e 0 são inválidos. Por favor digite um número inteiro e positivo:")
    C()
  return c

def N():
  print("Digite um número inteiro para n que seja maior que 2:")
  n= int(input())
  if n < 2:
    print("Números negativos e 0 são inválidos. Por favor digite um número inteiro e positivo:")
    N()
  return n
  
def ABCN ():
  a = A()
  b = B()
  c = C()
  n = N()
  check_fermat(a, b, c, n)

def check_fermat(a, b, c, n):
  if ((a**n) + (b**n)) == (c**n):
    print("Holy smokes, Fermat was wrong!")
  else:
    print("No, that doesn't work!")

ABCN()