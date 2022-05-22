a=float(input('Enter the value of a :'))
b=float(input('Enter the value of b :'))
action = input('operator (sum/sub/mul/mod/div):')

match action:
    case 'sum':
        print(f'{a+b}')
    case 'sub':
        print(f'{a-b}')
    case 'mul':
        print(f'{a*b}')
    case 'mod':
        if b!=0:
            print(f'{a%b}')
        else:
            print('Cant divided by 0')
        
    case 'div':
        if b!=0:
           print(f'{a/b}')
        else:
            print('cant divide by zero')
    case _ :
        print('Operator not supported')        
        
            
