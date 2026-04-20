#Program to find area of triangle when length of sides are given.

a=float(input("Enter the length of side A : "))
b=float(input("Enter the length of side B : "))
c=float(input("Enter the length of side C : "))

if a+b>c and b+c>a and c+a>b :
    s=(a+b+c)/2                           #semi-perimeter
    Area=(s*(s-a)*(s-b)*(s-c))**0.5        #Heron's Formula
    print("The Area of the given triangle is :",Area)
else :
    print("The given sides do not form a valid triangle.")
