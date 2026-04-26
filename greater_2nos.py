#Program to find the greatest among the two numbers.
#If the numbers are equal then print "numbers are equal".

x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))

if x>y :
    print ("The number",x,"is greater than",y)
elif y>x :
    print ("The number",y,"is greater than",x)
else :
    print ("The numbers are equal.")
