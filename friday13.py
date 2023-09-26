import datetime
import calendar

def find_Friday_13(year,month):
    #Get the thirteen day of the month
    day_13_of_the_month = datetime.date(year,month,13)
    print("The thirteenth day of month {} and year {} is a {}.".format(month,year,day_13_of_the_month.strftime("%A"))) 
    if day_13_of_the_month.weekday() == 4:
       return True
    return False

find_Friday_13(year=2023,month=3)
find_Friday_13(year=2024,month=11)
