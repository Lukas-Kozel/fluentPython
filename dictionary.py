from collections.abc import Mapping
my_dict = {}
print(isinstance(my_dict, Mapping)) # it means that object my_dict provides certain interface, which basically means that it check if the object is hashtable or mapping
tt=(1,2,(30,40))
print(hash(tt))
tl=(1,2,[30,40])
#print(hash(tl))
a = dict(one=1, two=2,three=3)
c = dict(zip(['one','two','three','four'],[1,2,3,4,5]))
print(a)
print(c)
DIAL_CODES = [
(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}

d={}
#print(d['k'])
print(d.get('k','a'))

import sys
import re
WORD_RE = re.compile('\w+')

#index ={}
#with open(sys.argv[1], encoding='utf-8') as fp:
#    for line_no, line in enumerate(fp,1):
#        for match in WORD_RE.finditer(line):
#            word = match.group()

# BEGIN STRKEYDICT0
class StrKeyDict0(dict):  #when there is another class in () it means it is inherited from it 

    def __missing__(self, key):
        if isinstance(key, str):  # <2>
            raise KeyError(key)
        return self[str(key)]  # <3>

    def get(self, key, default=None):
        try:
            return self[key]  # <4>
        except KeyError:
            return default  # <5>

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # <6>

# END STRKEYDICT0
regular = dict(zip(['2','3'],['two','three']))
d = StrKeyDict0([('2', 'two'),('3','three')])
#print(d[1])
print(regular)

print(d.get('2'))
print(1 in d)


import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key,item):
        self.data[str(key)] = item

print('---------------------------------')
from types import MappingProxyType
d={1:'A'}
d_proxy = MappingProxyType(d) #now d_proxy is read only
print(d_proxy)
d[2] = 'B'
print(d_proxy)

