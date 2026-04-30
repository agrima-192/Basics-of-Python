#Program to take any date as input and display next date of the calendar

print("Enter the following details of the date :")
d = int(input("Day="))
m = int(input("Month="))
y = int(input("Year="))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    days_in_month[1] = 29

if d < days_in_month[m - 1]:
    d += 1
else:
    d = 1
    if m == 12:
        m = 1
        y += 1
    else:
        m += 1

print(f"The next date: day={d} month={m} year={y}")
