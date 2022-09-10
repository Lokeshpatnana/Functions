# A lambda  function that returns even number from a list
# a=[2,3,1,4,5,6,7,8,9,45,25,16,22]
a=[int(x) for x in input().split()]
b=list(filter(lambda x:(x%2==0), a))
c=list(filter(lambda x:(x%2!=0), a))
print(b)
print(c)