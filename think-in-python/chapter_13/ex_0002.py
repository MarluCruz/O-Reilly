import string
def make_line_list(lines = list()):
    d = open('Dracula.txt', encoding='utf8')
    for word in d:
        if word[0] == '#' or word[0] == ' ': continue
        lines.append(word.lower())
    return lines

def number_of_each_words(lines):
    word_list = list()
    d = dict()
    for x in range(len(lines)):
        if lines[x] != '\n':
            word_list = lines[x].rsplit(' ')
            for i in range(len(word_list)):
                if word_list[i] not in d:
                    word = word_list[i]
                    d[word.strip(string.punctuation).strip(string.whitespace)] = 1
                elif word_list[i] in d:
                    word = word_list[i]
                    d[word] += 1
        word_list.clear()
    return d

def total_number_of_words(lisT):
    soma = 0
    for x in range(len(lisT)):
        soma += lisT[x]
    
    return soma




lineList = list()
lineList = make_line_list(lineList)
d = number_of_each_words(lineList)
total = total_number_of_words(list(d.values()))
print(d)
print('O número toatal de palvras é {}'.format(total))

            
        
"""
linha = lines[x]
for letter in linha:
            if (letter in string.punctuation and letter != "'"): continue
            if (letter in string.whitespace): 
                print('\n')
            else:
                print(letter, end="")"""