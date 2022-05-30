# 32. Implement a program to calculate  sum of digits divisble by 3
num= int(input('Enter the number : '))
sum=0
for num1 in str(num):
    sum=sum+int(num1)
print(f'Sum of given number is : {sum}')    
if sum%3==0:
    print('Sum of given number is divisble by 3')
else:
    print('Sum of given number''s  is not  divisble by 3')    