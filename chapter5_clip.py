from clip import clip
from inspect import signature
print(clip.__defaults__)
print(clip.__code__.co_varnames)
sig = signature(clip)
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

from operator import *
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))


from operator import *
from functools import partial
triple = partial(mul,3)
print(triple(6))
print(list(map(triple, range(1,10))))

import unicodedata, functools
nfc = functools.partial(unicodedata.normalize, "NFC")
s1 = 'café'
s2 = 'cafe\u0301'
print(s1,s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))
