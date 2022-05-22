#Check if given number n is 10 and Print multiplication table for the n
n=int(input('Enter the value : '))
if n==10:
    for i in range (1,11):
        print(f'{n} x {i} =  {n*i}')
else:
    print('Given number is not 10')      