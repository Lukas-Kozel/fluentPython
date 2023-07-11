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
