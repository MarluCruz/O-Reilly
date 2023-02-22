def use_all(word, letter1, letter2, letter3, letter4, letter5):
    if (letter1 in word) and (letter2 in word) and (letter3 in word) and (letter4 in word) and (letter5 in word):
        return True
    else:
        return False
def use_all_plus(word, letter1, letter2, letter3, letter4, letter5, letter6):
    if (letter1 in word) and (letter2 in word) and (letter3 in word) and (letter4 in word) and (letter5 in word) and (letter6 in word):
        return True
    else:
        return False

count = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if use_all_plus(word, 'a', 'e', 'i', 'o', 'u', 'y'):
        print(word)
        count += 1
print('Houve um total de {} palavras'.format(count))