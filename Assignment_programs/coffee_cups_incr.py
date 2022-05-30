#For each of 6 coffee cups I buy, 
# I get a 7th cup free,In total I get 7 cups.
# Implement a program that takes n cups bought and
# print as an integer, the total number of cups I would get.

n=int(input('Enter the number of cups : '))

if n>=6:
    n= n+n//6
    print (f'number of cups {n}')
else:
    print (f'number of cups given are : {n}')