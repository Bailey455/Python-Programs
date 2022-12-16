def get_first_day_year():
    user_day = int(input('Enter the first day of the year, (ex. Sunday = 0, Monday = 1, Tuesday = 2, etc.):'))    
   
    if user_day > 6 and user_day < 0:
        print('Enter the first day of the year, (ex. Sunday = 0, Monday = 1, Tuesday = 2, etc.):')
    else:
        return user_day

def first_day():
    if get_first_day_year == 0:
        user_day = 'Sun'
    elif get_first_day_year == 1:
        user_day = 'Mon'
    elif get_first_day_year == 2:
        user_day = 'Tue'
    elif get_first_day_year == 3:
        user_day = 'Wed'
    elif get_first_day_year == 4:
        user_day = 'Thu'
    elif get_first_day_year == 5:
        user_day = 'Fri'
    elif get_first_day_year == 6:
        user_day = 'Sat'
    return user_day

def days_in_month(month, year):
    if ((year % 4 ==0) and (year % 100 != 0)) or (year % 400 == 0):
        leap = True
    else:
        leap = False

    amount_days = 0

    if (leap == True) and (month == 1):
        amount_days == 29
    elif (leap == False) and (month ==1):
        amount_days == 28
   
    if month == 0:
        amount_days = 31
    elif month == 2:
        amount_days = 31
    elif month == 3:
        amount_days = 30
    elif month == 4:
        amount_days = 31
    elif month == 5:
        amount_days = 30
    elif month == 6:
        amount_days = 31
    elif month == 7:
        amount_days = 31
    elif month == 8:
        amount_days = 30
    elif month == 9:
        amount_days = 31
    elif month == 10:
        amount_days = 30
    elif month == 11:
        amount_days = 31
    return amount_days

def month_name(month_int):
    if month_int == 0:
        month = 'January'
    elif month_int == 1:
        month = 'February'
    elif month_int == 2:
        month = 'March'
    elif month_int == 3:
        month = 'April'
    elif month_int == 4:
        month = 'May'
    elif month_int == 5:
        month = 'June'
    elif month_int == 6:
        month = 'July'
    elif month_int == 7:
        month = 'August'
    elif month_int == 8:
        month = 'September'
    elif month_int == 9:
        month = 'October'
    elif month_int == 10:
        month = 'November'
    elif month_int == 11:
        month = 'December'
    return month

def print_month(year, month, user_day):
    print(f'{month} - {year}')
    print('-----------------------------')
    print('Sun Mon Tue Wed Thu Fri Sat ')

    fin = 0
    while fin < user_day:
        print('{:4s}'.format(''), end = '')
        fin += 1
    fin = 1
    while fin <= days_in_month:
        print('{:4d}'.format(fin), end = '')
        user_day += 1 

        if user_day % 7 == 0:
            print('')
            user_day = 0 
        fin += 1 
    return user_day

if __name__ == '__main__':
    year = int(input('Enter a year for calender:'))
    first_day = get_first_day_year()

    print()
    print(f'===Calendar for {year}===')
    print()

    for month in range(0,11):
        first_day = print_month(year, month, first_day)

        print('')
        print('')