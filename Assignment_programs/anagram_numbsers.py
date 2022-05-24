# 13.Check if two given numbers are Anagram or not - hint: use list/string functions to do this
n1=int(input('Enter the first input value with two digits: '))
n2=int(input('Enter the second input value with two digits: '))
print(sorted(str(n1)))
print(sorted(str(n2)))
if sorted(str(n1)) == sorted(str(n2)):
    print(f'Given numbers are anagram')
else:    
    print(f'Given numbers are not anagram')