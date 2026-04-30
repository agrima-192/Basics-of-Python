#Program to find whether a given year is a leap year or not.

year=int(input("Enter the Year to check: "))

if (year%400==0) or ((year%4==0 and year%100!=0)) :
    print(year,"is a Leap Year.")
else:
    print(year,"is a NOT a Leap Year.")
