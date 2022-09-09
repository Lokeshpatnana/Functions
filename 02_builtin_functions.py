''' Pre-Defined Functions '''

''' sorted() '''
# a=[2,3,6,4,1,5]
# a.sort()
# print(a)
# print(sorted([22,26,27,24,28,23,25]))
# print(sorted([8,7,5,6,0,-1,-2]))
# a=['a','A','Z','z']
# print(sorted(a))
# print(ord('a'))
# print(chr(122))

''' all() '''
# print(all([True,1,2]))
# print(all([True,'',1,2]))
# print(all([True,' ',1,2]))
# print(all([True,False,1,2]))
# print(all([True,True,1,2,0]))
# print(all([True,True,1,2,None]))
# print(all((True,True,1,2,None)))

''' any() '''
# print(any([True,False,False,0,23]))
# print(any([False,False,'']))
# print(any([True,True,None,0]))

''' bool() '''
# print(bool(False))
# print(bool(1))
# print(bool(0))
# print(bool(None))
# print(bool('bool'))
# print(bool(''))
# print(bool(' '))

''' eval() '''
# print('eval=',eval("7+4.2-5"))
# a=eval('6+4-1')
# b=eval('2+4.3-1')
# print(a,type(a))
# print(b,type(b))

''' sum() '''
# print('sum=',sum([1,2,3,4,5,6]))
# print('sum=',sum((10.5,23.4,55,26)))

''' reversed-list '''
# for a in reversed([1,2,3,4,5,6]):
#     print(a)

''' reversed-tuple '''
# for i in reversed((1,3,5,7,9)):
#     print(i)

''' enumerate() '''
# a=['lokesh','sai','hari']
# b=enumerate(a)
# print(type(b))
# print(list(b))
# print(tuple(b))
# print(dict(b))

# a=['milk','bread','python']
# c=enumerate(a,-3)
# print(list(c))