# Example on Local And Global Variable

a=50 # Global Variable
def number():
    b=25  # Local Variable
    a=32
    print(a)
    print("Local Variable b:",b)
    print("Global VAriable a:",a)
print("Global Variable a:",a)
number()
print("Global Variable a:",a)

a=150
def fn():
    global a
    a=30
    print(a)
print(a)
fn()
print(a)