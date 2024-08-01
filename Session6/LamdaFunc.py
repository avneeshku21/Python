# Benefits of using a Function
# Code Modularity
# Code Readibility
# Code Reusability

# *Lambda Function
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# lambda a,b : a+b
# x -> x^2
lambda x:x**2

# x,y -> x+y
# a = lambda x,y:x+y
# a(5,2)

# check if a string has 'a'
# a = lambda s:'a' in s
# a('hello')

# odd or even
# a = lambda x:'even' if x%2 == 0 else 'odd'
# a(6)

# *Diff between lambda vs Normal Function
# No name
# lambda has no return value(infact,returns a function)
# lambda is written in 1 line
# not reusable

# Then why use lambda functions?
# *They are used with HOF

# higher order ek aesa function hota hai jiske return ,khud ek function milta hai


# Example

def square(x):
  return x**2

def cube(x):
  return x**3

# HOF
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(lambda x:x**3,L)

# *Map function
# square the items of a list
list(map(lambda x:x**2,[1,2,3,4,5]))


# odd/even labelling of list items
L = [1,2,3,4,5]
list(map(lambda x:'even' if x%2 == 0 else 'odd',L))


# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

list(map(lambda users:users['gender'],users))

# **Filter

# numbers greater than 5
# L = [3,4,5,6,7]

# list(filter(lambda x:x>5,L))

# fetch fruits starting with 'a'
# fruits = ['apple','guava','cherry']

# list(filter(lambda x:x.startswith('a'),fruits))


# *Reduce
# sum of all item
# import functools

# functools.reduce(lambda x,y:x+y,[1,2,3,4,5])


# find min
# functools.reduce(lambda x,y:x if x>y else y,[23,11,45,10,1])