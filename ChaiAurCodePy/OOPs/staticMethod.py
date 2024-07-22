
# Static means-

#It is a method that belongs to class rather than an instnace of a class.

# This method is accesible to every instance of a class but method defined in an instance are only able to be accessed by that object of class

# @staticmethod  is Decoraters 
#it is use for rule implemntation



class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1
    def full_name(self):
        return f"{self.brand}{self.model}"
    def fuel_type(self):
       return "Petrol or Diesel"
    
    @staticmethod 
    def general_des():
       return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
     super().__init__(brand,model)
     self.battery_size=battery_size

    def fuel_type(self):
       return "Electric Charge"

myCar=Car("Mahendra","Thar")
#print(myCar.general_des())
print(Car.general_des())