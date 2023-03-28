def capitalize_all(t):
    return[s.capitalize() for s in t]# ESte é um caso de mapeamento
""" Os operadores do colchete indicam que estamos construindo uma nova lista. A expressão dentro dos colchetes especifica os elementos da lista, e a clásula for indica qual sequência estamos atravessando"""

def only_upper(t):
    return [s for s in t if s.isupper()]
# Abrangência de Listas também podem ser usadas para filtragem.

if __name__ == '__main__':
    print(only_upper('Paçoca'))