def three_pair(word):
    if len(word) <= 1:
        return True
    if word[0:1] == word[1:2]:
        return three_pair(word[2:])
    else:
        return False

count = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if (len(word) >= 6) and (three_pair(word[0:6])):
        print(word)
        count += 1
print('Houve um total de {} palavras em ordem alfabética'.format(count))