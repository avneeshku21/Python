
#***************2 ways to traverse a list
# itemwise
# indexwise


#****itemwise
# l=[1,2,3,4,5,6]
# for i in l:
#     print(i)


# *****indexwise
# l=[1,2,3,4,5]
# for i in range(0,len(l)):
#     print(i,l[i])


# Zip
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# L1 = [1,2,3,4]
# L2 = [-1,-2,-3,-4]

# list(zip(L1,L2)) 

# [i+j for i,j in zip(L1,L2)]

# L = [1,2,print,type,input] #list me ham builtin function bhi store kr skte hai

# print(L)

# Disadvantages of Python Lists
# Slow
# Risky usage
# eats up more memory