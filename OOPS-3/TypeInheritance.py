
# **Types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Multiple Inheritance(Diamond Problem)
# Hybrid Inheritance


# single inheritance
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# SmartPhone(1000,"Apple","13px").buy()


#******* multilevel
# class Product:
#     def review(self):
#         print ("Product customer review")

# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(20000, "Apple", 12)

# s.buy()
# s.review()


# **Hierarchical
# There is one Parent and one or more Child




# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# class FeaturePhone(Phone):
#     pass

# SmartPhone(1000,"Apple","13px").buy()
# FeaturePhone(10,"Lava","1px").buy()


# * Multiple
# Do parent ho skte hai with single child


class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()



# the diamond problem
# https://stackoverflow.com/questions/56361048/what-is-the-diamond-problem-in-python-and-why-its-not-appear-in-python2
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class Product:
#     def buy(self):
#         print ("Product buy method")

# # Method resolution order
# class SmartPhone(Phone,Product):
#     pass

# s=SmartPhone(20000, "Apple", 12)

# s.buy()

# Polymorphism

# Having multiple face mtlb sitution k according behave kre


# *Method Overriding
# Inheritance me  parent or child k pass same method ho   tab child class ka method call hota hai

# *Method Overloading

# single class m ek name ke do method hai aur dono ka behaviour alg alg hai depanding on the input

# benifit
#  Code readablity

# *Operator Overloading
# sme operatore depend on input to bheaviour alg alg hojata hai

"Hello"+"World" # conactionation
[1,2,3,4]+[6,7,8,9] # merging