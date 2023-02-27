def histogram(s):
    d = dict()
    for c in s:
        if c == ' ' : continue
        if c ==',': continue
        d[c] = d.get(c, 0) + 1   
    return invert_dic(d)

def invert_dic(d):
    inverse = {}
    for key in d:
        inverse.setdefault(d[key], key)
    return inverse

def use_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def make_word_list():
    """Read. the words in words.txt and return a dictionary
    that contains the words as keys."""
    l = list()
    fin = open('words.txt')
    x = 0
    for line in fin:
        word = line.strip().lower()
        l.append(word)
        x += 1
    return l
def raider_letter(word, words):
    for letter in words:
        if letter not in word:
            return False
    return True
def breaking_the_alias(t):
    c = t[-1]
    b = list()
    t.pop()
    b += t
    b.append(c)
    t.clear()
    return b
def anagram_lists(d, lisT):
    anagram_collection = lisT
    anagram_list = list()
    i = 0
    j = i + 1
    for i in range(len(d)):
        for j in range(j, len(d)):
            if (len(d[i]) == len(d[j])) and use_all(d[i], d[j]) and raider_letter(d[i], d[j]) and (histogram(d[i]) == histogram(d[j])):
                if d[i] not in anagram_list:
                    anagram_list.append(d[i])
                anagram_list.append(d[j])      
        if (len(anagram_list) != 0):
            for x in range(len(anagram_list)):
               d.remove(anagram_list[x]) 
            return d[i:], anagram_collection.append(breaking_the_alias(anagram_list))
    print()    
    return anagram_collection


anagram_collection = anagram_lists(make_word_list(), list())
print(len(anagram_collection))
for x in range(anagram_collection):
    print('{} : {}'.format(x+1, anagram_collection))

    