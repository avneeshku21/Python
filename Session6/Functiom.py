
#** Function
# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# def my_function():
#   print("Hello from a function")
# my_function()


# def is_even(num):
#   """
#   This function returns if a given number is odd or even
#   input - any valid integer
#   output - odd/even
#   created on - 16th Nov 2022
#   """
#   if type(num) == int:
#     if num % 2 == 0:
#       return 'even'
#     else:
#       return 'odd'
#   else:
#     return 'pagal hai kya?'

# # function
# # function_name(input)
# for i in range(1,11):
#   x = is_even(i)
#   print(x)

# Parameters Vs Arguments
# Types of Arguments
# Default Argument
# Positional Argument
# Keyword Argument

# def power(a=1,b=1):
#   return a**b

# positional argument

# power(2,3)

# keyword argument
# power(b=3,a=2)

#    *args and **kwargs

# *args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function

# *args
# allows us to pass a variable number of non-keyword arguments to a function.

# def multiply(*kwargs):
#   product = 1

#   for i in kwargs:
#     product = product * i

#   print(kwargs)
#   return product

# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

# def display(**kwargs):
#     for(key,value)in kwargs.items():
#         print(key,'->',value)
    
# display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad')


# *Points to remember while using *args and **kwargs
# order of the arguments matter(normal -> *args -> **kwargs)
# *The words “args” and “kwargs” are only a convention, you can use any name of your choice

# **Without return statement

# L = [1,2,3]
# print(L.append(4))
# print(L)

# ****Variable Scope

# def g(y):
#     print(x)
#     print(x+1)
# x = 5
# g(x)
# print(x)

# def f(y):
#     x = 1
#     x += 1
#     print(x)
# x = 5
# f(x)
# print(x)

# ********Nested Functions

def f():
  def g():
    print('inside function g')
    f()
  g()
  print('inside function f')

# *Functions are 1st class citizens
# ******They act as data type
# *type and id
# def square(num):
#   return num**2

# type(square)

# id(square)

# reassign
# x = square
# id(x)
# x(3)

# def func_a():
#     print('inside func_a')

# def func_b(z):
#     print('inside func_c')
#     return z()

# print(func_b(func_a))