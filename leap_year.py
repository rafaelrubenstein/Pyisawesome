def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
print("Please enter a year to see if it is a leap year")
user_year = int(input())
while user_year <= 0:
    print("Please enter a year that is a positive number")
    user_year = int(input())
