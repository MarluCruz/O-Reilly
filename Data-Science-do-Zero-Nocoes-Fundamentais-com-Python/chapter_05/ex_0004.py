def recurse(n, s): #In this line we made the function recurse, recurse has two parameters n and s.
  if n == 0: #In this line there is a conditional with only one condition, the condition say that if n is equal 0 do it.
    print(s) #In this line the function print receives the variable s and print it on the screen.
  else: #If the condition isn't true do it.
    recurse(n-1, n+s) #The function is called recursively, and receives n-1, and n+s as argument

recurse(3, 0) #The function recurse is called recursively in the __int__ main and receives 3 and 0 as argument