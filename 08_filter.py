# filter() function that returns even numbers from a list

def any(x):
    if x%2==0:
        return True
    else:
        return False
print(any(52))

# Let us take list of two numbers
loki=[10,23,45,25,63,78,92]
a=list(filter(any, loki))
print("From the loki the even values are:",a)
print("From the loki the odd values are:",a)

# call filter() with is even and list
b=[int(x) for x in input().split()]
c=list(filter(any, b))
print("From the b the even values are:",c)