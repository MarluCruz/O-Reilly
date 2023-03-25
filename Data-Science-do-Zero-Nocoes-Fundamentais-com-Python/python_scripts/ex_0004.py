#Defaultdict para contar as palavras de um dicionário
with open('documents/text_0001.txt', 'r') as document:
    from collections import defaultdict
    word_counts = defaultdict(int)
    for word in document:
        word_counts[word] += 1
print(word_counts.values())
