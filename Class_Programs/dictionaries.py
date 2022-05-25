# Stoes the value in key pair
# {
#     key1 : value1,
#     key2 : value2,
#     ......
    
#     keyn : valuen
# }
# login={'uname':'Krishna','pwd':'Ram'}
# print(login['uname'])
record={}
sentence=['the','quick','brown','fox','jumped','over','the','lazy','dog']
i=1
for words in sentence:
    record[i]=words
    i+=1
record[10]='cat'    
print(record)
