def any_lowercase1(s):
    for c in s: # Inicia um círculo de repetição que passará por cada caracter de s
        if c.islower():# Uma condicional que é ativada na presença de uma letra minúscula
            return True# Achando uma letra minúscula retornamos True
        else:# Um 'senão' para a condicional anterior e onde está o erro da função
            return False #Caso a letra minúscula não se encontre na primeria posição da string o resultado sempre será False.
        
def any_lowercase2(s):
    for c in s:# Inicia um círculo de repetição que passará por cada caracter de s
        if 'c'.islower():# Uma condicional que é ativada caso a letra 'c' seja minúscula. O erro aqui ocorre porque ao colocar o c entre apóstrofos nós mudamos o tipo dele para string. Portanto não estamos mais avaliando os caracteres de s, mas a string 'c'.
            return 'True'# Aqui temos o nome True entre apóstrofos o que incide em outro erro pois deixamos de passar um valor booleano para passar uma string. Podendo afetar operações lógicas vindouras. 
        else:# Um 'senão' para a condicional anterior
            return 'False'# Aqui temos o nome False entre apóstrofos o que incide em outro erro pois deixamos de passar um valor booleano para passar uma string. Podendo afetar operações lógicas vindouras. 
        
def any_lowercase3(s):
    for c in s:#Inicia um círculo de repetição que passará por cada caracter de s
        flag = c.islower() #A variável flag recebe o resultado de c.islower()
    return flag#Retorna flag e o problema. Como o círculo reliza continuas atribuições a flag o valor True só irá ser retornado caso a última letra seja minúscula.
def any_lowercase4(s):
    flag = False #Atribui o valor de False para a variável flag
    for c in s:#Inicia um círculo de repetição que passará por cada caracter de s
        flag = flag or c.islower() #Atribuímos a operação lógica de  or onde Flag é atribuída a ela mesma ou o operador lógico o método c.islower(). Caso em algum momento o valor seja True ele será passado.
    return flag # Por fim retornamos flag. Este método é correto!
def any_lowercase5(s):
    for c in s:#Inicia um círculo de repetição que passará por cada caracter de s
        if not c.islower():#A condiciona é ativada com uma negação de c.islower(), ou seja quando c.islower() for False.
            return False#Retorna False, como é necessário apenas uma negação de c.islower para ativar esta condicional, qualquer palavra que contenha pelo menos uma letra maiúscula incidi em um erro.
    return True

print(any_lowercase5('mamaco'))