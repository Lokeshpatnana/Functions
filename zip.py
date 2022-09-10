a=[10,20,30,40,50,60]
b=[1,2,3,4,5]
print(a+b) # here a and b are adding the elements like extend method of list
c=list(zip(a,b))
print(c)

a=[10,20,30,40,50,60]
b=[1,2,3,4,5]
for x,y in zip(a,b):
    print(x,y)

a=[10,20,30,40,50,60]
b=[1,2,3,4,5]
for x,y in zip(a,b):
    print(x+y,x-y)

a=range(10,15)
b=range(1,5)
for x,y in zip(a,b):print(x+y)