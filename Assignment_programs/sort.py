# 20. Can you sort below names list and print the count ? 
#   names = ['sri',,'kavi','shillu','marry','soujanya','devi','rajini','bhargavi']

names = ['sri','kavi','shillu','marry','soujanya','devi','rajini','bhargavi']
names.sort(reverse=False)
print(f'Ascending order of the given list : {names}')
print (f'Length / count of the names array is : {len(names)}')
names.sort(reverse=True)
print(f'Descending order of the list : {names}')