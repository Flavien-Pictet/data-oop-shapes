import math

class Shape:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    def say_name(self):
        return f"My name is {self.name}"

class Rectangle(Shape):
    def __init__(self, color, name, width, height):
        Shape.__init__(self, color, name)
        self.width = width
        self.height = height

    def say_name(self):
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        area_ = self.width * self.height
        return area_

    def perimeter(self):
        perimeter_ = (self.height + self.width) * 2
        return perimeter_

class Circle(Shape):
    def __init__(self, color, name, radius):
        Shape.__init__(self, color, name)
        self.radius = radius

    def say_name(self):
        return f"My name is {self.name} and I am a circle."

    def area(self):
        area_ = math.pi * ( self.radius ** 2 )
        return area_

    def perimeter(self):
        perimeter_ = 2 * math.pi * self.radius
        return perimeter_
