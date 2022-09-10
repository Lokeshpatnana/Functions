# lambda that returns product of elements of a list
from functools import *
a=[1,2,3,4,56,8,7]
b=reduce(lambda x, y:x+y, a)
c=reduce(lambda x, y:x-y, a)
d=reduce(lambda x, y:x*y, a)
print(b)
print(c)
print(d)