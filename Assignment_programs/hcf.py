from cgitb import small

def calculate_hcf(a,b):
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if((a%i==0) & (b%i==0)):
            hcf=i
        
    return hcf
n1=int(input('Enter the first number : '))
n2=int(input('Enter the second number : '))
print(calculate_hcf(n1,n2))