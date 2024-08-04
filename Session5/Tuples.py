# Tuples
# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# Characterstics

# Ordered
# Unchangeble/ immutable
# Allows duplicate

#* empty
t1 = ()
print(t1)

# *create a tuple with a single item
# t2 = ('hello',)
# print(t2)
# print(type(t2))

# *homo
# t3 = (1,2,3,4)
# print(t3)

#* hetro

# t4 = (1,2.5,True,[1,2,3])
# print(t4)


# *tuple
t5 = (1,2,3,(4,5))
print(t5)

# *using type conversion
# t6 = tuple('hello')
# print(t6)

# *Accessing Items
# Indexing
# Slicing

# t3 = (1,2,3,4)
# print(t3)
# print(t3[0])

# *Editing items

# print(t3)
# t3[0] = 100
# immutable just like strings

# Deleting items
t3 = (1,2,3,4)
# print(t3)
# del t3
# print(t3)

#******************Operations on Tuples

# *+ and *
# t1 = (1,2,3,4)
# t2 = (5,6,7,8)

# print(t1 + t2)

# print(t1*3)

# *membership
1 in t1

#* iteration
for i in t1:
  print(i)

#********************Tuple Functions

# *len/sum/min/max/sorted

# t = (1,2,3,4)
# len(t)

# sum(t)

# min(t)

# max(t)

# sorted(t,reverse=True)

# *count

# t = (1,2,3,4,5)

# t.count(50)

#* index

# t.index(50)

# ****Difference between Lists and Tuples
# Syntax
# Mutability
# Speed
# Memory
# Built in functionality
# Error prone
# Usability

#* tuple unpacking
# a,b,c = (1,2,3)
# print(a,b,c)

# a,b,*others = (1,2,3,4)
# print(a,b)
# print(others)

#*swap
# a = 1
# b = 2
# a,b = b,a

# print(a,b)

# zipping tuples
# a = (1,2,3,4)
# b = (5,6,7,8)

# tuple(zip(a,b))