def is_reverse(word1, word2):
    i = 0
    j = len(word2) -1
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def are_there_reverse(t):
    count = 0
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if len(t[i]) == len(t[j]):
                if is_reverse(t[i], t[j]):
                    count += 1
    return count


thislist = ['pay', 'brag', 'bat', 'tab', 'garb', 'part', 'yap', 'trap', 'pals', 'slap']

print(are_there_reverse(thislist))