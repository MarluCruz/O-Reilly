def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0:1] == word[1:2]:
        return is_abecedarian(word[1:])
    if word[0:1] < word[1:2]:
        return is_abecedarian(word[1:])
    else:
        return False

count = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
        count += 1
print('Houve um total de {} palavras em ordem alfabética'.format(count))