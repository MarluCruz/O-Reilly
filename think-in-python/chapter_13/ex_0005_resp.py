import string
import random
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

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    hist: map from word to frequency
    """
    # TODO: This could be made faster by computing the cumulative
    # frequencies once and reusing them.

    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = in_bisect(freqs, x)
    return words[index]

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
    

#hist = process_file('Dracula.txt')

#print("\n\nHere are some random words from the book")
#for i in range(100):
    #print(random_word(hist), end=' ')


hist = process_file('DraculaModified.txt')
#listWord = process_file('words.txt')
t = most_commom(hist)
#resp = subtract_set(hist, listWord)
#resp_2 = subtract(hist, listWord)
#print(resp == resp_2)

print('Total number of words:', total_words(hist))
print('Number of different words:', different_words(hist))
print('The msot common words are:')
for freq, word in t[:10]:
    print(word, freq, sep='\t')
#for x in resp:
    #print(x)