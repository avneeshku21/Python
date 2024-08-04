
#* How objects access attributes
# *Note Python me objects mutable hote hai




# class Person:

#   def __init__(self,name_input,country_input):
#     self.name = name_input
#     self.country = country_input

#   def greet(self):
#     if self.country == 'india':
#       print('Namaste',self.name)
#     else:
#       print('Hello',self.name)

# p = Person('Avneesh','india')
# print(p.greet())


# *Attribute creation from outside of the class
# p.gender = 'male'



# *Reference Variables
# p=person() p is hold the refrence
# Reference variables hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variable to an existing object does not create a new object

# why we use p=Person() this syntax?
# because Person k refence ko dobara use krne k liye ye syntax likhte hai

# Pass by reference

# jab bhi ap kisi function ko object pass krna chate ho as input ...... to ap object nhi uska reference or address bhejte ho


# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# # outside the class -> function
# def greet(person):
#   print('Hi my name is',person.name,'and I am a',person.gender)
#   p1 = Person('ankit','male')
#   return p1

# p = Person('nitish','male')
# x = greet(p)
# print(x.name)
# print(x.gender)

# *Object ki mutability

# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# # outside the class -> function
# def greet(person):
#   person.name = 'ankit'
#   return person

# p = Person('nitish','male')
# print(id(p))
# p1 = greet(p)
# print(id(p1))

