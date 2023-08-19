
class Vector2d:
    typecode = 'd'
    
    def __init__(self,x,y) -> None:
        self.x = float(x)
        self.y = float(y)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    
    def __iter__(self):
        return (i for i in (self.x,self.y))

class Foo:
    def __getitem__(self,pos):
        return range(0,30,10)[pos]
    
f = Foo()
print(f[1])
for i in f: print(i)

from typing import Any
from Pythonic_cardDeck import Deck, set_card
from random import shuffle
deck = Deck()
Deck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])



import collections
from collections import abc
Card  = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.abc.MutableSequence):
    
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
     
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,index):
        return self._cards[index]
    
    def __setitem__(self, index, value):
        self._cards[index] = value
    
    def __delitem__(self,index):
        del self._cards[index]
        
    def insert(self, index, value):
        self._cards.insert(index,value)
        

import abc
class Tombola(abc.ABC):
    
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""
    
    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.
        This method should raise `LookupError` when the instance is empty.
        """
    
    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())
    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
    
    
class Fake(Tombola):
        
        def pick(self):
            return 13

        def load(self, iterable):
            self._data = iterable
            
f = Fake()
print(f)


import random

class BingoCage(Tombola):
    
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
        
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        self.pick()
        
    