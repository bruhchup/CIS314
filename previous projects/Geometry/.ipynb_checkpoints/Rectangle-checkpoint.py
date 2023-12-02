class rectangle:

    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.area = self.length * self.height

    def getLength(self):
        return self.length

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.area