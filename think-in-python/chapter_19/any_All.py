#Python tem uma função integrada, any, que recebe uma sequência de valores booleanos e retorna True se algum dos valores for True. Ela funciona em listas:

print(any([False, False, True]))
#Entetanto, muitas vezes é usada com expressões geradoras:
print(any(letter == 't' for letter in 'monty'))