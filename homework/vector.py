class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + self.b, other.a + other.b
    
    def __sub__(self, other):
        return self.a - self.b, other.a - other.b
    
x = Vector(2, 4)
y = Vector(5, 7)
print(x + y)
print(x - y)