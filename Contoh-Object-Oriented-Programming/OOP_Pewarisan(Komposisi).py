class Shape:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def draw(self):
        print(f"Drawing {self.color} circle with radius {self.radius}")

circle = Circle("blue", 5)
circle.draw()
