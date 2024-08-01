
# *************Dictionary
# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# Characterstics:

# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items

# *empty dictionary
# d = {}
# d

# *1D dictionary
# d1 = { 'name' : 'nitish' ,'gender' : 'male' }
# d1


# *with mixed keys
# d2 = {(1,2,3):1,'hello':'world'}
# d2

# *2D dictionary -> JSON
# s = {
#     'name':'nitish',
#      'college':'bit',
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