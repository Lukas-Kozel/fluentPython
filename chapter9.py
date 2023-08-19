from array import *
import math
class Vector2d:
    typecode = 'd'
    __slots__ = ('__x', '__y')
    
    #nastaveni read only variables
    
    @property
    def x(self):
        return self.__x
    
    @property #marks the getting methods
    def y(self):
        return self.__y
    
    def __init__(self,x,y) -> None:
        self.__x= float(x)
        self.__y=float(y) 
    
    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)
    def __iter__(self):
        return (i for i in (self.x,self.y))
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode,self)))       
    
    def __eq__(self,other) -> bool:
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x,self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)


    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    def angle(self):
        return math.atan2(self.y,self.x)
    
    


brl = 1/2.43
print(brl)
print(format(brl,'0.1f'))
    
print('1BRL = {rate:0.2f} USD'.format(rate=brl))

v1 = Vector2d(3,4)
print(format(v1))
print(format(Vector2d(1, 1), 'p'))
print(v1)