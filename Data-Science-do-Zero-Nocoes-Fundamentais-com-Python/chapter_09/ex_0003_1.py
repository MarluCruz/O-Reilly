def avoids(word, letter1, letter2, letter3, letter4, letter5):
    if letter1 in word:
        return False
    elif letter2 in word:
        return False
    elif letter3 in word:
        return False
    elif letter4 in word:
        return False
    elif letter5 in word:
        return False
    else:
        return True
def write_words(alphabet, i, j, x, k, y):
    count = 0
    for line in fin:
        word = line.strip()
        if avoids(word, alphabet[i], alphabet[j], alphabet[x], alphabet[k], alphabet[y]):
            count += 1
    return count
def more_words(alphabet):
    i = 0
    j = i + 1
    x = j + 1
    k = x + 1
    y = k + 1
    count = 0
    while i == 0:
        while j < x:
            while x < k:
                while k < y:
                    for y in range(y, len(alphabet)):
                        count = write_words(alphabet, i, j, x, k, y)
                        """
                        for line in fin:
                                word = line.strip()
                                if avoids(word, alphabet[i], alphabet[j], alphabet[x], alphabet[k], alphabet[y]):
                                    count += 1
                        """            
                        print('A combinação "{},{},{},{},{}" permitiu {} palavras'.format(alphabet[i], alphabet[j], alphabet[x], alphabet[k], alphabet[y], count))
                    k += 1
                x += 1
            j += 1
        


alphabet = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
fin = open('words.txt')
more_words(alphabet)
#for line in fin:
    #word = line.strip()