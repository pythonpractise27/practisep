def calculate_lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if ((greater%a==0) & (greater%b==0)):
            lcm1=greater
            break
        greater+=1
    return lcm1        
n1=int(input('Enter the first number : '))
n2=int(input('Enter the second number : '))
print(calculate_lcm(n1,n2))