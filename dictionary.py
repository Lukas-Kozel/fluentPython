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
print(d.get('k'))

import sys
import re
WORD_RE = re.compile('\w+')

index ={}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            