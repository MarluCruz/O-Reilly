def use_all(word, required):
    return all(False for letter in  required if letter not in  word)

def use_all2(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

if __name__ == '__main__':
    count = 0
    fin = open('words.txt')
    list1 = []
    list2 = []
    for line in fin:
        word = line.strip()
        if use_all(word, 'dog'):
            list1.append(word)
            count += 1
        if use_all2(word, 'dog'):
            list2.append(word)

            #count += 1
    #print('Houve um total de {} palavras'.format(count))
    print(list1 == list2)