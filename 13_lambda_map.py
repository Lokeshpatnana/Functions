# lambda that returns squares
# list1=[1,5,9,3,7,4]
list1=[int(x) for x in input().split()]
list2=list(map(lambda x:x**2, list1))
print(list2)