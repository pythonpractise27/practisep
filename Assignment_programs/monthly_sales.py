# 24. The e-commerce company Bookshelf wishes to analyse its monthly sales data between minimum range 30 to max range 100. The company has categorized these book sales into four groups depending on 
# the number of sales with the help of these groups the company will know which stock they should increase or decrease in their inventory for the next month. 
# the groups are as follows

# 	sales range		groups
# 	30-50 ------------------> D
# 	51-60 ------------------> C
# 	61-80 ------------------> B
# 	81-100 -----------------> A

# 	write a program to find the group for the given book sale count

book_sale_count=int(input('Enter the number of book sale count : '))
if (book_sale_count>=30) & (book_sale_count<=50):
    print('Range is D')
elif (book_sale_count>50) & (book_sale_count<=60):
    print('Range is C')    
elif (book_sale_count>60) & (book_sale_count<=80):
    print('Range is B')    
elif (book_sale_count>80) & (book_sale_count<=100):
    print('Range is A')    