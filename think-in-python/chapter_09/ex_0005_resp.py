def use_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

count = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if use_all(word, 'ebook'):
        print(word)
        count += 1
print('Houve um total de {} palavras'.format(count))