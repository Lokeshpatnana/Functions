def num(name1='3.10.5',Hello="Python"):   # Function Declaration
    print("Function Program Basics",Hello,name1)
num()  ;''' num should be exactly at left, it is for calling the function '''
num(22,'lokesh')
num('josh','innovations')
num('evng','func topic')
num(name1=22)
num(Hello=16)

""" At the time of calling a function and passing a values into it
then the values passed during the calling function will be taken 
into consideration. it is nothing but the values have been updated. """

def j(loki):
    print('Lokesh')
j(22)