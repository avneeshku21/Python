
#*np.sort
# *Return a sorted  copy of an array

import numpy as np
# a=np.random.randint(1,100,24)
# print(a)
# b=np.random.randint(1,100,24).reshape(6,4)
# print(b)
# s=np.sort(a)
# s=np.sort(a)[::-1] # for Descending order
# print(s)

# *two dim array k liye np.sort(b=axis-0)



#******************* Append
# *np. append()
# *The numpy.append() appends values along the mentioned axis at the end of the array

# *Two D array me ek exiting columb aad krne k liye
# np.append(b,np.random.random((b.shape[0],1)),axis=1)


#****************** Concatenate
# numpy.concatenate() function concatenate a sequence of arrays along an existing axis.
# concatenate is moslty used for table of data

# c = np.arange(6).reshape(2,3)
# d = np.arange(6,12).reshape(2,3)

# *columb wise
# np.concatenate((c,d),axis=0)

#*Rowwise
# np.concatenate((c,d),axis=1)


# ******************np.unique
# With the help of np.unique() method, we can get the unique values from an array given as parameter in np.unique() method.
# code
# e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])

# print(np.unique(e))
# print(np.unique(e))

# np.expand_dims
# With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array

# Using expand_dims  we can  convert 1D array to 2D array  or 2D array to 3D array

#***** code
# a=np.random.randint(1,100,24)
# a.shape
# print(np.expand_dims(a,axis=0).shape)
# print(np.expand_dims(a,axis=1).shape)

# ***************np.where
# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.
# print(np.where(a>50))
# print(np.where(condition, true,false))
# print(np.where(a>50, 0,a))
# print(np.where(a%2==0, 0,a))

# ****************np.argmax
# The numpy.argmax() function returns indices of the max element of the array in a particular axis.

# Note- kisi bhi array m sbse max element nikalne ka tarika hai
# a=np.random.randint(1,100,24)
# print(np.argmax(a))
# b=np.random.randint(1,100,24).reshape(6,4)
# print(np.argmax(b,axis=1))

#******************* np.cumsum (cummulative Sum)
#  numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis.

# **np.cumsum(a)
b=np.random.randint(1,100,24).reshape(6,4)
np.cumsum(b,axis=1)

# *******************np.percentile
# numpy.percentile()function used to compute the nth percentile of the given data (array elements) along the specified axis.
# https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
a=np.random.randint(1,100,24)
np.percentile(a,50)
np.median(a)

# ******************np.histogram
# Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.
# Note- ye Frequency count batata hai in a given range
# https://numpy.org/doc/stable/reference/generated/numpy.histogram.html

# *np.histogram(a,bins=[0,50,100])

# np.corrcoef
# Return Pearson product-moment correlation coefficients.

# https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html

# salary = np.array([20000,40000,25000,35000,60000])
# experience = np.array([1,3,2,4,2])

# np.corrcoef(salary,experience)

# **********************np.isin
# With the help of numpy.isin() method, we can see that one array having values are checked in a different numpy array having different elements with different sizes.

# https://numpy.org/doc/stable/reference/generated/numpy.isin.html

# ***********************np.flip
# The numpy.flip() function reverses the order of array elements along the specified axis, preserving the shape of the array.

# https://numpy.org/doc/stable/reference/generated/numpy.flip.html

# np.flip(a)
# np.flip(b,axis=1)

# np.put
# The numpy.put() function replaces specific elements of an array with given values of p_array. Array indexed works on flattened array.

# https://numpy.org/doc/stable/reference/generated/numpy.put.html

# np.put(a,[0,1],[110,530])

# np.delete
# The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis.

# https://numpy.org/doc/stable/reference/generated/numpy.delete.html

# code
# a
# np.delete(a,[0,2,4])