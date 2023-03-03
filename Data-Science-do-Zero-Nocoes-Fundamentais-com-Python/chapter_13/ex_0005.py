import random
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1   
    return d

def sum_all(numbers):
    soma = 0
    for x in range(len(numbers)):
        soma += numbers[x]
    return soma

def choose_from_hist(d):
    thisdict =dict()
    total = sum_all(list(d.values()))
    key = random.choice(list(d.keys()))
    thisdict[key] = '{}/{}'.format(d.get(key), total)
    return thisdict
    

listLetter = histogram('bananal')
d = choose_from_hist(listLetter)
print(d.items())


