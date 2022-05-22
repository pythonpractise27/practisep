#  Can you count how many tea's we have in below drinks list .
# 		-Also can you first pop one element from the drinks list and print it.
#             -Can you also remove 'cough_syrup' element and print the final list ?

#      drinks= ['tea','milk','tea','coffee','water','tea','lemonide','tea','coffee','cough_syrup','']

drinks= ['tea','milk','tea','coffee','water','tea','lemonide','tea','coffee','cough_syrup','']
#print(f'count of teas in drinks list are str({drinks.count('tea')})')
n=int(input('Enter the index number that to be removed from the list : '))
print(drinks.count('tea'))
popped_out_drink=drinks.pop(n)
print(f'Popped out drink is : {popped_out_drink}')
print(f'Drinks list : {drinks}')
removed_drink=drinks.remove('cough_syrup')
print(f'Removed drink is : {removed_drink}')
print(f'List if drinks after popped out & removal : {drinks}')