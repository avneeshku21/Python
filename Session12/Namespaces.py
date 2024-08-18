# Namespaces
# A namespace is a space that holds names(identifiers). Programmatically speaking, namespaces are dictionary of identifiers(keys) and their objects(values)

# There are 4 types of namespaces:

# Builtin Namespace
# Global Namespace
# Enclosing Namespace
# Local Namespace

# Scope and LEGB Rule
# A scope is a textual region of a Python program where a namespace is directly accessible.

# The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope. If the interpreter doesn’t find the name in any of these locations, then Python raises a NameError exception.

# *local and global
# global var
# a = 2

# def temp():
#   # local var
#   b = 3
#   print(b)

# temp()
# print(a)

# *local and global -> same name
# a = 2

# def temp():
#   # local var
#   a = 3
#   print(b)

# temp()
# print(a)


# *built-in Scope

# *local and global -> editing global
# a = 2

# def temp():
#   # local var
#   a += 1
#   print(a)

# temp()
# print(a)

# a = 2

# def temp():
#   # local var
#   global a
#   a += 1
#   print(a)

# temp()
# print(a)

# local and global -> global created inside local
# def temp():
#   # local var
#   global a
#   a = 1
#   print(a)

# temp()

# local and global -> function parameter is local
# def temp(z):
#   # local var
#   print(z)

# a = 5
# temp(5)
# print(a)
# print(z)
# print(a)

# built-in scope
# import builtins
# print(dir(builtins))

# renaming built-ins
# L = [1,2,3]
# print(max(L))
# def max():
#   print('hello')

# print(max(L))


# *Enclosing scope
# def outer():
#   def inner():
#     print(a)
#   inner()
#   print('outer function')


# outer()
# print('main program')

