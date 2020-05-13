class Circle(object):
    def __init__(self, r):
       self.radius = r
    def area(self):
       return self.radius**2*3.14
    def chuvi(self):
        return self.radius*2*3.14

aCircle = Circle(3)
print (aCircle.area())
print (aCircle.chuvi())
