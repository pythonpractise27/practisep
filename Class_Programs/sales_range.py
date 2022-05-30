books_sale=int(input('Enter the sale number of units : '))

if books_sale>=30 & books_sale<=50:
    print('Range of the group is D')
elif books_sale>50 & books_sale<=60:
    print('Range of the group is C')
elif books_sale>60 & books_sale<=80:
    print('Range of the group is B')
elif books_sale>=81 & books_sale<=100:
    print('Range of the group is A')
else:
    print('Range is not the give list')