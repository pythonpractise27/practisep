import modul
#import modul as m #alias for the module
# from modul import add #calling single function
# from modul import variable_num as x,add as y
# print(x)
print(modul.variable_num)
n1=int(input('Enter the value n1 : '))
n2=int(input('Enter the value n2 : '))
# y(n1,n2)
modul.add(n1,n2)
modul.product(n1,n2)


for i in range(1,10):
    print(modul.random.uniform(1,5))