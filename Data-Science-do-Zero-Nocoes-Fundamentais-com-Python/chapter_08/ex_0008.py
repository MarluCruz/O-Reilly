def rotate_str(word, n):
    alphabet_M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_m = 'abcdefghijklmnopqrstuvwxyz'
    j = -1
    k = -1
    word1 = ''
    for y in range(len(word) - 1):
        for x in range(len(alphabet_M) - 1):
            k += 1
            if word[y:y+1] == alphabet_M[k:k + 1]:
                for i in range(n):
                    j += 1
                    if j > 26:
                        j = 0
                    if i == (n - 1):
                        word1 = word1 + alphabet_M[j:j+1]
                        k = 0
            if word[y:y+1] == alphabet_m[k:k + 1]:
                for i in range(n):
                    j += 1
                    if j >= 26:
                        j = 0
                    if i == (n - 1):
                        word1 = word1 + alphabet_m[j:j+1]
                    k = 0
            break
    return word1

print(rotate_str('ab', 1))