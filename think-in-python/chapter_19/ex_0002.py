def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def avoids2(word, forbidden):
    return (forbidden - word) >= (forbidden)



if __name__ == '__main__':
    list1 = []
    listt2 = []
    count = 0
    fin = open('words.txt')
    print('Digite a primeira letra:')
    forbidden = str(input())
    print('Digite a segunda letra:')
    forbidden = forbidden + str(input())
    print('Digite a terceira letra:')
    forbidden = forbidden + str(input())
    print('Digite a Quarta letra:')
    forbidden = forbidden + str(input())
    print('Digite a Quinta letra:')
    forbidden = forbidden + str(input())
    for line in fin:
        word = line.strip()
        if avoids(set(word), set(forbidden)):
            list1.append(word)

        if avoids(set(word), set(forbidden)):
            listt2.append(word)
    #print('Houve um total de {} palavras'.format(count))
    print(list1 == listt2)