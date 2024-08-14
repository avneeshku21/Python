# There are 2 stages where error may happen in a program

# During compilation -> Syntax Error
# During execution -> Exceptions

# **************Syntax Error*******************
# Something in the program is not written according to the program grammar.
# Error is raised by the interpreter/compiler
# You can solve it by rectifying the program

#  Examples of syntax error
# print 'hello world'

# Other examples of syntax error
# Leaving symbols like colon,brackets
# Misspelling a keyword
# Incorrect indentation
# empty if/else/loops/class/functions

# *IndexError
# The IndexError is thrown when trying to access an item at an invalid index.
L = [1,2,3]
L[100]

# *ModuleNotFoundError
# The ModuleNotFoundError is thrown when a module could not be found.
# import mathi
# math.floor(5.3)

# NOTE: If your import is failing due to a missing package, you can
# manually install dependencies using either !pip or !apt.

# To view examples of installing some common dependencies, click the
# "Open Examples" button below.

# *KeyError
# The KeyError is thrown when a key is not found

# d = {'name':'nitish'}
# d['age']


# *TypeError
# The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
# 1 + 'a'

# **************ValueError
# The ValueError is thrown when a function's argument is of an inappropriate type.
# int('a')

# ***************NameError
# The NameError is thrown when an object could not be found.
# print(k)

# ************AttributeError
# L = [1,2,3]
# L.upper()

# # Stacktrace


# *****************Exceptions******************

# If things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened.
# Logical Error

# Exceptions are raised by python runtime
# You have to takle is on the fly

# *Examples
# Memory overflow
# Divide by 0 -> logical error
# Database error


# *********Why is it important to handle exceptions
# how to handle exceptions
# -> Try except block

# let's create a file
# with open('sample.txt','w') as f:
#   f.write('hello world')


# try catch demo
# try:
#   with open('sample1.txt','r') as f:
#     print(f.read())
# except:
#   print('sorry file not found')


# *catching specific exception
# try:
#   m=5
#   f = open('sample1.txt','r')
#   print(f.read())
#   print(m)
#   print(5/2)
#   L = [1,2,3]
#   L[100]
# except FileNotFoundError:
#   print('file not found')
# except NameError:
#   print('variable not defined')
# except ZeroDivisionError:
#   print("can't divide by 0")
# except Exception as e:
#   print(e)

# *else
try:
  f = open('sample1.txt','r')
except FileNotFoundError:
  print('file nai mili')
except Exception:
  print('kuch to lafda hai')
else:
  print(f.read())