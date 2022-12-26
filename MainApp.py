from datetime import date

def my_function(date2):
    currentDate = date.today()
    currentYear = currentDate.year
    date1 = date(currentYear,1,1)
    days = abs(date1-date2).days
    return days // 7

date2 = date(2001,5,11)
print(my_function(date2))