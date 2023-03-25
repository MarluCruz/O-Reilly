def middle(t):
  new = []
  new = new + t
  new.pop(0)
  new.pop(-1)
  return new

t = [1, 2, 3 , 4]
new = middle(t)
print(new)
print(t)
print(new is t)