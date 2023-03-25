def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1   
    return d

def invert_dic(d):
    inverse = {}
    for key in d:
        inverse.setdefault(d[key], key)
    return inverse

dicti = histogram('banana')
print(dicti)
print(invert_dic(dicti))

