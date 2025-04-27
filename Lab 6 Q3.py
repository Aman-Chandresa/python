date1 = (1, 1, 2025)
date2 = (12, 12, 2024)

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 0

def total_days(date):
    day, month, year = date
    total_days = day
    
    for m in range(1, month):
        total_days += days_in_month(m, year)
    
    for y in range(1, year):
        total_days += 365 + (1 if is_leap_year(y) else 0)
    
    return total_days

total_days_date1 = total_days(date1)
total_days_date2 = total_days(date2)

days_difference = abs(total_days_date2 - total_days_date1)

print("Number of days between the two dates:", days_difference)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")