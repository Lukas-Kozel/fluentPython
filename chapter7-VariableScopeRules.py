from typing import Any


def f1(a):
    print(a)
    print(b)
    
b = 6 #global variable
f1(3)


def f2(a):
    global b
    print(a)
    print(b)
    b=9
    
b = 6 #global variable
f2(3)
print(b)

print('--------------------------------Closures------------------------------')

class Average:
    
    def __init__(self) -> None:
        self.series = []
    
    def __call__(self,new_value) -> Any:
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

avg = Average()
print(avg(10))
print(avg(11))


def make_average():
    series = []
    
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return average

avg = make_average()
print(avg(10))
print(avg(11))

print('--------------------------------Nonlocal Declaration------------------------------')
def make_average():
    count = 0
    total = 0
    def average(new_value):
        nonlocal count, total #nutno pretypovat kvuli chybe pri assignovani variable, ktera neni lokalne (v average) definovana
        count += 1
        total += new_value
        return total / count
    return average


avg = make_average()
print(avg(10))
print(avg(11))

print('-------------------------simple decorator--------------------------------------')
import time

def clock(fcn):
    def clocked(*args):
        t0 = time.perf_counter()
        result = fcn(*args)
        elapsed = time.perf_counter() -t0
        name = fcn.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed,name,arg_str,result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    
    
print('-----------------------improvement-------------------')

import time
import functools

def clock(fcn):
    @functools.wraps(fcn)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = fcn(*args,**kwargs)
        elapsed = time.time() - t0
        name = fcn.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(args) for arg in args))
        if kwargs:
            pairs = ['%s = %r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_lst.append(', '.join(arg_lst))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked

@functools.lru_cache() #zrusi volani funkce pro stejna cisla, ktera jiy byla volana
@clock
def fibonacci(n):
    if n< 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(6))

print('-----------------------generic functions with single dispatch-------------------')

import html
from functools import *
import numbers
from collections import abc

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize(['alpha', 66, {3, 2, 1}]))


registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')
    
print('registry ->', registry)
f1()


registry = set()

def register(active = True):
    def decorate(fcn):
        print('running register(active=%s)->decorate(%s)' % (active, fcn))
        if active:
            registry.add(fcn)
        else:
            registry.discard(fcn)
            
        return fcn
    return decorate

@register(active=False)
def f1():
    print('running f1()')
    
@register()
def f2():
    print('running f2()')
    
def f3():
    print('running f3()')