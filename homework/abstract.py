import abc

class Shape(abc.ABC):
    @abc.abstractmethod 
    def area(self): pass

class Reactangle(Shape):
    def __init__(self, width, length) -> None:
        super().__init__()
        self.width = width
        self.length = length


    def area(self): return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (self.radius**2) * 3.14


def print_area(shape):
    print(shape.area())

    
rect = Reactangle(10, 5)
print_area(rect)
circle = Circle(5)
print_area(circle)