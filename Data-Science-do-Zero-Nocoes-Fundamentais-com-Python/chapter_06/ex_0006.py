def is_power(a, b):
  if a % b == 0 and (a/b == b**1):
    return True
  else:
    return False

print(is_power(100,10))