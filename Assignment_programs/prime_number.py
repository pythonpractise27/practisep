#10.Check if a number is prime or not 
n=int(input('Enter the value : '))
if (n%2==0 & (n==0|n==1)):
    print(f'Given number is not prime')
else:
    print(f'Given number is prime')    