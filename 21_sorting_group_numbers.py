"""1st way"""
def num_sort(lis):
    lis.sort()
    for i in lis:print(i,end=" ")
print("Enter Numbers:")
a=[int(x) for x in input().split()]
num_sort(a)

""" 2nd way"""
lst=[int(x) for x in input().split()]
lst.sort(reverse=True)
print(*lst)