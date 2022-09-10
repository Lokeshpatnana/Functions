# A Lambda function that returns bigger number
b=lambda x,y:x if x>y else y   # write lambda function
x,y=[int(n) for n in input("Enter two numbers:").split()]
print(b(x,y))

a=[int(b) for b in input("Enter Numbers:").split()]
print("Bigger Number is:",max(a))
print("Smaller Number is:",min(a))

c=[20,25,41,12,66]
print(max(c))
print(min(c))