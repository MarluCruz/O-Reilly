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

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def frenquency_word(d):
    keys = list(d.keys())
    thisdict = dict()
    keys.sort()
    for x in range(20):
        thisdict[max(keys)] = d.get(max(keys))
        keys.pop()
    return thisdict

lineList = list()
lineList = make_line_list(lineList)
d = number_of_each_words(lineList)
total = total_number_of_words(list(d.values()))
invertido = invert_dict(d)
top20 = frenquency_word(invertido)
#print(d)
#print(invertido)
print('Essa é lista das 20 palavras mais frequentes:')
for x,i in top20.items():
    print("{} | {}".format(x,i))
print('O número toatal de palvras é {}'.format(total))

