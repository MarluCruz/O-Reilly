def do_twice(function, argument):
  function(argument)
  function(argument)
def print_spam(argument):
  print(argument)
do_twice(print_spam, 'spam')