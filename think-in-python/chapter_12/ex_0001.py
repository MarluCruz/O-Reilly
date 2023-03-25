def sumall(*numbers):
    #soma = 0
    #if (len(numbers)%2)  == 0:
        #for x in range((len(numbers))/2):
            #soma += sum(numbers[x], numbers[x + 1])
    
    return sum(*numbers)

a = (1, 2, 3, 4, 5)
print (sumall(a))