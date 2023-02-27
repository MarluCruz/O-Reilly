def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

def is_there_rotate_pair(t, n):
  for x in range(len(t)):
    rotated = rotate_word(t[x], n)
    if rotated in t:
      print ('{} | {}'.format(t[x], rotated))

thislist2 = ['army', 'marine', 'space', 'emperor', 'god', 'army', 'cheer', 'melon', 'sleep', 'jolly', 'cubed', 'bunny']
is_there_rotate_pair(thislist2, -10)