def do_twice(function, argument):
  function(argument)
  function(argument)

def print_spam(argument):
  print(argument)

def do_four(function, argument):
  do_twice(function, argument)
  do_twice(function, argument)

do_four(print_spam, 'spam')