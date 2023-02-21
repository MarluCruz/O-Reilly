def avoids(word, letter1, letter2, letter3, letter4, letter5):
    if letter1 in word:
        return False
    elif letter2 in word:
        return False
    elif letter3 in word:
        return False
    elif letter4 in word:
        return False
    elif letter5 in word:
        return False
    else:
        return True

fin = open('words.txt')
print('Digite a primeira letra:')
letter1 = str(input())
print('Digite a segunda letra:')
letter2 = str(input())
print('Digite a terceira letra:')
letter3 = str(input())
print('Digite a Quarta letra:')
letter4 = str(input())
print('Digite a Quinta letra:')
letter5 = str(input())
for line in fin:
    word = line.strip()
    if avoids(word, letter1, letter2, letter3, letter4, letter5):
        print(word)
