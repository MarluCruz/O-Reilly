def breaking_the_alias(t):
    c = t[-1]
    b = list()
    t.pop()
    b += t
    b.append(c)
    return b
a = ['banana', 'orange', 'pear', 'apple']
b = ['cyclin', 'soccer', 'football', 'basket']
c = breaking_the_alias(a)
print(c)
print(a)