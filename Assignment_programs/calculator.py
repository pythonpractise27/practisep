a=float(input('Enter the value of a :'))
b=float(input('Enter the value of b :'))
action = input('operator (add/sub/mul/div):')

if action == 'add':
   print(f'{a+b}')
elif action == 'sub':
    print(f'{a-b}')
elif action == 'mul':
    print(f'{a*b}')    
elif action == 'div':
    print(f'{a/b}')
else:
    print('Action not recognised')

