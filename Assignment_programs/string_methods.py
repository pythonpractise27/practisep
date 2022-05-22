#Can you convert the first letter of the given sentence to upper case "move forward,"
a='move forward'
a1=a.capitalize()
print(f' {a.capitalize()}') #Changing only first letter to upper case
# print(f' {a.title()}') #Converting all the first letters of the word to upper case
# print(f' {a.upper()}') #converting whole text to capital letters


# Can you make the below sentence to have only lower case values
#     "learn lessons" 
b='learn lessons'
b1=b.lower()
print(f'{b.lower()}')

#Can you convert all characters in below sentence to upper case "and dump the past"
c='and dump the past '
c1=c.upper()
print(f'{c.upper()}')
# print(f'Output of all 3 messages are : {a1} {b1} {c1}')

print(''.join([a.capitalize(),' ', b.lower(),' ',c.upper()]))

    