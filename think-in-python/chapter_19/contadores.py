"""Um contador é com um conjunto, exceto que se um elemento aparecer mais de uma vez o contador acompanha quantas vezes ele aparece. Se tiver familiaridade com a idade matemática de multiconjunto, um contador é uma forma natural de representar um multiconjunto."""
from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)
    # Se duas palavras forem anagramas, elas contêm as mesmas letras com as mesmas contagens, então seus contadores são equivalentes.


count = Counter('parrot')
print(count)
# Ao contrário de dicionários, os contadores não causam uma exceção se você um elemento que não aparece. Em vez disso retornam 0 :
print(count['d'])
for val, freq in count.most_common(3):
    print(val, freq)