def retorne(word):
    if word == '':
        return
    word_reduction.append(word)
    return retorne(word[1:])

word_reduction = []
retorne('banana')
print(word_reduction)
