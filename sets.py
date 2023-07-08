l = ['spam','spam','eggs']
set(l)
print(set(l))
print(list(set(l)))
s = {1}
print(type(s))
s.pop()
print(s)

k = ['spam','kokos']
print(set(k) - set(l))
from unicodedata import name
print({chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')})
