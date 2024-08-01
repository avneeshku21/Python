def f():
  def g():
    print('inside function g')
    f()
  g()
  print('inside function f')