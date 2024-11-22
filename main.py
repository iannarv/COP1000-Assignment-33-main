def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_valid_date(year, month, day):
    """Validate the date with consideration for leap years."""
    # Check year validity
    if year <= 0:
        return False
    
    # Check month validity
    if month < 1 or month > 12:
        return False
    
    # Days in each month (non-leap year)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust February for leap years
    if is_leap_year(year):
        days_in_month[2] = 29
    
    # Check day validity
    if day < 1 or day > days_in_month[month]:
        return False
    
    return True

# Get input from user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day: "))

# Validate and output the result
if is_valid_date(year, month, day):
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")