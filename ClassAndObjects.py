#Class Is a bluprint to create and object
class Student:
    name="ali"
#S is an object here , sab students ka naam ali hai
s=Student()
print(s.name)
b=Student()
print(b.name)

#Calculate Area and Perimeter using OOP
import math
#Defining Class
class Circle:
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius

radius=int(input("Enter Radius \t"))
#Define Object // Radius hum argument pass kar rahay hain to the constructor of class when creating object
 
circle=Circle(radius)
#Object kai method ko print karo 
# You always forget() in printing method
print(circle.area())
print(circle.perimeter())

# Write a Python program to create a person class. Include attributes like name, country and date of birth.
from datetime import date
class Person:
    def __init__(self, name,country,datebirth):
        self.name=name
        self.country=country
        self.datebirth=datebirth
#person is an object that has attributes name etc    
person=Person("Yusra","Pakistan",date(2001,12,22))
print(person.name , person.country , person.datebirth)

# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Car:
    def __init__(self , maxspeed , milleage):
        self.maxspeed=maxspeed
        self.milleage=milleage
car=Car("78" , "600")
print(car.maxspeed , car.milleage)

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Mairay Pass aik Vehcile hai aur Bus ki class hai 
# Method overriding mai two methods have same name liken dono methods will perform diff tak
class Vehicle:
    def __init__(self , name , maxspeed , milleage):
        self.name=name
        self.maxspeed=maxspeed
        self.milleage=milleage
    
    def seating_capacity(self , capacity=9):
        return f"The Seating Capacity of   {self.name}  is  {capacity}"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity=0):
        return super().seating_capacity(capacity)
    # superkeyword is used to access methods and attributes from parent class

vehicle=Vehicle("Car" , 8900 ,89)
bus=Bus("Bus" , 600 , 90)
# Class Bus inherits Class Vehicle liken jab subclass ka object method ko call karay gaa toh subclass will execute its own method
print(bus.name , bus.seating_capacity())
print(vehicle.name , vehicle.seating_capacity())


# Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# ClassVar is a Var shared among all childclass of parentclass . Initialized outside instanceclass
class Vehicle:
    color="white" #Class Variable
    def __init__(self , name , speed , milleage):
        self.name=name
        self.speed=speed
        self.milleage=milleage
        
class Bus(Vehicle):
    pass
class Train(Vehicle):
    pass

vehicle=Vehicle("Car" , 8900 ,90)
bus=Bus("Bus" , 67 ,89)
train=Train("Train" ,78, 90 )
print(train.milleage, train.color)
print(bus.color)
print(vehicle.color)

# Encapsulation Get And Set Method
class Student:
    def __init__(self , name , age ,grade):
        self.__name=name 
        self.__age=age
        self.__grade=grade
  
    # Get Methods that are used to retrive values of private attributes
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_grade(self):
        return self.__grade

    # Set Methods that are used to modify teh values of private attributes
    def set_name(self , name):
        self.__name = name
    
    def set_age(self,age):
        if age > 0:
            self.__age==age
        else:
            print("The Age Should be in Positive Numbers")
    
    def set_grade(self,grade):
        if grade == [f"A+ , B+"]:
            self.__grade=grade
        else:
            print("The Grade Should be A and B +")

student=Student("Ali" , 9 ,"A")

# Get Method 
print(student.get_name() , student.get_age() , student.get_grade())
# Error since you cant access attribute because they are private , you cant access outside the class
# koi method sai hum access karsaktay hain inside the class

# Set Method
student.set_name("Ahmed")
student.set_age(10)
student.set_grade("B")

# Using getter methods again to check the changes
print("Name:", student.get_name())   # Output: Ahmed
print("Age:", student.get_age())     # Output: 10
print("Grade:", student.get_grade()) # Output: B

# Method Overloading
class Calc:
    def add(self, x, y, z=None):
        if z is None:
            print("x + y = {}".format(x + y))
        else:
            print("x + y + z = {}".format(x + y + z))
zz = Calc()
zz.add(4, 2, 3)  # Output: x + y + z = 9
zz.add(4, 2)     # Output: x + y = 6

# Set Attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
person = Person("Alice", 30)

# Displaying initial attributes
print("Initial attributes:")
print("Name:", person.name)
print("Age:", person.age)

# Using setattr() to change attribute values
setattr(person, 'name', 'Bob')
setattr(person, 'age', 25)

# Displaying updated attributes
print("\nUpdated attributes:")
print("Name:", person.name)
print("Age:", person.age)
