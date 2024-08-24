# Numpy array vs Python lists

# Why list use over numpy
# Beacause list can store non homogeneous data

# ****Speed
# a=[i for  i in range(10000000)]

# b=[i for  i in range(10000000,200000000)]

# c=[]
# import time
# start=time.time()
# for i in range (len(a)):
#     c.append(a[i]+b[i])

# print(time.time()-start)
#output 3.26sec

#*** numpy
# Why numpy is much faster than list

# Becasue it use C type array means numpy(static) array is fixed in size

# it is not a referncial array means isme ham directly item ko memory m store krte hai na ki address


import time
import numpy as np
# a = np.arange(10000000)
# b = np.arange(10000000,20000000)

# start = time.time()
# c = a + b
# print(time.time()-start)

# memory

# a = [i for i in range(10000000)]
# import sys

# a = np.arange(10000000,dtype=np.int8)
# sys.getsizeof(a)


# *****************Advancing Indexing

# Normal Indexing and slicing

a = np.arange(24).reshape(6,4)
# a
# a[1,2]
# a[1:3,1:3] # Slicing

# Fancy Indexing
 # fancy indexing m ham ek list provide krte hain
# a=[[0,2,3]]
# a[:,[0,2,3]]

# Boolean Indexing
a = np.random.randint(1,100,24).reshape(6,4)
# a
# find all numbers greater than 50
a[a > 50]

# find out even numbers
a[a % 2 == 0]

# find all numbers greater than 50 and are even

a[(a > 50) & (a % 2 == 0)]

# find all numbers not divisible by 7
a[~(a % 7 == 0)]
