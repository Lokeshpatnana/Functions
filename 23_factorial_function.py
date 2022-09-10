"""1st way"""
def factor(b):
    if b==0:
        return 1
    else:
        a=b*factor(b-1)
        return a
b=abs(int(input("Enter any Number:")))
print(f"{b}! =",factor(b))

"""2nd way"""
import math
print(math.factorial(6))