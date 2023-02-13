def plusAndminus_01():
  print("+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+")
def plusAndminus_02():
  print("+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+")
def bar_01():
  print("|", " ",  " ",  " ",  " ","|", " ", " ", " ", " ", "|")
def bar_02():
  print("|", " ",  " ",  " ",  " ","|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|",  " ", " ", " ", " ", "|")
def do_bar_four(f):
  do_bar_twice(f)
  do_bar_twice(f)
def do_bar_twice(f):
  f()
  f()
def drawPicture_01():
  plusAndminus_01()
  do_bar_four(bar_01)
  plusAndminus_01()
  do_bar_four(bar_01)
  plusAndminus_01()

def drawPicture_02():
  plusAndminus_02()
  bar_02()
  bar_02()
  bar_02()
  bar_02()
  plusAndminus_02()
  bar_02()
  bar_02()
  bar_02()
  bar_02()
  plusAndminus_02()
  bar_02()
  bar_02()
  bar_02()
  bar_02()
  plusAndminus_02()
  bar_02()
  bar_02()
  bar_02()
  bar_02()
  plusAndminus_02()

drawPicture_01()
drawPicture_02()