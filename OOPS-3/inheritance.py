
# *class Relationships

# Two type of realtionships
#dimaond shape

# Two type of relationships

# 1 Aggregation- Means One Class owns the Other Class
# Agrrigation m jo own class hai bo uske private variable ko access nhi kr skta 
# example
class Customer:

  def __init__(self,name,gender,address):
    self.name = name
    self.gender = gender
    self.address = address

  def print_address(self):
    print(self.address._Address__city,self.address.pin,self.address.state)

  def edit_profile(self,new_name,new_city,new_pin,new_state):
    self.name = new_name
    self.address.edit_address(new_city,new_pin,new_state)

class Address:

  def __init__(self,city,pin,state):
      self.__city = city
      self.pin = pin
      self.state = state

  def get_city(self):
    return self.__city

  def edit_address(self,new_city,new_pin,new_state):
    self.__city = new_city
    self.pin = new_pin
    self.state = new_state

add1 = Address('gurgaon',122011,'haryana')
cust = Customer('Avii','male',add1)

cust.print_address()

cust.edit_profile('Priya','mumbai',111111,'maharastra')
cust.print_address()
# method example
# what about private attribute


#********************Inheritance*************

# *What is Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

#*Triangle shape
#*Benifite- Code Resuseablity
#*Child Class cant use Private member of parent Class

# *Inheritance in summary
# A class can inherit from another class.

# Inheritance improves code reuse

# Constructor, attributes, methods get inherited to the child class

# The parent has no access to the child class

# Private properties of parent are not accessible directly in child class

# Child class can override the attributes or methods. This is called method overriding

# super() is an inbuilt function which is used to invoke the parent class methods and constructor

# Example

# parent
class User:

  def __init__(self):
    self.name = 'nitish'
    self.gender = 'male'

  def login(self):
    print('login')

# child
class Student(User):

  def __init__(self):
    self.rollno = 100

  def enroll(self):
    print('enroll into the course')

u = User()
s = Student()

print(s.name)
s.login()
s.enroll()

# *****************Method Overriding

# *agr Parent or child class m same naam ka method ho to hmesha child class ka method run hoga



# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")

# s=SmartPhone(20000, "Apple", 13)

# s.buy()

#**********Supper Key Word*******************

#Super keyword ka use kr k parent ke members or property  ko use kr skte ho

# Supper Hamehs chlid class m use hota hai bahr use nhi krte 

# Supper cant use  varibale or member


# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")
#         #* syntax to call parent ka buy method
#         super().buy()

# s=SmartPhone(20000, "Apple", 13)
