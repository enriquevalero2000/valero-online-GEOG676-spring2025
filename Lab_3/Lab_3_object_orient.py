#Functions for shapes
class Shape:
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calcArea(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calcArea(self):
        return 0.5 * self.base * self.height

# Read the file
file = open("C:\\Users\\enriquevalero\\OneDrive - Texas A&M University\\Documents\\GEOG_676(ONLINE)\\repo\\valero-online-GEOG676-spring2025\\Lab_3\\shape.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    attributes = line.split(",")
    Shape = attributes[0]

    if Shape == "Rectangle":
        length = int(attributes[1])
        width = int(attributes[2])
        rectangle = Rectangle(length, width)
        print("Area of rectangle is: ", rectangle.calcArea())
    elif Shape == "Circle":
        radius = int(attributes[1])
        circle = Circle(radius)
        print("Area of circle is: ", circle.calcArea())
    elif Shape == "Triangle":
        base = int(attributes[1])
        height = int(attributes[2])
        triangle = Triangle(base, height)
        print("Area of triangle is: ", triangle.calcArea())
    else:
        pass
