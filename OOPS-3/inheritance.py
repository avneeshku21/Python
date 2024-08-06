
# *class Relationships
<<<<<<< HEAD
# Two type of realtionships
#dimaond shape
=======
# Two type of relationships
>>>>>>> c5dd0c50d6836539d7732d60f7744d1d69f4ea5b

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
# Triangle shape
#* Benifite- Code Resuseablity

# Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.


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
