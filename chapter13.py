from array import array
import reprlib
import math
import numbers
from typing import Any
import functools
import operator
import itertools

class Vector:
    
  typecode = 'd'
  
  def __init__(self, components):
      self._components = array(self.typecode, components)
      
      
  def __iter__(self):
      return iter(self._components)
  
  
  def __repr__(self):
      components = reprlib.repr(self._components)
      components = components[components.find('['):-1]
      return 'Vector({})'.format(components)
  
  
  def __str__(self):
      return str(tuple(self))
  
  
  def __bytes__(self):
      return (bytes([ord(self.typecode)]) + bytes(self._components))
    
        
  def __eq__(self, other):
        return tuple(self) == tuple(other)
      
        
  def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
      
      
  def __bool__(self):
        return bool(abs(self))
  
  def __abs__(self):
      return math.sqrt(sum(x*x for x in self))
  
  def __neg__(self):
      return Vector(-x for x in self)
  
  def __pos__(self):
      return Vector(self)
  
  def __add__(self, other):
      pairs = itertools.zip_longest(self,other,fillvalue=0)
      return Vector(a+b for a,b in pairs)
  
  def __radd__(self,other):
      return self + other
  
v1 = Vector([1,2,3])
v1 = v1 + (10,20,30)
v1 = v1 + {20,30}
print(v1)