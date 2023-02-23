import random
import time
def in_bisect(t, valor):
    limite_inferior = 0
    limite_superior = len(t) -1

    while True:
        posicao_atual = int((limite_inferior + limite_superior) / 2)
        if t[posicao_atual] == valor:
            return posicao_atual
        elif limite_inferior > limite_superior:
            return None
        else:
            if t[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
            else:
                limite_superior = posicao_atual -1


thislist = []
for x in range(100):
    thislist.append(random.randint(0, 1000))

thislist.sort()

%timeit print(in_bisect(thislist, thislist[random.randint(0, 99)]))
