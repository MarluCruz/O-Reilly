import string

lines = list()
d = open('89.txt', encoding='utf8')
for word in d:
    if word[0] == ' ': continue
    lines.append(word.lower())

for x in range(len(lines)):
        linha = lines[x]
        for letter in linha:
            if (letter in string.punctuation and letter != "'"): continue
            if (letter in string.whitespace): 
                print('\n')
            else:
                print(letter, end="")