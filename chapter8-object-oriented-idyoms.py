from typing import Any


class Gizmo:
    def __init__(self) -> None:
        print('Gizmo id: %d' % id(self))
x = Gizmo()
print(x)
print(dir())

charles = {'name':'Charles L. Dodgson', 'born':1832}
lewis = charles
print(lewis is charles)
lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is charles)

t1 = (1,2,[3,4])
t2 = (1,2,[3,4])
print(t2 == t2)
t1[-1].append(9)
print(t1)

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print(l1)
print(l2)

class Bus():
    
    def __init__(self, passengers = None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)

import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1),id(bus2), id(bus3))
bus1.drop('Bill')
print(bus2.passengers)
print(bus3.passengers)

def f(a,b):
    a +=b
    return a

x=1
z=2
print(f(x,z))
print(x,z)
x = [1,2]
z = [3,4]
print(f(x,z))
print(x,z)

import weakref
s1 = {1,2,3}
s2 = s1
def bye():
    print('gone')

ender = weakref.finalize(s1,bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)


class Cheese:
    
    def __init__(self, kind) -> None:
        self.kind = kind
    
    def __repr__(self) -> str:
        return 'Cheese(%r)' % self.kind 

import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Parmesan'),Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie')]
for cheese in catalog:
    stock[cheese.kind] = cheese
    
print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
