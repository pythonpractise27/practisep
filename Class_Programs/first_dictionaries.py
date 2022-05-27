# my_dict={'name':['Krishna','Ram','Pradyumna'],'age':[20,20,30]}
# print(my_dict['name'][2])
# print(my_dict['age'][2])

my_dict=dict([(1,'Mary'),(2,'Soujanya'),(3,'Sri')])
print(my_dict.get(3))
print(my_dict.get(4))
# removing the item from the dictionary
my_dict.pop(2) 

print(my_dict)
# Appending the dictionary
my_dict[2]='Rama'
my_dict[3]='Anand'
my_dict[4]='Bhargavi'
my_dict[5]='Krishna'
print(my_dict)
for key in my_dict:
   print( my_dict[key])