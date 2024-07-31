# List Comprehension
# List Comprehension provides a concise way of creating lists.

# *newlist = [expression for item in iterable if condition == True]image.png

# Advantages of List Comprehension

# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.
#***************************************************
# Add 1 to 10 numbers to a list (old method)
# L = []

# for i in range(1,11):
#   L.append(i)

# print(L)

# l=[i for  i in range(1,11)]
# print(l)

#**Scalar multiplication on vector
# v=[2,4,5]
# s= -4
# l=[s*i for i in v]
# print(l)

# **add square
# l=[1,2,3,4,5]

# l1=[i*i for i in l]
# print(l1)


# *Print all numbers divisible by 5 in the range of 1 to 50

# l2=[i for i in range(1,51) if i%5 == 0]

# *find languages which start with letter p
# languages = ['java','python','php','c','javascript']

# [language for language in languages if language.startswith('p')]

#*** Nested if with List Comprehension
# basket = ['apple','guava','cherry','banana']
# my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

# [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]

# **Print a (3,3) matrix using list comprehension -> Nested List comprehension

# list=[[i*j for i in range(1,4)] for j in range(1,4)]
# print(list)

# *cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]

product=[i*j for i in L1 for j in L2]
print(product)