# 20. Can you sort below names list and print the count ? 
#   names = ['sri',,'kavi','shillu','marry','soujanya','devi','rajini','bhargavi']

from itertools import count


names = ['sri','kavi','shillu','marry','soujanya','devi','rajini','bhargavi']
names.sort(reverse=False)
print(f'Ascending order of the given list : {names}')
print (f'Length / count of the names array is : {len(names)}')
names.sort(reverse=True)
print(f'Descending order of the list : {names}')
names.append('Anand')
names.append('Nithin')
print(f'After appending the names : {names}')
names.sort(reverse=True)
print(f'Descending order of the list after appending : {names}')
num_peope_list=len(names)
print(num_peope_list)
