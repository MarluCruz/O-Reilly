#EXpressões geradoras são semelhantes às anbrangências de listas, mas com parênteses em vez de colchetes

g = (x**2 for x in range(5))
print(g)

"""O resultado é um objeto gerador que sabe como fazer interações por uma sequência de valores. No entanto, ao contrário de uma abrangência de listas, ele não calcula todos os valores de uma vez; espera pelo pedido. A função integrada next recebe o próximo valor do gerador:"""

print(next(g))
print(next(g))
for val in g:
    print(val)

#Expressões geradoras muitas vezes são usadas com funções como sum, max e min:
print(sum(x**2 for x in range(5)))