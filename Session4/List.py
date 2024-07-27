
#****List is Dynamic
#list me ham value store nhi krte...... hai ham uske address ko store krte hai
#speed of execution is slow because  ham list double krte 
# hai aur copy krte hai ( basically dynamic hai)



# list=[1,2,3]
# print(id(list))  # id  give addresss
# print(id(list[0]))
# print(id(list[1]))
# print(id(list[2]))
# print(id(1))
# print(id(2))
# print(id(3))

# list[0]="a"
# print(list[0])
# print(id(list[0]))
 #Here the memory address will be change after change value of list 

# ***********characterstics of list
# orderd
# chanagable/mutale
# Hetrogeneous
# can have duplicates
# are dyanamic
# can be nested
# items can be accessed
# we   can add contain any kind of objects in python

# L=[1,2,3]
# L1=[3,2,1]
# print(L==L1) # here order is not same
#************************************************
# print([])
#1D
# print([12,3,4,5,6])
#2D
# print([1,2,3,4,5,[4,5]])
#3D


#*******Hetrogenous
# print([1,2,3,True,"Helo"])

#*******Using Type Coversion
#print(list('Hello')) #['H', 'e', 'l', 'l', 'o']

# Accessing item from a list
# list=[1,2,3,4,5,]
# print(list[0])

# slicing
# l=[1,2,3,4,5,6,7]
# print(l[-3:])
# print(l[0::2])

#********** Adding nem Element

# **Append - Append me ham list m ek baar me ek element ko list k end m add kr skte hai
# append me agrr ham multiple store krte hai to  bo ek purri list hi add kr deta hai

# l=[1,2,3,4,5,6,7]
# l.append(10)
#l.append([10,11,12,13,14])
# print(l)


# **Extend
# Extend me ek sath multiple  item ko list m add kr skte hai
l=[1,2,3,4,5,6,7]
l.extend([10,11,12,13,14])
print(l)


# ***insert
#insert m ek baar m ek chiz add hogi multiple chiz add nhi hogi

# L=[1,2,3,4,5,6,7,8]
# L.insert(1,100)
# print(L)







