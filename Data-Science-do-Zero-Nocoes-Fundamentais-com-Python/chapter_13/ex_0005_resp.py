import string
def process_file(filename):
    hist = dict()
    fp = open(filename, encoding = 'Utf-8')
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_commom(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse = True)
    return t
def subtract(d1, d2):
 return set(d1) - set(d2)

def subtract_set(d1, d2):
    res = dict()
    d1Keys = set(d1.keys())
    d2Keys = set(d2.keys())
    resp = d1Keys.difference(d2Keys)
    return resp

hist = process_file('Dracula.txt')
listWord = process_file('words.txt')
t = most_commom(hist)
resp = subtract_set(hist, listWord)
resp_2 = subtract(hist, listWord)
print(resp == resp_2)

#print('Total number of words:', total_words(hist))
#print('Number of different words:', different_words(hist))
#print('The msot common wors are:')
#for freq, word in t[:10]:
    #print(word, freq, sep='\t')
#for x in resp:
    #print(x)