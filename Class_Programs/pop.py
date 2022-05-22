developer=[]
developer.insert(1,'Python')
developer.insert(1,'Git')
developer.insert(1,'Jira')
developer.insert(2,'Git')
developer.insert(3,'Jira')
print (f'This the developer list : {developer}')

element=developer.pop()
print (f'This the developer list after implementing pop : {element}')


rm_element=developer.remove('Python')

print (f'Removed element : {rm_element}')