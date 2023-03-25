from collections import Counter
with open('documents/text_0001.txt', 'r') as document:
    word_count = Counter(document)
    print(word_count)
    for word, count in word_count.most_common(10):
        print(word, count)
   