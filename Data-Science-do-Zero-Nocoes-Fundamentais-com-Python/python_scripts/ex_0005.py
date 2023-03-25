#Utiliza um contador para informar o número de palavras em um documento
from collections import Counter
with open('documents/text_0001.txt', 'r') as document:
    word_count = Counter(document)
    print(word_count)