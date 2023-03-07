def sed(words, file1, file2, word = 'the' ):
    fp = open(file1, encoding='utf-8')
    modified = open('{}.txt'.format(file2), 'w', encoding='utf-8')
    for line in fp:
        modified.write(line.replace('the', words))

    
sed('Buzzlightyear', 'Dracula.txt', 'DraculaModified')