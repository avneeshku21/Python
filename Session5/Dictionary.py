
# *************Dictionary
# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'Avneesh' , 'age' : 22 , 'gender' : 'male' }

# Characterstics:

#unordred
# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items

# *empty dictionary
# d = {}
# d

# *1D dictionary
# d1 = { 'name' : 'Avii' ,'gender' : 'male' }
# d1


# *with mixed keys
# d2 = {(1,2,3):1,'hello':'world'}
# d2

# *2D dictionary -> JSON
# s = {
#     'name':'Avii',
#      'college':'Mjp',
#      'sem':4,
#      'subjects':{
#          'dsa':50,
#          'maths':67,
#          'english':34
#      }
# }
# s


# *using sequence and dict function
# d4 = dict([('name','nitish'),('age',32),(3,3)])
# d4


# duplicate keys
# d5 = {'name':'nitish','name':'rahul'}
# d5


# mutable items as keys
# d6 = {'name':'nitish',(1,2,3):2}
# print(d6)

#************Accessing items
# my_dict = {'name': 'Jack', 'age': 26}
# # []
# my_dict['age']
# # get
# my_dict.get('age')
# s['subjects']['maths']

#*********Adding key-value pair

# d4['gender'] = 'male'
# d4
# d4['weight'] = 72
# d4

# s['subjects']['ds'] = 75
# s

#***********Remove key-value pair
# d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
# # pop
# #d.pop(3)
# #print(d)
# # popitem
# #d.popitem()
# # d.popitem()
# # print(d)
# # del
# #del d['name']
# #print(d)
# # clear
# d.clear()
# print(d)

# del s['subjects']['maths']
# s

# ***********Dictionary Operations
# Membership
# Iteration

# print(s)

# 'name' in s

d = {'name':'Avii','gender':'male','age':22}

# for i in d:
#   print(i,":",d[i])

#* len/sorted
# len(d)
# print(d)
# sorted(d,reverse=True)
# max(d)

# *items/keys/values
# print(d)

# print(d.items()) # tuple ki form m disply karta hai
# print(d.keys()) #ek sth apke keys ko print krta hai
# print(d.values()) # values ko ek sath display krta hai


# *update
# d1 = {1:2,3:4,4:5}
# d2 = {4:7,6:8}

# d1.update(d2)
# print(d1)

#Dictionary Comprehension
# print 1st 10 numbers and their squares
# {i:i**2 for i in range(1,11)}

# distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
# print(distances.items())


# *using existing dict
# distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
# {key:value*0.62 for (key,value) in distances.items()}

#* using zip
# days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

#** using if condition
# products = {'phone':10,'laptop':0,'charger':32,'tablet':0}

# {key:value for (key,value) in products.items() if value>0}

# Nested Comprehension
# print tables of number from 2 to 4
# {i:{j:i*j for j in range(1,11)} for i in range(2,5)}