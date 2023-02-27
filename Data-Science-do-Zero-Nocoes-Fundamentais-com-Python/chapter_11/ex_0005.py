def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.
    Faster version using a set.
    t: sequence
    """
    return len(set(t)) < len(t)

#t = [1, 2, 3]
#print(has_duplicates(t))
#t.append(1)
#print(has_duplicates(t))

t = [1, 2, 3]
print(has_duplicates2(t))
t.append(1)
print(has_duplicates2(t))