# Positional arguments demo
def attach(s1,s2):
    s3=s1+s2
    print("Total String is: "+s3)
attach('Hi','Lokesh')

s1,s2=[x for x in input().split(',')]
attach(s1, s2)