import numpy as np

class circle:

    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.circumference = 2 * np.pi * self.radius 
        self.area = np.pi * (self.radius**2)

    def getRadius(self):
        return self.radius

    def getDiameter(self):
        return self.diameter

    def getCircumference(self):
        return self.circumference

    def getArea(self):
        return self.area
        
    