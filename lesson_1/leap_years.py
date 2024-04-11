year = input('Enter the year to determine if it is a leap year: ')
def is_leap_year(year):

    if year > 1751:    
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return year % 4 == 0
    else:
        return year % 4 == 0
    


    
