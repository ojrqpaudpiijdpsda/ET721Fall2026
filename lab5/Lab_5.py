'''
Lab 5: review of class, object, methods, asnd attributes
Jiaxi Pang
Sep 16, 2026

'''
print('\n ----- Example 1: class Circle -----')

class Circle():
    #values that need to pass to the object of class Circle
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    #attributes
    pi = 3.14157

    #method
    def circumference(self):
        return 2*self.pi*self.radius

    


ci1 = Circle(2, 'red')
print(ci1.color)
print(ci1.circumference())


print('\n ----- Example 2: class Rectangle -----')

class Rectangle():
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

    #method to calculate the area
    def area(self):
        return self.w * self.h

    #method to calculate the perimeter
    def perimeter(self):
        return 2*self.w + 2*self.h
    '''
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.w, self.h, fc = self.c ))
        plt.axis('scaled')
        plt.show()
    
    '''
    
#create instance object of the class
r1 = Rectangle(2,3, "Green")
print(r1.h)
print(r1.w)
print(r1.c)
print(f'The perimeter of ractangle with heigh = {r1.h}, width = {r1.w}, is {r1.perimeter}')
#r1.drawRectangle()

'''
Cars dealership's inventory management system
You are working on a Python program to simulate a cars dealerships inventory management system. The system aims to model cars and their attributes accurately
Task 1: create class to represent each vehicle. Each car should have attributes for maximum speed and mileage
Task 2: update the class with the default color for all vehicles, "white"
Task 3: create a class method rto assign seating capacity to a vehicle
Task 4: create a class method to display all the properties of an object class --> ' the car has _ seats, with _ miles and maximum speed of _ '
Task 5: create two instance objects of the car. One car will have a max speed of 200kph and mileage of 50000 kmpl with five seating capacity.
The other car maxSpeed = 180kph, mileage = 75000kmpl, four seating
'''

class car():
    def __init__(self, maxSpeed, mileage) :
        self.maxSpeed = maxSpeed
        self.mileage = mileage

    
    defaultColor = 'white'

    def capacity(self, capacity):
        self.cap = capacity
        
    
    def displayAll(self):
        print(f' the car has {self.cap} seats, with {self.mileage} miles and maximum speed of {self.maxSpeed}')


c1 = car(200, 50000)
c1.capacity(5)
c1.displayAll()
c2 = car(180, 75000)
c2.capacity(4)
c2.displayAll
