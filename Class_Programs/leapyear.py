year=int(input('Enter the year : '))
if (year%4==0&year%100!=0)|year%400==0:
    print('Given year is Leap year')
else:
    print('GIven year is not leap year')    