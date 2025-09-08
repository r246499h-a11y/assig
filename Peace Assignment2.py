#Peace Makonyonga
#R246499H
# QUESTION 1

# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} vehicle engine started.")

# Subclass 1
class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def start_engine(self):
        print(f"{self.brand} car with {self.doors} doors is starting with a key ignition.")

# Subclass 2
class Bike(Vehicle):
    def __init__(self, brand, type_of_bike):
        super().__init__(brand)
        self.type_of_bike = type_of_bike

    def start_engine(self):
        print(f"{self.brand} {self.type_of_bike} bike is starting with a kick or button.")

# Testing the classes
v = Vehicle("Generic")
c = Car("Toyota", 4)
b = Bike("Yamaha", "sport")

v.start_engine()  # Output: Generic vehicle engine started.
c.start_engine()  # Output: Toyota car with 4 doors is starting with a key ignition.
b.start_engine()  # Output: Yamaha sport bike is starting with a kick or button.


# QUESTION 2
import math
from abc import ABC, abstractmethod

# Base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function using polymorphism
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

# Example usage
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3)
]

print("Total area of all shapes:", total_area(shapes))


# QUESTION 3

# Base class
class Shape:
    def __init__(self, name):
        self.name = name
        print(f"Shape initialized: {self.name}")

    def calculate_area(self):
        print("Base Shape: calculate_area called (no calculation).")


# Derived class
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)  # Call Shape's constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        # Optionally call the base class's version of calculate_area
        super().calculate_area()

        # Now perform the actual area calculation
        area = self.width * self.height
        print(f"{self.name} Rectangle area: {area}")
        return area


# Example usage
rect = Rectangle("MyRectangle", 5, 3)
area = rect.calculate_area()


#QUESTION 4

## Dog class
class Dog:
    def make_sound(self):
        print("Woof! Woof!")

# Cat class
class Cat:
    def make_sound(self):
        print("Meow...")

# Function that uses duck typing
def process_sound(sound_object):
    sound_object.make_sound()

# Usage
dog = Dog()
cat = Cat()

process_sound(dog)  # Output: Woof! Woof!
process_sound(cat)  # Output: Meow...


#QUESTION 5

from abc import ABC, abstractmethod

# Abstract Base Class
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        """Read data from a file"""
        pass

    @abstractmethod
    def write(self, data):
        """Write data to a file"""
        pass

# Concrete class for handling text files
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        print("Text file read successfully.")
        return content

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)
        print("Text file written successfully.")

# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            content = file.read()
        print("Binary file read successfully.")
        return content

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)
        print("Binary file written successfully.")

# Example usage
if __name__ == "__main__":
    # Handling a text file
    text_handler = TextFileHandler("example.txt")
    text_handler.write("Hello from a text file!")
    print(text_handler.read())

    # Handling a binary file
    binary_handler = BinaryFileHandler("example.bin")
    binary_handler.write(b'\x48\x65\x6C\x6C\x6F')  # Binary for "Hello"
    print(binary_handler.read())


