""" Local Scope
Value can be accessed inside the function only """
# """
def fun():
    x=6;y=5;z=3
    print(x+y)
fun()
# """

""" Global Scope of a Variable, can be accessed by any one """
# """
a=3
def bcd():
    a=4
    b=3;c=9
    print(a)
    print(b)
print(a)
bcd()
print(a)
# """

""" Global is the keyword, which is need to be specified if we want to use
the local variable as global variable """
# """
c=2
b=55
def funy():
    a=5
    global c,b
    b=7
    c=6
    print(b)
print(c)
funy()
print(c)
print(b)
print(c)
# """

""" Count the Length of the String without using built-in function{len method} """
# """
def fn(st):
    c=0
    for i in st:
        c+=1
    return c
print(fn('Lokesh'))
# """

""" A Guy Having Multiple Names """
# """
def sc():
    school='sths'
    print(f"Name in School is {school}")
    cl()
def cl():
    college='s.k&r.k'
    print(f"Name in college is {college}")
    wk()
def wk():
    work='office' 
    print(f"Name  at work location is {work}")
    sc()
wk()
# """