def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

#letter = 'laio'
#print(letter[::-1])
print(is_palindrome('osso'))
print(is_palindrome('allna'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))