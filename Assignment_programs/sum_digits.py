# 28. Implement a program to calculate sum of digits present in the given number

num=int(input('Enter the number more than 2 digits: '))
sum=0
for i in str(num):
    # sum=sum+int(i)
    sum+=int(i)
print(sum)