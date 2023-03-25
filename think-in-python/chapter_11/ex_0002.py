def dict_search():
    fin = open('words.txt')
    dic = dict()
    x = 0
    for line in fin:
        word = line.strip()
        dic[word] = x
        x += 1
    return dic
    


dic = dict_search()
print()
%timeit print(dic.get('lion', 0))
print()