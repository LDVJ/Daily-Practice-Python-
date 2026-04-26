# class Dog: #  class creation
#     def __init__(self, name, breed): # constructor - runs automatically as soon as this class is called
#         self.dogname = name
#         self.dogbreed = breed

# my_dog = Dog("Tommy","Bulldog")
# print(my_dog.dogname) 
# print(my_dog.dogbreed)
# print(my_dog.__dict__) # whatever attributes are defined in this are stores as a dictonary in this object it is done by self
# # the seperation between the data between different objects is done by self itself
# neighbour_dog = Dog("Rose","German Shepheard")
# print(neighbour_dog.dogname) 
# print(neighbour_dog.dogbreed)
# print(neighbour_dog.__dict__) # whatever attributes are defined in this are stores as a dictonary in this object it is done by self


class Car:
    # suppose i have to know how many car objects have been created using this clas
    # we declare the class variable here
    __car_count = 0

    def __init__(self, brand : str, model : str):
        self.__brand = brand
        self.model = model
        Car.__car_count += 1
    
    def get_brand(self):
        return self.__brand
    
    def full_car_name(self):
        return f"{self.__brand} {self.model}"
    
    @classmethod
    def total_cars(cls):
        return cls.__car_count
    
    @property
    def brand(self):
        return self.__brand

class ElectricCar(Car):

    __electric_car_count = 0

    def __init__(self, brand : str, model : str,battery_size : int):
        super().__init__(brand=brand, model=model)
        self.battery_size  = battery_size
        ElectricCar.__electric_car_count += 1
    
    def car_description(self):
        return f"{self.get_brand()} {self.model} have battery size of {self.battery_size} kw/hr"
    
    @classmethod # methodoverriding 
    def total_cars(cls):
        return cls.__electric_car_count

class Battery:
    def __init__(self, battery : int):
        self.__battery_size = battery
    
    

class Engine:
    pass

my_car = Car("Toyota", "Supra")
# print("Car brand:",my_car.brand)
# my_car.brand = "Farari"
# my_car.model = "Ultra 4"
# print("Car brand:",my_car.brand)
# print("Car Model:",my_car.model)

# print(my_car.full_car_name())
friend_car = Car("Audi","R8")
# print(friend_car.full_car_name())

# now we are going to access the car count vairable defined inside the class -- 


electric_car = ElectricCar("Tesla", "E1", 120)
print("Car instance",isinstance(electric_car, Car))
print("Electric-Car instance",isinstance(electric_car, ElectricCar))
print("Electric-friend-Car instance",isinstance(friend_car, ElectricCar))
print("Bicycle instance",isinstance(electric_car, Bicycle))
# print(electric_car.car_description())
# print("Electric Car Created:",ElectricCar.total_cars())
# print("Car Count with class variable:",Car.total_cars())