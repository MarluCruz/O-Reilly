from anagram_sets import all_anagrams, signature
import dbm
def store_anagrams(d):
    db = dbm.open('captions', 'c')
    for i,j in d.items():
        db[str(i)] = str(j)

def read_anagrams(word):
    db = dbm.open('captions', 'r')
    key = signature(word)
    try:
        print(db[key])
    except:
        print("Something is wrong")

#def read_anagrams():
if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    #store_anagrams(anagram_map)
    read_anagrams('stop')