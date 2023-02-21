def is_sorted(t):
    thislist = []
    thislist = thislist + t
    thislist.sort()
    if t == thislist:
        return True
    else:
        return False

thislist = [100, 50, 65, 82, 23]
print(is_sorted(thislist))