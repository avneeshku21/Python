# What is numpy?
# NumPy is the fundamental package for scientific computing in Python. 

# It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

# At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types

# *Why use numpy?

# Because Python datatype is slow thats why numpy is create

# *Numpy Arrays Vs Python Sequences

# NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.

# The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.

# NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

# A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.


import numpy as np
# *1D array
# a=np.array([1,2,3,4,5])
# print(a)
# print(type(a))

# *2D array
# b=np.array([[1,2,3,4],[6,7,8,9]]) # Matrix
# print(b)
#* 3D
# c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c) # Tensor


# **dtype
# np.array([1,2,3],dtype=float)
# np.array([1,2,3],dtype=complex)

# *np.arange
# np.arange(1,11,2)


# *with reshape
# x=np.arange(1,11).reshape(2,5)
# print(x)

# d=np.arange(16).reshape(2,2,2,2)
# print(d)


# *np.ones and np.zeros
# isme sare k sare item One hote aur zero hote hai
# it is use in Neural network

# print(np.ones((3,4)))

# print("*****************")

# print(np.zeros((3,4)))

# *np.random
# np.random.random((3,4))

# *np.linspace
#Range provide krte hai 
# 1. lower range 2. upper range 3. number of items
# Ye given range m equally points generate krta hai
# np.linspace(-10,10,10,dtype=int)

# *np.identity # Identity Matrix
# np.identity(3)

# *******************Array Attributes************
# a1 = np.arange(10,dtype=int)
# a2 = np.arange(12,dtype=float).reshape(3,4)
# a3 = np.arange(8).reshape(2,2,2)

# *ndim (number of dimesion) give array ko btata hai 1d h 2d 
# a3.ndim

#* shape
# print(a3.shape)


# *size Number of element present
# print(a2.size)
# a2

# *itemsize Memrory size
# a3.itemsize


# *dtype item ka datatype batata hai
# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)

# * Changing Datatype

# astype
# a3.astype(np.int32)

#**************** Array Operations*************

# a1 = np.arange(12).reshape(3,4)
# a2 = np.arange(12,24).reshape(3,4)

# a2

# scalar operations

# *arithmetic
# a1 ** 2

# *relational
# a2 == 15

# * vector operations
# arithmetic
# a1 ** a2

#*************************** Array Functions*******

# a1=np.random.random((3,3))

# a1=np.round(a1*100)

#*max/min/sum/prod
# 0 -> col and 1 -> row
# np.max(a1)

# np.max(a1 ,axis=1)
# np.min(a1)
# np.prod(a1,axis=0)

#* mean/median/std/var
# np.var(a1,axis=1)

# *trigonomoetric functions
# np.sin(a1)

# *dot product
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(12,24).reshape(4,3)

# np.dot(a2,a3)

# *log and exponents
# np.exp(a1)

# log and exponents
# np.exp(a1)
# round/floor/ceil

# np.ceil(np.random.random((2,3))*100)

### ************Indexing and Slicing************
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# a2[1,0]
# a3[1,0,1] #3rd me konse 2nd array then row then col


#**Slicing
# a1[2:5]

a2[0:2,1::2]
print(a2[::2,1::2])
a2[::2,1::2]

# **iterating
# for i in a1:
#     print(i)

# for i in a2:
#     print(i)

# for i in np.nditer(a3): #nditer func will chnge into oned array
#     print(i)


# *Transpose
np.transpose(a2)
a2.T

# ravel # it convert 1D array
a3.ravel()

# ***Stacking*********************

# horizontal stacking
# a4 = np.arange(12).reshape(3,4)
# a5 = np.arange(12,24).reshape(3,4)
# a5

# np.hstack((a4,a5))

# Vertical stacking
# np.vstack((a4,a5))

# Splitting
# horizontal splitting
#np.hsplit(a4,5)

# np.vsplit(a5,2)