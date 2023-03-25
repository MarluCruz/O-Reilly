def linecount(filename):
    count = 0
    for line in open(filename, encoding= 'utf-8'):
        count += 1
    return count

if __name__ == '__main__':
    print(linecount('wc.py'))