# Strings are sequence of Characters

# In Python specifically, strings are a sequence of Unicode Characters

# Creating Strings
# Accessing Strings
# Adding Chars to Strings
# Editing Strings
# Deleting Strings
# Operations on Strings
# String Functions

# s = 'hello'
# s = "hello"
# # multiline strings
# s = '''hello'''
# s = """hello"""
# s = str('hello')
# print(s)

# Positive Indexing
s = 'hello world'
print(s[41]) ## outside the range

# ******Slicing
# s = 'hello world'
# print(s[0:5])
# print(s[0:5:2])  #jump for two char

# print(s[::-1]) # easy ways to reverse the string

# s = 'hello world'
# print(s[-1:-6:-1])

#******Editing and Deleting in Strings
s = 'hello world'
s[0] = 'H'

# Noteeee......Python string are immutable

#************ Delet
s = 'hello world'
del s
print(s)

# Operations on Strings
# Arithmetic Operations
# Relational Operations
# Logical Operations
# Loops on Strings
# Membership Operations

# print('delhi' + ' ' + 'mumbai')

# print('delhi'*5)

# 'delhi' != 'delhi'

# 'mumbai' > 'pune'
# # lexiographically
# print(
# 'Pune' > 'pune')

# print('hello' and 'world')

# print('' and 'world')

# print('' or 'world')

# print(not 'hello')

# for i in 'hello':
#   print(i)


# print('D' in 'delhi')