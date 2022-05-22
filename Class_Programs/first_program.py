from unicodedata import name

name="Hare Krishna Hare Rama"
print(name.upper())
print(name.lower())
print(name[0:4].upper())
print(name[0:4])
print(name.replace('Krishna','Rama'))
new_name=name.split()
print(new_name)
print(' '.join(new_name))

#Giving input during the runtime
#if:elif:else: with indentation
Name=input("Enter the name:")
print(f"Given name is {Name}")