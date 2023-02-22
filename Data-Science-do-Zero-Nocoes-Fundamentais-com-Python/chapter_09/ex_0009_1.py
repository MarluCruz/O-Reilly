def is_reverse(age1, age2):
    return age1 == age2[::-1]

def is_reverse_count(i, j):
    count = 0
    son = []
    mom = []
    i = int(i)
    j = int(j)
    diferenca = j - i
    for i in range(i, 123):
        k = str(i)
        k = k.zfill(2)
        for j in range (diferenca + i, 124):
            x = str(j)
            x = x.zfill(2)
            if is_reverse(str(k), str(x)):
                if j - i == diferenca:
                    count += 1
                    son.append(k)
                    mom.append(x) 
    if count == 8:
        print()
        print('_______________________________________')
        for z in range(len(son)):
            print('{} {}'.format(son[z], mom[z]))
        print('_______________________________________')
        print()
        return True 
    else:
        return False 

def mommy_and_son():
    count = 0
    for i in range(1, 123):
        k = str(i)
        k = k.zfill(2)
        for j in range (i+1, 124):
            x = str(j)
            x = x.zfill(2)
            if is_reverse(k, x):
                if is_reverse_count(k, x):
                    count += 1
    print('Houve um total de {} combinações que satisfaziam essa condição'.format(count))

mommy_and_son()