#Utilizando get para contar as palavra em um documento
with open('documents/text_0001.txt', 'r') as document:
    word_counts = {}
    for word in document:
        previous_count = word_counts.get(word, 0)
        word_counts[word] = previous_count + 1
print(word_counts.values())
