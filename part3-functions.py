




def factorial(n):
    '''returns n!'''  #documentation for function
    return 1 if n<2 else factorial(n-1)*n

print(factorial(5))
print(factorial.__doc__)


fact = factorial
print(fact(5))
map(factorial,range(11)) #repeat calling factorial for each item from range
listA = list(map(fact, range(11)))
print(listA)

## higher order functions
#A function that takes a function as argument or returns a function as the result is a higher-order function.

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits,key=len))

def reverse(word):
    return word[::-1]

print(reverse('testing'))
print(sorted(fruits,key=reverse))


# modern replacement for map, filter, reduce
a = [fact(n) for n in range(6)]
print(a)
b = list(map(factorial, filter(lambda n: n%2, range(6))))
print(b)
c = [factorial(n) for n in range(6) if n%2]
print(c)

# ANONYMOUS FUNCTIONS
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key = lambda word: word[::-1]))

print('--------------------------')
import random
from typing import Any

class BingoCage:
    
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()
    
    #def __repr__(self): #string representation of if it is not present it will print only point into memory of object Vector
     #   return [str(item) for item in self._items]
    
bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(bingo)

#g = [n for n in range(5)]
#print(g)
#print([str(item) for item in g])

print(callable(bingo))
print(dir(bingo))

print('------------------------------------------------')
class C: pass
obj = C()
def func(): pass
print(sorted(set(dir(func)) - set(dir(obj))))

def tag(name, *content, cls=None, **attrs): #argument after the one with * is keyword argument
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s" ' % (attr,value) for attr, value in sorted(attrs.items()))
    else:
        attr_str= ''
    if content:
        return '\n'.join('<%s %s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s %s />' % (name, attr_str)

print(tag('br'))
print(tag('p','hello'))
print(tag('p','hello', 'world','2', cls='sidebar', id='k'))
print(tag(content='testing', name="img"))
my_tag = {'name': 'img', 'title': 'Boulevard', 'src': 'sunste.jpg', 'cls':'framed'}
print(tag(**my_tag))

def f(a,*,b):
    return a,b
print(f(1,b=2))