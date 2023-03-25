import string
def find(word,):
    index = 0
    while index < len(word):
        if word[index] in string.punctuation:
            return word[:index]
        index = index + 1
    return -1

def make_line_list(lines = list()): #another way to break the alias
    d = open('Diggy_Diggy_Hole.txt')
    for word in d:
        lines.append(word.lower())
    return lines

d = """61 | ['which']
51 | ['now,']
47 | ['upon']
42 | ['some']
41 | ['towards']
40 | ['red', 'going']
37 | ['shall']
36 | ['it,', 'none']
34 | ['taking', 'helsing', 'up,']
32 | ['able', 'and,']
31 | ['do', 'put', 'it;']
30 | ['whose', 'sleep,']
29 | ['myself', 'not,', 'so,']
28 | ['find']
27 | ['chapter', 'that', 'lest', 'is,']
26 | ['out', 'raised', 'out,', 'electronic']
25 | ["seward's", 'back,']
24 | ['seems']
23 | ['the', 'till', 'say', 'cut', 'grim', 'rushed']
22 | ['he', 'window', 'other,', 'nearly', 'between', 'turning', 'during', 'showed', 'leave', 'see,', 'time.']"""

c = """61 | ['which']
51 | ['now,']
47 | ['upon']
42 | ['some']
41 | ['towards']
40 | ['red', 'going']
37 | ['shall']
36 | ['it,', 'none']
34 | ['taking', 'helsing', 'up,']
32 | ['able', 'and,']
31 | ['do', 'put', 'it;']
30 | ['whose', 'sleep,']
29 | ['myself', 'not,', 'so,']
28 | ['find']
27 | ['chapter', 'that', 'lest', 'is,']
26 | ['out', 'raised', 'out,', 'electronic']
25 | ["seward's", 'back,']
24 | ['seems']
23 | ['the', 'till', 'say', 'cut', 'grim', 'rushed']
22 | ['he', 'window', 'other,', 'nearly', 'between', 'turning', 'during', 'showed', 'leave', 'see,', 'time.']"""

print(c == d)
