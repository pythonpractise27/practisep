# 37. Write a program to reverse a number (without using any built in functions)
num=int(input('Enter the number more than 2 digits: '))
rev=0
while num>0:
    rev=(rev*10)+(num%10)
    num=num//10
print(rev)    