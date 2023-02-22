def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

count = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word, 'acefhlo'):
        print(word)
        count += 1
print('Houve um total de {} palavras'.format(count))