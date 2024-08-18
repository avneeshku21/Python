# Namespaces
# A namespace is a space that holds names(identifiers).Programmatically speaking, namespaces are dictionary of identifiers(keys) and their objects(values)

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