
from abc import ABC, abstractmethod

import math
class Shape():
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass
    @abstractmethod
    def get_name(self):
        pass

class Point2D:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x:.2f}, {self.y:.2f}"

class Circle(Shape):
    def __init__(self, center:Point2D,radius:float):
        self.center = center
        self.radius = radius
        self.name = "Circ"

    def get_name(self):
        return self.name
    def get_area(self):
        return math.pi * (self.radius ** 2)
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"{self.get_name()}: C=({self.center}), R={self.radius:.2f}"
    

class Rectangle(Shape):
    def __init__(self, p1:Point2D, p2:Point2D):
        self.p1 = p1
        self.p2 = p2
        self.name = "Rect"
    

    def get_name(self):
        return self.name
    
    def get_area(self):
        width = abs(self.p2.x - self.p1.x)
        height = abs(self.p2.y - self.p1.y)
        return width * height
    
    def get_perimeter(self):
        width = abs(self.p2.x - self.p1.x)
        height = abs(self.p2.y - self.p1.y)
        return 2 * (width + height)
    

    def __str__(self):
        return f"{self.get_name()}: P1=({self.p1}) P2=({self.p2})"
        

def main():
    shapes = []
    while True:
        try:
            line = input()
            args = line.split()
            cmd = args[0]
            print("$" + line)
            if cmd == "circle":
                x = float(args[1])
                y = float(args[2])
                r = float(args[3])
                circle = Circle(Point2D(x,y),r)
                shapes.append(circle)
            elif cmd == "rect":
                x1 = float(args[1])
                y1 = float(args[2])
                x2 = float(args[3])
                y2 = float(args[4])
                rectangle = Rectangle(Point2D(x1,y1),Point2D(x2,y2))
                shapes.append(rectangle)
            elif cmd == "info":
                for shape in shapes:
                    print(f"{shape.get_name()}: A={shape.get_area():.2f} P={shape.get_perimeter():.2f}")
            elif cmd == "show":
                for shape in shapes:
                    print(str(shape))
            elif cmd == "end":
                break
            else:
                print("fail: command invalid")

        except Exception as e:
            print("fail:", e)
        

main()