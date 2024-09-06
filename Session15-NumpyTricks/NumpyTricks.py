
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
a=np.random.randint(1,100,24)
# a.shape
# print(np.expand_dims(a,axis=0).shape)
# print(np.expand_dims(a,axis=1).shape)

# ****np.where
# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.
# print(np.where(a>50))
# print(np.where(condition, true,false))
print(np.where(a>50, 0,a))
print(np.where(a%2==0, 0,a))
