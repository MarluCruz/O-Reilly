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
def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)

def sum_all(numbers):
    return sum(numbers)
def random_choice(d):
    listWord = list()
    numbers = sum_all(list(d.values()))
    for x, i in d.items():
        for _ in range(i):
            listWord.append(x)
    return listWord


hist = process_file('Dracula.txt')
random_choice(hist)