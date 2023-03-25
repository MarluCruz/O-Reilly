def chop (t):
    t.pop(0)
    t.pop(-1)
    return None

t = [1, 2, 3 , 4]
chop(t)
print(t)