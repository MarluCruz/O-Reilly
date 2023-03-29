""" O módulo collections também tem defaultdict, que se parece com um dicionário, exceto pelo fato    de  que se você acessar uma chave que não existe, um novo valor pode ser gerado automaticamente. 
    Quando você cria um defaultdict, fornece uma função usada para criar valores. Uma função usada para criar objetos às vezes é chamada de factory(fábrica). As funções integradas que criam listas, conjuntos e outros tipos podem ser usadas como fábricas:"""
from collections import defaultdict
from All_anagrams import signature, print_anagram_sets_in_order

#All anagrams pode ser simplificado usando setdefault

def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
    return d

if __name__ == "__main__":
    anagram_map = all_anagrams('words.txt')
    print_anagram_sets_in_order(anagram_map)
    d = defaultdict(list)
    t= d['new key']
    print(t)
    t.append('new value')
    print(d)
