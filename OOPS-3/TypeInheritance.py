
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