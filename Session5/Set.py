# Sets
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

# However, a set itself is mutable. We can add or remove items from it.

# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Characterstics:

# Unordered
# set dose not follow indexing
# Mutable
# No Duplicates
# Can't contain mutable data types

# *empty
#s={} # we cant declare empty set


# s = set() 
# print(s)
# print(type(s))


# *1D and 2D
# s1 = {1,2,3}
# print(s1)
#s2 = {1,2,3,{4,5}} # 2D set is not allowed
#print(s2)

# *homo and hetro

# s3 = {1,'hello',4.5,(1,2,3)}
# print(s3)

#* using type conversion

# s4 = set([1,2,3])
# print(s4)


# *duplicates not allowed
# s5 = {1,1,2,2,3,3}
# print(s5)


# *set can't have mutable items
# s6 = {1,2,[3,4]}
# print(s6)



#* add
S = {1,2,3,4}
# S.add(5)
# print(S)

# *update
S.update([5,6,7]) # ye multiple item ko ek sth add krta hai
print(S)

#********************Deleting Items

s = {1,2,3,4,5}
# print(s)
# del s[0]
# print(s)

# *discard
# s.discard(50)
# print(s)

#* remove
# s.remove(50)
# print(s)

# *pop  # randomly kisi bhi item ko delt kr deta hai
# s.pop()

# *clear
# s.clear()
# print(s)

#************************Set Operation

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1 | s2
# #* Union(|)

# *Intersection(&)
# s1 & s2

#* Difference(-)
# s1 - s2
# s2 - s1

#* Symmetric Difference(^)
# s1 ^ 

#* Membership Test
# 1 not in s1

#* Iteration
# for i in s1:
#   print(i)

#*******************Set Functions

# *len/sum/min/max/sorted
# s = {3,1,4,5,2,7}
# len(s)
# sum(s)
# min(s)
# max(s)
# sorted(s,reverse=True)

#* union/update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# # s1 | s2
# s1.union(s1)

# s1.update(s2)
# print(s1)
# print(s2)

# *intersection/intersection_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# s1.intersection(s2)

# s1.intersection_update(s2)
# print(s1)
# print(s2)

#* difference/difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# s1.difference(s2)

# s1.difference_update(s2)
# print(s1)
# print(s2)

# *symmetric_difference/symmetric_difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# s1.symmetric_difference(s2)

# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)

# *isdisjoint/issubset/issuperset
# s1 = {1,2,3,4}
# s2 = {7,8,5,6}

# s1.isdisjoint(s2)

# s1 = {1,2,3,4,5}
# s2 = {3,4,5}

# s1.issuperset(s2)

# copy
# s1 = {1,2,3}
# s2 = s1.copy()

# print(s1)
# print(s2)

#************************Frozenset

# Frozen set is just an immutable version of a Python set object

# create frozenset
# fs1 = frozenset([1,2,3])
# fs2 = frozenset([3,4,5])

# fs1 | fs2

# what works and what does not
# works -> all read functions
# does't work -> write operations

#* When to use  jab ham read only application banana chate hai to Frozen set use krennge

# *2D sets  yes it is possiable

# fs = frozenset([1,2,frozenset([3,4])])
# fs

#******Set Comprehension
# examples

# {i**2 for i in range(1,11) if i>5}