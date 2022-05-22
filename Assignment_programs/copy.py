
from itertools import count


developer=[]
developer.insert(1,'Python')
developer.insert(1,'Git')
developer.insert(1,'Jira')
developer.insert(2,'Git')
developer.insert(3,'Jira')
print (f'This the developer list : {developer}')

new_copied_list=developer.copy()
print (f'This the developer list copied  : {new_copied_list}')
print(f'Print only first 2 values from the list : {new_copied_list[:2]}' )


print(f'Remove the Last element : {new_copied_list[:-1]}' )

developers_count=developer.count('Git')
print(f'Count of the given value from list : {developers_count}' )

#len
#tuple has index and count
