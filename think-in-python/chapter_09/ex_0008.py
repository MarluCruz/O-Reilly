import random
def is_palindrome(word):
    if (word == word[::-1]):
        return True
    else:
        return False

count = 0
x = 100000   
for x in range(100000, 999999):
    number = str(x)
    if is_palindrome(number):
        print(number)
        count += 1

print('Houve um total de {} números que satisfaziam essa condição'.format(count))
