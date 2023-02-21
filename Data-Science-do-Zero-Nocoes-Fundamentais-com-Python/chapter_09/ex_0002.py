fin = open('words.txt')
def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

count1 = 0
count2 = 0
for line in fin:
    word = line.strip()
    count1 += 1
    if has_no_e(word):
        #print(word)
        count2 += 1

percentual = 100 - ((count2 * 100) / count1)

print("O percentual de palavras que não tem 'e' são {}".format(round(percentual, 2)))
