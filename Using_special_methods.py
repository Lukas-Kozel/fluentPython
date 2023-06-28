from math import hypot
#hypot = euclidean distance
class Vector:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __repr__(self): #string representation of if it is not present it will print only point into memory of object Vector
        return 'Vector(%r,%r)' % (self.x,self.y)
    
    def __abs__(self):
        return hypot(self.x,self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

v1 = Vector(3,4)
print(abs(v1*3))