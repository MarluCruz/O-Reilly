def gcd(a, b):
  if (a > b):
    r = a % b
    if r != 0:
      return gcd(b, r)
    else:
      return b
  elif (b > a):
    r = b % a
    if r != 0:
     return  gcd(a, r)
    else:
      return a

print(gcd(72, 48))