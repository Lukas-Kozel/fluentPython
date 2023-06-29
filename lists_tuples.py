import array
from collections import namedtuple
def compareList(list1, list2):
    for item in list1:
        if item not in list2:
            return False
    return True


symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii_map = list(filter(lambda c: c > 127, map(ord,symbols)))
print(beyond_ascii_map)
symbols2 = '$¢a£¥€¤'
codes2 = [ord(symbol) for symbol in symbols2]

print(compareList(codes,codes2))

x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

#nasobeni matic:
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]


#generator expressions
symbols =  '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('i', (ord(symbol) for symbol in symbols)))

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

a,b, *rest = range(5)
print(a,b,rest)


metro_areas = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longtitude) in metro_areas:
    if longtitude <=0:
        print(fmt.format(name,latitude, longtitude))

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.coordinates)
print(tokyo._fields)
dict = tokyo._asdict()
print(dict)
print(dict.get('name'))
for key, value in dict.items():
    print(key + ':', value)
