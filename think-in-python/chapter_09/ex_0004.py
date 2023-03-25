def uses_only(word, letter1, letter2, letter3, letter4, letter5, letter6, letter7):
    for letter in word:
        if (letter != letter1) and (letter != letter2) and (letter != letter3) and (letter != letter4) and (letter != letter5) and (letter != letter6) and (letter != letter7):
            return False
    return True

count = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word, 'a', 'c', 'e', 'f', 'h', 'l', 'o'):
        print(word)
        count += 1
print('Houve um total de {} palavras'.format(count))