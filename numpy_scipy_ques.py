import numpy as np
a = np.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3,4
print(a)
print(a[2])
print(a[2,1])
print(a[:,1])
a.transpose()
print(a)
print('---------------------------------')
#dequeue
from collections import deque
dq = deque(range(10), maxlen=10)
dq.rotate(-4)
dq.appendleft(-1)
dq.extend([11,12,13])
dq.extendleft([10,20,30,40])
print(dq)
