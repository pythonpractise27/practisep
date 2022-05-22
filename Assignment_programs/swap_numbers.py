from os import TMP_MAX


a=int(input("Enter the first value : "))
b=int(input("Enter the second value : "))
print(f"Value of a before swapping : {a}")
print(f"Value of b before swapping : {b}")
temp=a
a=b
b=temp
print(f"Value of a after swapping : {a}")
print(f"Value of b after swapping : {b}")