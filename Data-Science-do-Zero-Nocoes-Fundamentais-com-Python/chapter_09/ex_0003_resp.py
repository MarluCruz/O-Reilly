def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
       

count = 0
fin = open('words.txt')
print('Digite a primeira letra:')
forbidden = str(input())
print('Digite a segunda letra:')
forbidden = forbidden + str(input())
print('Digite a terceira letra:')
forbidden = forbidden + str(input())
print('Digite a Quarta letra:')
forbidden = forbidden + str(input())
print('Digite a Quinta letra:')
forbidden = forbidden + str(input())
for line in fin:
    word = line.strip()
    if avoids(word, forbidden):
        print(word)
        count += 1
print('Houve um total de {} palavras'.format(count))