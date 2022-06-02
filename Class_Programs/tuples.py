a=(1,2,3,4)
print(len(a))
b=('singlevaluetuple',)
print(b)
print(a[-1]) #returning the last value of the tuple
d=('sita','ram','lakshman','hanuman','jaya','Rama')
#slicing
print(d[1:4:1])
print(d[::])
print(d[:2:])
print(d[-4:-1])

for i in d:
    print(i)

# converting tuple to list
print(type(d))
e=list(d)
print(e)
e.append('Krishna')
print(e)
(a,b,*c)=d
print(a)
print(b)
print(c)