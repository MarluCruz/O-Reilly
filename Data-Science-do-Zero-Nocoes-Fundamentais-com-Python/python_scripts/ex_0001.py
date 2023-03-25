#Criando um dicionário para contar as palavra de um documento
with open('documents/text_0001.txt', 'r') as document:
    word_counts = {}
    for word in document:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
print(word_counts.values())
print (word)