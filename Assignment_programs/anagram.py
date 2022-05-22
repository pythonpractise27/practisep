# 13.Check if two given numbers are Anagram or not - hint: use list/string functions to do this
n1=input('Enter the first input value with two digits: ')
n2=input('Enter the second input value with two digits: ')
print(f'{sorted(n1)}')
print(f'{sorted(n2)}')
if sorted(n1) == sorted(n2):
    print(f'Given numbers are anagram')
else:    
    print(f'Given numbers are not anagram')