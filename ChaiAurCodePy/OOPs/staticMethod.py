
# Static means-

#It is a method that belongs to class rather than an instnace of a class.

# This method is accesible to every instance of a class but method defined in an instance are only able to be accessed by that object of class

# @staticmethod  is Decoraters 
#it is use for rule implemntation



class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
        Car.total_car+=1
    def full_name(self):
        return f"{self.brand}{self.__model}"
    def fuel_type(self):
       return "Petrol or Diesel"
    
    @staticmethod 
    def general_des():
       return "Cars are means of transport"
    @property
    def model(self):
       return self.__model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
     super().__init__(brand,model)
     self.battery_size=battery_size

    def fuel_type(self):
       return "Electric Charge"

my_tesla=ElectricCar("tesla","Model s","85kwh")
myCar=Car("Mahendra","Thar")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
# print(myCar.model)
#print(myCar.general_des())