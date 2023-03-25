# Utilizando try and except para contar as palavra em um documento
with open('documents/text_0001.txt', 'r') as document:
    word_counts = {}
    for word in document:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1
print(word_counts.values())