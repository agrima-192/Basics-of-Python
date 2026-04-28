#Program to find the greatest among the three numbers,
#assuming no two values are same.

x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))
z=int(input("Enter the third number : "))

if x>y and x>z :
    print ("The number",x,"is greatest.")
elif y>x and y>z :
    print ("The number",y,"is greatest.")
else :
    print ("The number",z,"is greatest.")
