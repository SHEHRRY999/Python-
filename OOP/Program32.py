class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius
    
    def Perimeter(self):
        return 2 * 3.14 * self.radius
    
c = Circle(35)
print("Area of Circle is: ", c.Area(), " And Perimeter : ", c.Perimeter())
