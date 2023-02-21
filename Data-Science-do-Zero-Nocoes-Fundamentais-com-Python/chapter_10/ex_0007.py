def has_duplicates(t):
    """Returns True if any element appears more than once in a sequence.
    t: list
    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

thislist = ['army', 'marine', 'space', 'emperor', 'god', 'army']
print(has_duplicates(thislist))