
def leapyear(year):
    if (year % 100 == 0) and (year % 400 == 0):
        print('leap year')
    elif (year % 4 == 0) and (year % 100 != 0):
        print('leap year')
    else:
        print('not leap year')


year = int(input('Enter a year to check leap year or not: '))
leapyear(year)



